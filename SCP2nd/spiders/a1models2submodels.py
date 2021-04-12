import scrapy


class A1models2submodelsSpider(scrapy.Spider):
    name = '1models2submodels'
    allowed_domains = ['automobile-catalog.com']
    start_urls = ['https://www.automobile-catalog.com/model/jaguar/xk_x100.html']

    def parse(self, response):
        Model_Name = response.xpath('//p[@id="top"]/font/b/text()').get()
        submodels = response.css('table').css('td').css('table').css('td').css('table').css('td').css('table').css('td').css('table').css('tr').css('td').css('table')
        for submodel in submodels:
            Submodel_StartYear = submodel.css('tr').css('td').css('p').css('a').css('font').css('b::text').get()
            howMany = len(submodel.css('tr'))

            if howMany > 2:
                theSubmodel = submodel.css('tr')[howMany-2]
                Submodel_EndYear = submodel.css('tr')[howMany-1].css('td').css('p').css('a').css('font').css('b::text').get()
            elif howMany == 2:
                theSubmodel = submodel.css('tr')[1]
                Submodel_EndYear = submodel.css('tr')[1].css('td').css('p').css('a').css('font').css('b::text').get()
            else:
                theSubmodel = submodel.css('tr')[0]
                Submodel_EndYear = Submodel_StartYear

            Submodel_Name = theSubmodel.css('td').css('p').css('a').css('font').css('b').css('font::text').get()
            Submodel_Link = theSubmodel.css('td').css('p').css('a::attr(href)').get()

            item = {
            'Model_Name': Model_Name,
            'Submodel_Name': Submodel_Name,
            'Submodel_StartYear': Submodel_StartYear,
            'Submodel_EndYear': Submodel_EndYear,
            'Submodel_Link': Submodel_Link
            }
            yield item
        pass
