# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LearnScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    articleTitle = scrapy.Field()
    articleLink = scrapy.Field()
    postingDate = scrapy.Field()
    pass
