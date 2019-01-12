# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from sina.items import SinaItem


class NewsSpider(RedisSpider):
    name = 'news'
    allowed_domains = ['sina.com']
    # start_urls = ['http://news.sina.com.cn/guide/']
    redis_key = 'news:start_urls'

    def parse(self, response):
        item = SinaItem()
        div_list = response.xpath('.//div[@id="tab01"]/div')[:-1]
        for div in div_list:
            item['b_title'] = div.xpath('./h3/a/text()').extract_first()
            item['b_urls'] = div.xpath('./h3/a/@href').extract_first()

            for li in div.xpath('./ul/li'):
                item['s_title'] = li.xpath('./a/text()').extract_first()
                item['s_urls'] = li.xpath('./a/@href').extract_first()
                # print(item)

            yield scrapy.Request(item['s_urls'], callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):
        item = response.meta['item']
        urls = response.xpath('.//a/@href').extract_first()



