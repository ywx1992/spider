# -*- coding: utf-8 -*-
import scrapy
import re

class GithubSpider(scrapy.Spider):
    name = 'login2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract_first()
        utf8 = response.xpath("//input[@name='utf8']/@value").extract_first()
        commit = response.xpath("//input[@name='commit']/@value").extract_first()
        post_data = dict(
            login="841896368@qq.com",
            password="blue841896368",
            authenticity_token=authenticity_token,
            utf8=utf8,
            commit=commit
        )
        yield scrapy.FormRequest(
            "https://github.com/session",
            formdata=post_data,
            callback=self.after_login
        )

    def after_login(self,response):
        # with open("a.html","w",encoding="utf-8") as f:
        #     f.write(response.body.decode())
        print(re.findall("841896368",response.body.decode()))
