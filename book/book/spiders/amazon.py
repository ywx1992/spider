# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider


class AmazonSpider(RedisCrawlSpider):
    name = 'amazon'
    allowed_domains = ['amazon.cn']
    # start_urls='https://www.amazon.cn/gp/book/all_category/ref=sv_b_1'
    redis_key = 'amazon'

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='a-row a-size-base']/div[2]//td/a",)), follow=True),
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='mainResults']/ul/li//h2/..",)), callback='parse_book_detail'),
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='pagn']",)), follow=True),
    )

    def parse_book_detail(self, response):
        item = dict()
        item["book_title"] = response.xpath("//span[@id='productTitle']/text()").extract_first()
        if item["book_title"] is None:
            item["book_title"] = response.xpath("//span[@id='ebooksProductTitle']/text()").extract_first()
        item["book_author"] = response.xpath("//span[@class='author notFaded']/a/text()").extract()
        # 例如排除一个属性的节点可以使用//tbody/tr[not(@class)]来写，排除一个或者两个属性可以使用//tbody/tr[not(@class or @id)]来选择
        item["book_cate"] = response.xpath("//div[@id='wayfinding-breadcrumbs_feature_div']/ul/li[not(@class)]/span/a/text()").extract()
        item["book_cate"] = [i.strip() for i in item["book_cate"]]
        # item["book_img"] = response.xpath("//div[@id='img-canvas']/img/@src").extract_first()
        item["book_price"] = response.xpath("//div[@id='soldByThirdParty']/span[2]/text()").extract_first()
        if item["book_price"] is None:
            item["book_price"] = response.xpath("//tr[@class='kindle-price']/td[2]/text()").extract_first()
            if item["book_price"] is not None:
                item["book_price"] = item["book_price"].strip()
        print(item)

