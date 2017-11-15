#!/bin/env python
# -*- coding:utf-8 -*-


class UrlManager(object):
    def __init__(self):
        self.old_urls = set()
        self.new_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
   
    def has_new_url(self):
        if len(self.new_urls) == 0:
            return False
        else:
            return True

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
            
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url