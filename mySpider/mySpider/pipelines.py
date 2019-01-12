# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging


logger = logging.getLogger(__name__)


class MyspiderPipeline(object):
    def process_item(self, item, spider):
        item["end"] = "结尾"
        return item

       
class MyPipeline(object):
    def process_item(self, item, spider):
        if spider.name == "itcast":
            print(item)


class MyspiderPipeline1(object):
    def process_item(self, item, spider):
        if item['come_from'] == 'itcast1':
            logger.warning("*  " * 10)
            return item

