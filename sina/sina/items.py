# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 大类标题、url
    b_title = scrapy.Field()
    b_urls = scrapy.Field()

    # 小类标题、url
    s_title = scrapy.Field()
    s_urls = scrapy.Field()

    # 文章标题、正文、url
    title = scrapy.Field()
    content = scrapy.Field()
    urls = scrapy.Field()
