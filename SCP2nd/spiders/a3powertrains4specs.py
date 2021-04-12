import scrapy
import csv

class A3powertrains4specsSpider(scrapy.Spider):
    name = '3powertrains4specs'
    allowed_domains = ['automobile-catalog.com']

    with open('data/3powertrains.csv', "r") as f:
        reader = csv.DictReader(f)
        start_urls = []
        for item in reader:
            start_urls.append("https://www.automobile-catalog.com" + item['Powertrain_Link'])

    # start_urls = [
    #     f"file:F:\GDrive\WorkSpace\Python\ScrapyProject1\ACpages\\4_Specs\car2004220565alfa_romeo_156_1_6_twin_spark_16v_impression_business__base.html",
    #     f"file:F:\GDrive\WorkSpace\Python\ScrapyProject1\ACpages\\4_Specs\car2004220325alfa_romeo_156_2_0_jts_16v_progression_classic__turismo_or_veloce.html",
    #     f"file:F:\GDrive\WorkSpace\Python\ScrapyProject1\ACpages\\4_Specs\car2007222560alfa_romeo_159_1_9_jts_16v_distinctive.html",
    #     f"file:F:\GDrive\WorkSpace\Python\ScrapyProject1\ACpages\\4_Specs\car2007222605alfa_romeo_159_1_9_jtdm_16v_dpf_distinctive_q-tronic.html",
    #     f"file:F:\GDrive\WorkSpace\Python\ScrapyProject1\ACpages\\4_Specs\car20121595195ford_mondeo_5-dr_1_6_tdci_115_ambiente.html",
    #     f"file:F:\GDrive\WorkSpace\Python\ScrapyProject1\ACpages\\4_Specs\car20121595300ford_mondeo_5-dr_2_0_tdci_140_trend_powershift.html",
    #     f"file:F:\GDrive\WorkSpace\Python\ScrapyProject1\ACpages\\4_Specs\car20121595390ford_mondeo_5-dr_2_0_tdci_163_titanium_powershift.html",
    #     f"file:F:\GDrive\WorkSpace\Python\ScrapyProject1\ACpages\\4_Specs\car20121595420ford_mondeo_5-dr_2_2_tdci_200_titanium.html",
    #     f"file:F:\GDrive\WorkSpace\Python\ScrapyProject1\ACpages\\4_Specs\car20101453550citroen_metropolis.html",
    #     f"file:F:\GDrive\WorkSpace\Python\ScrapyProject1\ACpages\\4_Specs\car20212965430bmw_ix3.html",
    #     f"file:F:\GDrive\WorkSpace\Python\ScrapyProject1\ACpages\\4_Specs\car20212971415fiat_500_cabrio.html"
    # ]
    # start_urls = ['https://www.automobile-catalog.com/car/2005/1287215/jaguar_xk8_coupe.html']

    def parse(self, response):
        specssheet = response.xpath('.//table/tr/td/p/font[contains(., "How much horsepower")]')
        # specssheet = response.xpath('.//table/tr/td/p[contains(., "How much horsepower")]')
        # specssheet = response.xpath('.//table/tr/td/table/tr/td/center')
        for specs in specssheet:
            eecSegmentation = specs.xpath('//center/table/tr/td/table/tr/td/table')[1].xpath('.//tr')[1].xpath('.//td/p/font/table/tr')[12].xpath('.//b/text()').get()
            traction = specs.xpath('//center/table/tr/td/table/tr/td/table')[1].xpath('.//tr')[1].xpath('.//td/p/font/table/tr')[17].xpath('.//b/text()').get()
            bodyStyle = specs.xpath('//center/table/tr/td/table/tr/td/table')[1].xpath('.//tr')[1].xpath('.//td/p/font/table/tr')[15].xpath('.//b/text()').get()

            _basicDimensions = specs.xpath("//center/table/tr/td/table/tr/td").xpath(".//b[contains(., ' mm / ')]").xpath("../../../../..")
            length = _basicDimensions.xpath('.//tr[1]/td/p/font/b/text()').get()
            width = _basicDimensions.xpath('.//tr[2]/td/p/font/b/text()').get()
            height = _basicDimensions.xpath('.//tr[3]/td/p/font/b/text()').get()
            wheelbase = _basicDimensions.xpath('.//tr[5]/td/p/font/b/text()').get()
            weight = _basicDimensions.xpath('../../../../../tr[2]/td/p/font/table/tr/td/p/font/b/text()').get()

            _engineSpecs = specs.xpath("//td/p/font/table/tr/td[contains(., 'Engine manufacturer')]")
            engineManufacturer = _engineSpecs.xpath('../../tr[1]/td/p/font/b/text()').get()
            engineType = _engineSpecs.xpath('../../tr[2]/td/p/font/b/text()').get()
            FuelType = _engineSpecs.xpath('../../tr[3]/td/p/font/b/text()').get()
            Fuel_System = _engineSpecs.xpath('../../tr[4]/td/p/font/b/text()').get()
            Charge_System = _engineSpecs.xpath('../../tr[5]/td/p/font/b/text()').get()
            Valves_Per_Cylinder = _engineSpecs.xpath('../../tr[6]/td/p/font/b/text()').get()
            Additional_Features = ", ".join(filter(None,(_engineSpecs.xpath('../../tr[8]/td/p/font/b/text()').get(), _engineSpecs.xpath('../../tr[10]/td/p/font/b/text()').get())))
            Cylinders_Alignment = _engineSpecs.xpath('../../tr[13]/td/p/font/b/text()').get()
            Displacement = _engineSpecs.xpath('../../tr[14]/td/p/font/b/text()').get()
            Horsepower = _engineSpecs.xpath('../../tr[16]/td/p/font/b/text()').get()
            Torque = _engineSpecs.xpath('../../tr[18]/td/p/font/b/text()').get()
            Battery_Capacity = _engineSpecs.xpath('../../tr[30]/td/p/font/b/text()').get()
            Battery_Capacity_Net = _engineSpecs.xpath('../../tr[31]/td/p/font/b/text()').get()

            _trannySpecs = specs.xpath("//center/table/tr/td/table/tr/td").xpath(".//font[contains(., 'Engine manufacturer')]").xpath("../../../../tr[3]")
            Transmission = _trannySpecs.xpath('.//td/p/font/table[1]/tr[1]/td/p/font/b/text()').get()
            Transmission_Type = _trannySpecs.xpath('.//td/p/font/table[1]/tr[2]/td/p/font/b/text()').get()
            Number_Of_Gears = _trannySpecs.xpath('.//td/p/font/table[1]/tr[4]/td/p/font/b/text()').get()

            _factoryClaim = specs.xpath("//center/table/tr/td/table/tr/td")
            Top_Speed = _factoryClaim.xpath(".//table[contains(., 'Top speed:')]/tr[1]/td[2]/p/font/b/text()").get()
            zeroTo100kmh = _factoryClaim.xpath(".//table[contains(., 'Top speed:')]/tr[4]/td[2]/p/font/b/text()").get()
            ECE90_120_city_comb = _factoryClaim.xpath(".//table[contains(., 'ECE 90/120/city')]/tr/td/p/font/b/text()")[0].get()
            EU_NEDC_Australia_ADR82 = _factoryClaim.xpath(".//table[contains(., 'ECE 90/120/city')]/tr/td/p/font/b/text()")[4].get()
            E_Power_Cons_NEDC_comb = _factoryClaim.xpath(".//tr[contains(., 'power consumption NEDC combined:')]/td/p/font/b/text()").get()
            E_Power_Cons_WLTP_comb = _factoryClaim.xpath(".//tr[contains(., 'power consumption WLTP combined:')]/td/p/font/b/text()").get()
            E_Range_NEDC_comb = _factoryClaim.xpath(".//tr[contains(., 'range NEDC combined:')]/td/p/font/b/text()").get()
            E_Range_WLTP_comb = _factoryClaim.xpath(".//tr[contains(., 'range WLTP combined:')]/td/p/font/b/text()").get()
            E_Range_NEDC_city = _factoryClaim.xpath(".//tr[contains(., 'range NEDC city:')]/td/p/font/b/text()").get()
            E_Range_WLTP_city = _factoryClaim.xpath(".//tr[contains(., 'range WLTP city:')]/td/p/font/b/text()").get()
            Simulation_Based_Consumption = _factoryClaim.xpath(".//table[contains(., 'simulation based on the European type of traffic')]").xpath("../table[8]/tr/td/p/font/b/text()").get()

            Submodel_Name = specs.xpath('//p[@id="top"]').xpath(".//font[contains(., 'all versions')]")[3].xpath('.//b/text()').get()
            Powertrain_Name = specs.xpath("//center/table/tr/td/table/tr/td").xpath(".//b[contains(., 'as offered for the')]").xpath('text()').get()

            Related_Models_L = specs.xpath("//td/table/tr/td/p/font/b[contains(., 'Sales markets')]/../../../../../../p/font")
            Related_Models = ", ".join(filter(None,(Related_Models_L.xpath('./p[7]/font/text()').get(), Related_Models_L.xpath('./p[8]/font/text()').get(), Related_Models_L.xpath('./p[9]/font/text()').get(), Related_Models_L.xpath('./p[10]/font/text()').get(), Related_Models_L.xpath('./p[11]/font/text()').get())))
            Markets_Sold = " ".join(filter(None,(Related_Models_L.xpath('./p[2]/font/text()').get(), Related_Models_L.xpath('./p[3]/font/text()').get(), Related_Models_L.xpath('./p[4]/font/text()').get()))).strip()

            _hpTorqueCurve = specs.xpath("//b[contains(., 'Full engine data: horsepower/torque')]")
            Powertrain_Link = _hpTorqueCurve.xpath('../../../../../..').xpath('.//table[3]/tr/td/p/font/b/a/@href').get().replace("/curve/", "/car/")

            item = {
            'Submodel_Name': Submodel_Name,
            'Powertrain_Name': Powertrain_Name,
            'Powertrain_Link': Powertrain_Link,
            'Related_Models': Related_Models,
            'Markets_Sold': Markets_Sold,

            'EEC_segmentation': eecSegmentation,
            'Body_Style': bodyStyle,
            'Traction': traction,

            'Length': length,
            'Width': width,
            'Height': height,
            'Wheelbase': wheelbase,
            'Weight': weight,

            'Engine_Manufacturer': engineManufacturer,
            'Engine_Type': engineType,
            'Fuel_Type': FuelType,
            'Fuel_System': Fuel_System,
            'Charge_System': Charge_System,
            'Valves_Per_Cylinder': Valves_Per_Cylinder,
            'Additional_Features': Additional_Features,
            'Cylinders_Alignment': Cylinders_Alignment,
            'Displacement': Displacement,
            'Horsepower': Horsepower,
            'Torque': Torque,

            'Transmission': Transmission,
            'Transmission_Type': Transmission_Type,
            'Number_Of_Gears': Number_Of_Gears,

            'Top_Speed': Top_Speed,
            '0_100_kmh_(sec)': zeroTo100kmh,
            'ECE90_120_city_comb': ECE90_120_city_comb,
            'EU_NEDC_Australia_ADR82': EU_NEDC_Australia_ADR82,
            'Battery_Capacity': Battery_Capacity,
            'Battery_Capacity_Net': Battery_Capacity_Net,
            'E_Power_Cons_NEDC_comb': E_Power_Cons_NEDC_comb,
            'E_Power_Cons_WLTP_comb': E_Power_Cons_WLTP_comb,
            'E_Range_NEDC_comb': E_Range_NEDC_comb,
            'E_Range_WLTP_comb': E_Range_WLTP_comb,
            'E_Range_NEDC_city': E_Range_NEDC_city,
            'E_Range_WLTP_city': E_Range_WLTP_city,
            'Simulation_Based_Consumption': Simulation_Based_Consumption
            }
            yield item
        pass
