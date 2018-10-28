# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhipinItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    money = scrapy.Field()
    company = scrapy.Field()
    city = scrapy.Field()
    work_year = scrapy.Field()
    education = scrapy.Field()
    company_text = scrapy.Field()
    financing = scrapy.Field()
    detail = scrapy.Field()
