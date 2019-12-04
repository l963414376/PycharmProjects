# -*- coding: utf-8 -*-
import os
import scrapy
import sys

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sys.path.append(path)

from doubanSpider.items import DoubanspiderItem


class DoubanmoiveSpider(scrapy.Spider):
    name = 'doubanmoive'
    allowed_domains = ['movie.douban.com']
    offset = 0
    url = "https://movie.douban.com/top250?start="

    start_urls = (

        url + str(offset),

    )

    def parse(self, response):
        item = DoubanspiderItem()

        movies = response.xpath("//div[@class='info']")

        for each in movies:

            # 电影标题

            item['title'] = each.xpath(".//span[@class='title'][1]/text()").extract()[0]

            # 电影信息

            item['bd'] = each.xpath(".//div[@class='bd']/p/text()").extract()[0]

            # 豆瓣评分

            item['star'] = each.xpath(".//div[@class='star']/span[@class='rating_num']/text()").extract()[0]

            # 脍炙人口的一句话

            quote = each.xpath(".//p[@class='quote']/span/text()").extract()

            if len(quote) != 0:
                item['quote'] = quote[0]

            yield item

        if self.offset < 225:
            self.offset += 25

            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

        def parse(self, response):
            pass
