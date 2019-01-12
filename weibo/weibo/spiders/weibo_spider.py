# -*- coding: utf-8 -*-
import scrapy


class WeiboSpiderSpider(scrapy.Spider):
    name = 'weibo_spider'
    allowed_domains = ['m.weibo.cn']
    start_urls = ['https://m.weibo.cn/u/2803301701']

    def parse(self, response):
        pass
