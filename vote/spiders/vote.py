# -*- coding: utf-8 -*-
import scrapy
from vote.items import VoteItem
from scrapy.contrib.loader import ItemLoader


class voteSpider(scrapy.Spider):
    name = 'vote'

    def start_requests(self):
        start_urls = ['']
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = ItemLoader(item=VoteItem(),response=response)
            

    
