# -*- coding: utf-8 -*-
import scrapy
from shdxxsbgSpider.items import ShdxxsbgspiderItem


class ShdxSpider(scrapy.Spider):
    name = 'shdx'
    allowed_domains = ['shu.edu.cn']
    start_urls = ['http://shu.edu.cn/']

    def parse(self, response):
        item = ShdxxsbgspiderItem()
        item['name'] = response.xpath('//div[@class="list-con"]/ul/li/a/div[1]/text()').get()
        item['time'] = response.xpath('//div[@class="list-con"]/ul/li/a/div[2]/text()').get()
        print(name)
        yield item


