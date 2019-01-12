# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        li_list = response.xpath("//div[@class='tea_con']//li")
        for li in li_list:
            item = {}

            item["img"] = li.xpath(".//img/@data-original").extract_first()
            item["name"] = li.xpath(".//h3/text()").extract_first()
            item["title"] = li.xpath(".//h4/text()").extract_first()
            item["info"] = li.xpath(".//p/text()").extract_first()

            yield item
