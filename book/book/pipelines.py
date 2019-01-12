# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime


class BookPipeline(object):
    def process_item(self, item, spider):
        item["crawled"] = datetime.utcnow()
        print(item)
        return item


# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
import requests
r = requests.get('https://baidu.com')







