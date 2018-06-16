# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose,TakeFirst

class LiveItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
#    title = scrapy.Field(
#        input_processor = MapCompose(lambda x:x.strip()),
#        output_processor = TakeFirst(),
#    )
#    username= scrapy.Field(
#        input_processor = MapCompose(lambda x:x.strip()),
#        output_processor = TakeFirst()
#    )
#    num = scrapy.Field(
#        output_processor = TakeFirst()
#    )
#    pic_addr = scrapy.Field(
#        output_processor = TakeFirst()
#    )
#    addr = scrapy.Field(
#        output_processor = TakeFirst()
#    )
#    platform = scrapy.Field(
#        output_processor = TakeFirst()
#    )
    pass
