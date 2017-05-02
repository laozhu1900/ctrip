#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy
from scrapy.selector import Selector
from scrapy.spider import Spider
from ..items import HotelItem
from conf import HotelConf
import os

urls = HotelConf().hotel_info['start_url']


class HotelSpider(Spider):
    name = "hotel"
    allowed_domains = ["hotels.ctrip.com"]

    start_urls = [urls]

    def parse(self, response):
        for url in response.xpath('//li[@class="searchresult_info_name"]/h2[@class="searchresult_name"]/a/@href').re(r'.*/\d*.html'):
            yield scrapy.Request(response.urljoin(url), self.parse_item)

        # crawl next page

        sites = response.xpath('//div[@class="c_page_list layoutfix"]/a/text()').extract()[-1]
        pages = int(sites)
        i = 1
        while i < pages:

            next_url = os.path.join(urls, "p" + str(i+1))
            yield scrapy.Request(response.urljoin(next_url), self.parse)
            i += 1

    def parse_item(self, response):

        item = HotelItem()
        item['name'] = response.xpath('//h2[@class="cn_n"]/text()').extract()[0]
        item['url'] = response.url

        yield item
