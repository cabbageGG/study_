# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
from AticleSpider.items import baikeItem, baikeItemLoader

class BaikeSpider(scrapy.Spider):
    name = 'baike'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/Python/407313']
    num = 0


    def parse(self, response):
        '''
        思考：1、应该需要运用深度优先或广度优先，
             2、还需要加深理解yield 机制
             这里应该是使用深度优先搜索url，当url达到5时，停止搜索url。此时5条请求已经发出，而解析字段还为完成，就等待继续完成。
        '''
        print('parse_detail')
        print(BaikeSpider.num)
        title = response.css('dd.lemmaWgt-lemmaTitle-title h1::text').extract()
        summary = response.css('div.lemma-summary div::text').extract()
        item_loader = baikeItemLoader(item=baikeItem(), response=response)
        item_loader.add_css("title", 'dd.lemmaWgt-lemmaTitle-title h1::text')
        item_loader.add_css("summary", 'div.lemma-summary div::text')

        baike_item = item_loader.load_item()

        yield baike_item
        # self.parse_detail(response)  这种的不会执行？？ 什么原因？？

        # links = response.xpath('//a[contains(@href, item)]').extract()
        links = response.css('a[href^="/item/"]::attr(href)').extract()

        for link in links:
            if BaikeSpider.num > 5:
                print('link')
                print(BaikeSpider.num)
                break
            else:
                BaikeSpider.num += 1 #这里很关键，需要理清思路，我们是需要5个url的请求。不是判断解析5次。
                yield Request(url=parse.urljoin(response.url, link), callback=self.parse)


    def parse_detail(self, response):
        print('parse_detail')
        title = response.css('dd.lemmaWgt-lemmaTitle-title h1::text').extract()
        summary = response.css('div.lemma-summary div::text').extract()
        item_loader = baikeItemLoader(item=baikeItem(), response=response)
        item_loader.add_css("title", 'dd.lemmaWgt-lemmaTitle-title h1::text')
        item_loader.add_css("summary", 'div.lemma-summary div::text')

        baike_item = item_loader.load_item()

        yield baike_item
