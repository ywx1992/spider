# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from scrapy.conf import settings

import pymysql


class Douban250Pipeline(object):
    # def __init__(self):
    #     # 获取数据库uri、数据库名、集合名
    #     mongo_uri = settings['MONGO_URI']
    #     mongo_db = settings['MONGO_DB']
    #     collection = settings['MONGO_COL']
    #     # 创建数据库连接，指向指定的数据库和集合
    #     self.client = MongoClient(mongo_uri)
    #     self.db = self.client[mongo_db]
    #     self.col = self.db[collection]

    # @classmethod
    # def from_crawler(cls, crawler):
    #     '''
    #             scrapy为我们访问settings提供了这样的一个方法，这里，
    #             我们需要从settings.py文件中，取得数据库的URI和数据库名称
    #     '''
    #     return cls(
    #         mongo_uri=crawler.settings.get('MONGO_URI'),
    #         mongo_db=crawler.settings.get('MONGO_DB')
    #     )

    def open_spider(self, spider):
        # print(spider.settings['MONGO_URI'])
        # print(spider.settings['MONGO_DB'])
        # print(spider.settings['MONGO_COL'])
        # 创建数据库连接，指向指定的数据库和集合
        self.client = MongoClient(spider.settings['MONGO_URI'])
        self.db = self.client[spider.settings['MONGO_DB']]
        self.col = self.db[spider.settings['MONGO_COL']]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.col.insert(dict(item))
        return item

    # 保存到mysql中
    def __init__(self):


