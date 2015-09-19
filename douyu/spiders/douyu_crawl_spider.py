# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from douyu.items import RoomCard


class DouyuCrawlSpiderSpider(CrawlSpider):
    name = 'douyu_crawl_spider'
    allowed_domains = ['douyutv.com']
    start_urls = [
        'http://www.douyutv.com/directory/all?page={}'.format(i)
        for i in range(1, 30)
    ]

    rules = (
        Rule(LinkExtractor(
            allow=r'http://www\.douyutv\.com/directory/all\?page=\d'),
            callback='parse_item',
            follow=True),
    )

    def parse_item(self, response):
        cards = response.xpath('//div[contains(@id, "item_data")]/ul/li')
        for index, card in enumerate(cards):
            item = RoomCard()
            item['zbTitle'] = card.xpath(".//h1/text()").extract()[0]
            item['zbViewer'], item['zbPlayer'] = card.xpath(
                ".//p/span/text()").extract()
            item['zbType'] = card.xpath(".//em/text()").extract()[0]
            if u"万" in item['zbViewer'] or '.' in item['zbViewer']:
                item['zbViewer'] = float(item['zbViewer'].strip(u'万')) * 10000
                item['zbViewer'] = int(item['zbViewer'])
            else:
                item['zbViewer'] = int(item['zbViewer'])

            print response.url
            print index
            yield item
