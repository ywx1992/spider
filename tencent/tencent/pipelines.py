# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from tencent.items import TencentItem


class TencentPipeline(object):
    def process_item(self, item, spider):
        if spider.name == "hr":
            print(item)
        if isinstance(item, TencentItem):
            print("- "*10)
        return item
