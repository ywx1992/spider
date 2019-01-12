# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    b_cate = scrapy.Field()
    s_cate = scrapy.Field()
    s_href = scrapy.Field()
    name = scrapy.Field()
    img = scrapy.Field()
    press = scrapy.Field()
    author = scrapy.Field()
    sku = scrapy.Field()
    price = scrapy.Field()
