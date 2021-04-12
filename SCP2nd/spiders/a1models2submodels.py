import scrapy


class A1models2submodelsSpider(scrapy.Spider):
    name = '1models2submodels'
    allowed_domains = ['automobile-catalog.com']
    start_urls = ['http://automobile-catalog.com/']

    def parse(self, response):
        pass
