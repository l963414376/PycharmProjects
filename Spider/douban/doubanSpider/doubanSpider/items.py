# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanspiderItem(scrapy.Item):
    title = scrapy.Field()

    # 电影信息

    bd = scrapy.Field()

    # 豆瓣评分

    star = scrapy.Field()

    # 脍炙人口的一句话

    quote = scrapy.Field()
