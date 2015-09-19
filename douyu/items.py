# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class RoomCard(scrapy.Item):
    zbTitle = scrapy.Field()
    zbViewer = scrapy.Field()
    zbPlayer = scrapy.Field()
    zbType = scrapy.Field()
