# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
import json
from book.items import BookItem


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com', 'p.3.cn']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        dt_list = response.xpath("//div[@class='mc']/dl/dt")  # 大分类列表
        for dt in dt_list:
            item = BookItem()
            item["b_cate"] = dt.xpath("./a/text()").extract_first()
            em_list = dt.xpath("./following-sibling::dd[1]/em")  # 小分类列表
            for em in em_list:
                item["s_cate"] = em.xpath("./a/text()").extract_first()
                item["s_href"] = em.xpath("./a/@href").extract_first()

                if item["s_href"] is not None:
                    item["s_href"] = "https:" + item["s_href"]
                    yield scrapy.Request(
                        item["s_href"],
                        callback=self.parse_book_list,
                        meta={"item": deepcopy(item)}
                    )

    def parse_book_list(self, response):
        item = response.meta["item"]
        li_list = response.xpath("//div[@id='plist']/ul/li")
        for li in li_list:
            item["name"] = li.xpath(".//div[@class='p-name']/a/em/text()").extract_first().strip()
            item["img"] = li.xpath(".//div[@class='p-img']/a/img/@src").extract_first()
            if item["img"] is None:
                item["img"] = li.xpath(".//div[@class='p-img']/a/img/@data-lazy-img").extract_first()
            item["img"] = "https:" + item["img"]
            item["press"] = li.xpath(".//span[@class='p-bi-store']/a/text()").extract_first()
            item["author"] = li.xpath(".//span[@class='author_type_1']/a/text()").extract()
            item["sku"] = li.xpath("./div/@data-sku").extract_first()
            yield scrapy.Request(
                "https://p.3.cn/prices/mgets?skuIds=J_{}".format(item["sku"]),
                callback=self.parse_price,
                meta={"item": deepcopy(item)}
            )

        next_url = response.xpath("//a[@class='pn-next']/@href").extract_first()
        if next_url is not None:
            yield scrapy.Request(
                "https://list.jd.com" + next_url,
                callback=self.parse_book_list,
                meta={"item": item}
            )

    def parse_price(self, response):
        item = response.meta["item"]
        item["price"] = json.loads(response.body.decode())[0]["op"]
        yield item
