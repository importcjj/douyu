# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from douyu.model import DBSession
from douyu.model import (
    Index,
    RoomCard
)
from scrapy import log


class DouyuPipeline(object):

    def __init__(self):
        pass

    def process_item(self, item, spider):
        if 1:
            card = {
                "crawlIndex": self.crawl_index,
                "zbTitle": item['zbTitle'].encode('utf-8'),
                "zbPlayer": item['zbPlayer'].encode('utf-8'),
                "zbViewer": item['zbViewer'],
                "zbType": item['zbType'].encode('utf-8')
            }
            c = RoomCard.new(**card)
            self.write2db(c)
            return item
        else:
            raise DropItem("Message")

    def write2db(self, obj):
        DBSession().add(obj)
        DBSession().flush()
        return obj

    def open_spider(self, spider):
        index = self.write2db(Index())
        self.crawl_index = int(index.id)

    def close_spider(self, spider):
        DBSession().commit()
        DBSession().remove()

    # @classmethod
    # def from_crawler(cls, crawler):
    #     pass
