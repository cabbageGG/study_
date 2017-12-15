# -*- coding: utf-8 -*-
import scrapy, re
from scrapy.http import Request
from urllib import parse

from AticleSpider.items import JobBoleArticleItem, JobBoleArticleItemLoader

from AticleSpider.utils.common import get_md5
from selenium import webdriver
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    # def __init__(self):
    #     self.browser = webdriver.Chrome(executable_path="/Users/dev/Desktop/chromedriver")
    #     super(JobboleSpider, self).__init__()
    #     dispatcher.connect(self.spider_closed, signals.spider_closed)
    #
    # def spider_closed(self, spider):
    #     #当爬虫退出的时候关闭chrome
    #     print ("spider closed")
    #     self.browser.quit()


    def parse(self, response):
        """
        1、获取每一页的urls
        2、获取下一页的url
        """
        if response.status == 404:
            print('failed 404')

        post_nodes = response.css('#archive .floated-thumb .post-thumb a')
        for post_node in post_nodes:
            image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url), meta={'front_image_url':image_url}, callback=self.parse_detail)

        next_url = response.css(".next.page-numbers::attr(href)").extract_first("")
        if next_url:
           yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):

        '''
        1、单个url的字段解析
        '''

        # article_item = JobBoleArticleItem()
        #
        # #使用xpath获取字段内容
        # front_image_url = response.meta.get('front_image_url', '')
        # title = response.xpath('//div[@class="entry-header"]/h1/text()').extract_first("")                                                #标题
        # create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace('·','').strip()  #创建时间
        # fav_nums = response.xpath("//span[contains(@class, bookmark-btn)]/text()").extract()[0]                                            #收藏数
        # match_re = re.match('.*?(\d+).*', fav_nums)
        # if match_re:
        #     praise_numfav_nums = int(match_re.group(1))
        # else:
        #     fav_nums = 0
        # praise_nums = response.xpath("//span[contains(@class, vote-post-up)]/h10/text()").extract()[0]                                     #点赞数
        #
        # comment_num = response.xpath("//a[@href='#article-comment']/span/text()").extract()[0]                                             #评论数
        # match_re = re.match('.*?(\d+).*', comment_num)
        # if match_re:
        #     comment_num = int(match_re.group(1))
        # else:
        #     comment_num = 0
        #
        # content = response.xpath('//div[@class="entry"]').extract_first('')      #内容
        #
        # tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()
        # tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        # tags = ",".join(tag_list)
        #
        # #使用css获取字段内容
        # front_image_url = response.meta.get('front_image_url', '')
        # title = response.css('.entry-header h1::text').extract_first("")  #标题
        # create_date = response.css('p.entry-meta-hide-on-mobile::text').extract()[0].strip().replace('·', '').strip()  #创建时间
        # fav_nums = response.css(".bookmark-btn::text").extract()[0]      #收藏数
        # match_re = re.match('.*?(\d+)s.*', fav_nums)
        # if match_re:
        #     fav_nums = int(match_re.group(1))
        # else:
        #     fav_nums = 0
        #
        # praise_nums = response.css('span.vote-post-up h10::text').extract()[0]   #点赞数
        # comment_nums = response.css("a[href='#article-comment'] span::text").extract()[0]   #评论数
        # match_re = re.match('.*?(\d+)s.*', comment_nums)
        # if match_re:
        #     comment_nums = int(match_re.group(1))
        # else:
        #     comment_nums = 0
        #
        # content = response.css('div.entry').extract_first('')      #内容
        #
        # tag_list = response.css('p.entry-meta-hide-on-mobile a::text').extract()            #标签：包括作者昵称 和 分类等 去掉评论
        # tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        # tags = ",".join(tag_list)
        #
        # article_item['title'] = title
        # article_item['content'] = content
        # article_item['front_image_url'] = [front_image_url, ]
        # article_item['create_date'] = create_date
        # article_item['fav_nums'] = fav_nums
        # article_item['praise_nums'] = praise_nums
        # article_item['comment_nums'] = comment_nums
        # article_item['tags'] = tags
        # article_item['url'] = response.url
        # article_item['url_id'] = get_md5(response.url)


        #通过item loader加载item
        front_image_url = response.meta.get("front_image_url", "")  # 文章封面图
        item_loader = JobBoleArticleItemLoader(item=JobBoleArticleItem(), response=response)  #注意这里的传入参数
        item_loader.add_css("title", ".entry-header h1::text")
        item_loader.add_value("url", response.url)
        item_loader.add_value("url_id", get_md5(response.url))
        item_loader.add_css("create_date", "p.entry-meta-hide-on-mobile::text")
        item_loader.add_value("front_image_url", [front_image_url])
        item_loader.add_css("praise_nums", ".vote-post-up h10::text")
        item_loader.add_css("comment_nums", "a[href='#article-comment'] span::text")
        item_loader.add_css("fav_nums", ".bookmark-btn::text")
        item_loader.add_css("tags", "p.entry-meta-hide-on-mobile a::text")
        item_loader.add_css("content", "div.entry")

        article_item = item_loader.load_item()

        yield article_item