#!/bin/env python
# -*- coding:utf-8 -*-

import urlparse, re, html_downloader
from bs4 import BeautifulSoup

class HtmlParser(object):
    def __init__(self):
        self.new_urls = set() 

    def parse(self, html_page, html_url):
        soup = BeautifulSoup(html_page, 'html.parser', from_encoding='utf-8')
        #/item/Python/407313
        links = soup.find_all('a', href=re.compile(r'/item/\S+'))
        for link in links:
            new_url = link['href']
            new_url_full = urlparse.urljoin(html_url, new_url)
            self.new_urls.add(new_url_full)

        url_data = {}
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        url_data['title'] = title_node.get_text()
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_="lemma-summary")
        url_data['summary'] = summary_node.get_text()
        #url
        url_data['url'] = html_url
        return self.new_urls, url_data

if __name__ == '__main__':
    '''
    the most important module
    need test and more excises
    '''
    print 'hello'
    root_url = 'https://baike.baidu.com/item/Python/407313'
    parser = HtmlParser()
    downloader = html_downloader.HtmlDownloader()
    html_page = downloader.download(root_url)
    urls, data = parser.parse(html_page,root_url)
    print urls
    print data

