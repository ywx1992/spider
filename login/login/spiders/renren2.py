# -*- coding: utf-8 -*-
import scrapy


class Renren2Spider(scrapy.Spider):
    name = 'renren2'
    allowed_domains = ['www.renren.com']

    def start_requests(self):
        url = "http://www.renren.com/PLogin.do"
        yield scrapy.FormRequest(
            url=url,
            callback=self.parse,
            formdata={"email": "15692092379", "password": "614131504"}
        )

    def parse(self, response):
        print(response.url)
        yield scrapy.Request(
            url="http://www.renren.com/321869744/profile",
            callback=self.parse_detail,
        )

    def parse_detail(self, response):
        print(response.url)

