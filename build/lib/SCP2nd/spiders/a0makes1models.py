import scrapy


class A0makes1modelsSpider(scrapy.Spider):
    name = '0makes1models'
    allowed_domains = ['automobile-catalog.com']
    start_urls = ['http://automobile-catalog.com/']

    def parse(self, response):
        pass
