import scrapy
import csv

class A2submodels3powertrainsSpider(scrapy.Spider):
    name = '2submodels3powertrains'
    allowed_domains = ['automobile-catalog.com']

    with open('data/2submodels.csv', "r") as f:
        reader = csv.DictReader(f)
        start_urls = []
        for item in reader:
            start_urls.append("https://www.automobile-catalog.com" + item['Submodel_Link'])

    # start_urls = [
    #     # f"file:F:\GDrive\WorkSpace\Python\ScrapyProject1\ACpages\\3_PowertrainsList\makejaguarxj_xj351xj_xj351_2_r2017.html",
    #     "https://www.automobile-catalog.com/make/jaguar/xk_x100/xk_x100_8_coupe/2005.html"
    # ]

    def parse(self, response):
        Submodel_Name = response.xpath('.//b[contains(., "The following versions and sub-models of")]/text()').get().partition('and sub-models of ')[2].partition(' were available')[0]
        powertrains = response.xpath('//td/ul').xpath('.//font[contains(., "manufactured by")]')
        i = 1
        for powertrain in powertrains:
            if powertrain.xpath('.//li').get().find("manufactured") < 0:
                Powertrain_Name = powertrain.xpath('.//li/b/text()').get().partition(", ")[0]
            else:
                Powertrain_Name = powertrain.xpath('.//li/b/text()').get().partition(",  manufactured or sold in")[0]
            Powertrain_Link = powertrain.xpath('../../table').xpath('.//p/font/b/a/@href').get()
            item2 = {
                "#i": i,
                'Submodel_Name': Submodel_Name,
                'Powertrain_Name': Powertrain_Name,
                'Powertrain_Link': Powertrain_Link
            }
            i += 1
            yield item2
        pass
