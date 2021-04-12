import scrapy


class A3powertrains4specsSpider(scrapy.Spider):
    name = '3powertrains4specs'
    allowed_domains = ['automobile-catalog.com']
    start_urls = ['http://automobile-catalog.com/']

    def parse(self, response):
        pass
