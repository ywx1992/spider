# -*- coding: utf-8 -*-
import scrapy
from douyuapp.items import DouyuappItem
import json


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']
    # start_urls = ['https://apiv2.douyucdn.cn/gv2api/rkc/roomlistV1/0_0/0/20/android?client_sys=android']
    url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        data = json.loads(response.text)["data"]

        # 如果拿不到数据，说明已经爬取完所有翻页
        if not data:
            return

        for each in data:
            item = DouyuappItem()
            item["room_name"] = each["room_name"]
            item["nickname"] = each["nickname"]
            item["img_url"] = each["vertical_src"]

            yield item

        self.offset += 20
        yield scrapy.Request(self.url+str(self.offset), callback=self.parse)
