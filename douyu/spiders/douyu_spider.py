# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.exceptions import IgnoreRequest
from douyu.items import RoomCard


class DouyuSpiderSpider(scrapy.Spider):
    name = "douyu_spider"
    allowed_domains = ["douyutv.com"]
    start_urls = (
        'http://www.douyutv.com/directory/all?page=1',
    )
    url_prefix = 'http://www.douyutv.com/directory/all?page={}'
    crawled_page = set()

    def parse(self, response):
        page_count = int(
            response.selector.re('pageCount:parseInt\("(\d+)"\)')[0])
        complete_urls = map(
            lambda x: self.url_prefix.format(x), range(1, page_count + 1))
        for url in complete_urls:
            yield Request(url=url, callback=self.parse_html)

    def parse_html(self, response):
        current_page = int(
            response.selector.re('current:parseInt\("(\d+)"\)')[0])
        if current_page in self.crawled_page:
            raise IgnoreRequest('crawled')
        self.crawled_page.add(current_page)

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

    def close(self, reason):
        print reason
        print self.crawled_page
