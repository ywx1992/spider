# -*- coding: utf-8 -*-
import scrapy
from douban250.items import Douban250Item
import re


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        item = Douban250Item()
        info_list = response.xpath("//div[@class='info']")
        for info in info_list:
            item["title"] = info.xpath(".//span[@class='title'][1]/text()").extract_first()

            item["score"] = info.xpath(".//span[@class='rating_num']/text()").extract_first()

            item["content"] = info.xpath("./div[@class='bd']/p/text()").extract()
            # item["content"] = [re.sub(r"\xa0|\s", " ", i) for i in item["content"]]
            item["content"] = [i.strip().replace("\xa0", " ") for i in item["content"] if len(i.strip()) > 0]

            item["info"] = info.xpath(".//p[@class='quote']/span/text()").extract_first()

            yield item

        next_page_url = response.xpath("//a[text()='后页>']/@href").extract_first()
        if next_page_url is not None:
            next_page_url = response.urljoin(next_page_url)
            # print(next_page_url)
            yield scrapy.Request(next_page_url, callback=self.parse)
