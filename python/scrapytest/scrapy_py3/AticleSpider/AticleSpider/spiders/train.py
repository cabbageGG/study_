# -*- coding: utf-8 -*-
import scrapy


class TrainSpider(scrapy.Spider):
    name = 'train'
    allowed_domains = ['kyfw.12306.cn']
    start_urls = ['https://kyfw.12306.cn/']

    def parse(self, response):
        pass
