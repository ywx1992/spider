# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonItemExporter
import json
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from douyuapp.settings import IMAGES_STORE
import os


class DouyuImagesPipeline(ImagesPipeline):
    # 发送图片链接请求,响应会保存在settings中指定的路径下(IMAGES_STORE)
    def get_media_requests(self, item, info):
        image_url = item["img_url"]
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        '''
        :param results: 下载图片结果,包含一个二元组（下载状态，图片路径）
        :param item:
        :param info:
        :return:
        '''
        # 获取图片路径，同时判断这个路径是否正确，如果正确，就放到 image_path里
        image_path = [x['path'] for ok, x in results if ok]

        # 将原本路径的图片名，修改为新建的图片名
        os.rename(IMAGES_STORE + '/' + image_path[0], IMAGES_STORE + '/' + item['nickname'] + '.jpg')


        return item





# class DouyuappPipeline(object):
    # def __init__(self):
    #     self.file = open('douyu.json', 'wb')
    #     self.exporter = JsonItemExporter(self.file, ensure_ascii=False)
    #     self.exporter.start_exporting()
    #
    # def close_spider(self, spider):
    #     self.exporter.finish_exporting()
    #     self.file.close()
    #
    # def process_item(self, item, spider):
    #     self.exporter.export_item(item)
    #     return item


    # def __init__(self):
    #     self.file = open('douyu2.json', 'w')
    #     self.file.write('[')
    #
    # def close_spider(self, spider):
    #     self.file.write(']')
    #     self.file.close()
    #
    # def process_item(self, item, spider):
    #     data = json.dumps(dict(item), ensure_ascii=False) + ','
    #     self.file.write(data)
    #     return item


# import json
# class JsonWriterPipeline(object):
#
#     def open_spider(self, spider):
#         self.file = open(spider.settings.get("SAVE_FILE", "./temp.json"), "w")
#
#     def close_spider(self,spider):
#         self.file.close()
#
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item)) + "\n"
#         self.file.write(line)
#         return item
