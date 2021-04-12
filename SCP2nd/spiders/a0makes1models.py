import scrapy
import csv
import w3lib.html

class A0makes1modelsSpider(scrapy.Spider):
    name = '0makes1models'
    allowed_domains = ['automobile-catalog.com']

    # with open('../data/0makes.csv', "r") as f:
    #     reader = csv.DictReader(f)
    #     start_urls = []
    #     for item in reader:
    #         ### OFFLINE
    #         start_urls.append(f"file:F:\GDrive\WorkSpace\Python\ScrapyProject1\ACpages\\1_ModelsList\\" + item['Make_Link'].replace("/", ""))
    #         ### ONLINE
    #         # if item['Available']: start_urls.append(item['Live_Link'])

    start_urls = [
        # f"file:F:\GDrive\WorkSpace\Python\ScrapyProject1\ACpages\\1_ModelsList\Alfa_Romeo_specifications_catalogue.html",
        "https://www.automobile-catalog.com/list-jaguar.html"
        # "https://httpbin.org/ip"
    ]
    # print(start_urls)

    def parse(self, response):
        Make = response.xpath('//b[contains(., "Specifications catalogue of the")]/text()').get().replace("Specifications catalogue of the ","").partition(" cars,")[0]
        models = response.css('table').css('td').css('table').css('td').css('table').css('td').css('table').css('td').css('p').css('a[style*=text-decoration]')
        for model in models:
            modelInfo = model.css('font').css('b').get().split("<br>")
            Model_Name = w3lib.html.remove_tags(modelInfo[0])
            modelProdYears = modelInfo[1].split("-")
            Model_StartYear = modelProdYears[0]
            Model_EndYear = w3lib.html.remove_tags(modelProdYears[1])
            item = {
            'Make': Make,
            'Model_Name': Model_Name,
            'Model_StartYear': Model_StartYear,
            'Model_EndYear': Model_EndYear,
            'Model_Link': model.css('a::attr(href)').get()
            }
            yield item
        pass
