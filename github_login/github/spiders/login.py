# -*- coding: utf-8 -*-
import scrapy
import re


class Github2Spider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response, #自动的从response中寻找from表单
            formdata={"login":"841896368@qq.com","password":"blue841896368"},
            callback = self.after_login
        )

    def after_login(self,response):
        print(re.findall("myblog",response.body.decode()))
