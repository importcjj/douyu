# -*- coding: utf-8 -*-
import scrapy
from douyu.items import RoomCard


class DouyuSpiderSpider(scrapy.Spider):
    name = "douyu_spider"
    allowed_domains = ["douyutv.com"]
    start_urls = (
        'http://www.douyutv.com/directory/all?page=1',
    )

    # def parse_urls(self, response):
    # pass

    def parse(self, response):
        cards = response.xpath('//div[contains(@id, "item_data")]/ul/li')
        for index, card in enumerate(cards):
            item = RoomCard()
            item['zbTitle'] = card.xpath(".//h1/text()").extract()[0]
            item['zbViewer'], item['zbPlayer'] = \
                card.xpath(".//p/span/text()").extract()
            item['zbType'] = card.xpath(".//em/text()").extract()[0]
            if u"万" in item['zbViewer'] or '.' in item['zbViewer']:
                item['zbViewer'] = float(item['zbViewer'].strip(u'万')) * 10000
                item['zbViewer'] = int(item['zbViewer'])

            print index
            yield item
