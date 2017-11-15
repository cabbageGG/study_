#!/bin/env python
# -*- coding:utf-8 -*-

import url_manager, html_downloader, html_parser, html_outputer

class spidermain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutPuter()

    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        count = 0
        while True:
            try:
                if self.urls.has_new_url():
                    html_url = self.urls.get_new_url()
                    html_page = self.downloader.download(html_url)
                    new_urls, url_data = self.parser.parse(html_page, html_url)
                    self.urls.add_new_urls(new_urls)
                    self.outputer.collect_data(url_data)
                    count = count + 1
                    print '%d craw %s' % (count, html_url.encode('utf-8'))
                    if count == 10:
                        break
                else:
                    break
            except:
                print 'craw fail'
        self.outputer.html_output()
    
if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313'
    spider = spidermain()
    spider.craw(root_url)