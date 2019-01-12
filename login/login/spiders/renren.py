# -*- coding: utf-8 -*-
import scrapy
import re


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ["http://www.renren.com/968371620/profile"]

    def start_requests(self):
        cookies = "anonymid=jnbb5u1m-ucorm0; _r01_=1; JSESSIONID=abc8MNL4SN4F-fJ4eB7zw; ick_login=86a82f0e-fe93-4c4b-a657-c92a04fecb24; depovince=GX; first_login_flag=1; ln_uact=15692092379; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebecookies=29bc250c-47e1-47db-bded-7cbbd35cd19c|||||; _de=9546EF04237D9B409BEACFB2B52206F3; p=ba73d5332325bd4be20bc14657ef218c0; t=117c69122c269d6780015c5c8aeead910; societyguester=117c69122c269d6780015c5c8aeead910; id=968371620; xnsid=5f279c0e; loginfrom=syshome"
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
        yield scrapy.Request(
            url=self.start_urls[0],
            callback=self.parse_page,
            cookies=cookies,
        )

    def parse_page(self, response):
        print(re.findall("李", response.body.decode()))
        print(response.url)
        with open("li.html", "w") as f:
            f.write(response.body.decode())

