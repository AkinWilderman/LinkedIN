# -*- coding: utf-8 -*-
import scrapy


class CrawlSpider(scrapy.Spider):
    name = 'crawl'
    allowed_domains = ['linkedin.com/login']
    start_urls = ['http://linkedin.com/login/']

    def parse(self, response):
        pass
