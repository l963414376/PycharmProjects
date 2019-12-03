# -*- coding: utf-8 -*-
import scrapy


class ShdxSpider(scrapy.Spider):
    name = 'shdx'
    allowed_domains = ['shu.edu.cn']
    start_urls = ['http://shu.edu.cn/']

    def parse(self, response):

