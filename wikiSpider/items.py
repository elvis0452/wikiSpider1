# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

#test180402
#test180403
#test180403-2 找python线上库地址

from scrapy import Item, Field
class Article(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
