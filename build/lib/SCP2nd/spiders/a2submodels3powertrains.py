import scrapy


class A2submodels3powertrainsSpider(scrapy.Spider):
    name = '2submodels3powertrains'
    allowed_domains = ['automobile-catalog.com']
    start_urls = ['http://automobile-catalog.com/']

    def parse(self, response):
        pass
