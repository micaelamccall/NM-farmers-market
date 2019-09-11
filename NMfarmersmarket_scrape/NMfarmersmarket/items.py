# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class nmFarmItem(scrapy.Item):
    name = scrapy.Field()
    address = scrapy.Field()
    schedule = scrapy.Field()
    manager = scrapy.Field()
    url = scrapy.Field()
    creditDebit = scrapy.Field()
    seniorDiscount = scrapy.Field()
    snap=scrapy.Field()
    pass