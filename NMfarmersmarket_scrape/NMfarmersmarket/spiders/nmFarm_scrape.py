import scrapy
from NMfarmersmarket.items import nmFarmItem
from datetime import datetime
import re

class nmFarm(scrapy.Spider):
    name = "nmFarm_scraper"

    #start URL
    start_urls = ["http://farmersmarketsnm.org/find-a-market/"]

    npages = 1

    def parse(self, response):
        for href in response.xpath("//h3/a//@href"):
            url = href.extract()
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self,response):
        item = nmFarmItem()

        #Getting name of farmer's market
        item['name'] = response.xpath("//div[contains (@class, 'row')]/h1/text()").extract()

        #Getting address
        address_list =  response.xpath("//div[contains(@class, 'wpsl-location-address')]/span/text()").extract()
        address_list = [x.strip() for x in address_list]
        item['address'] = ", ".join(address_list).strip()

        #Getting Schedule
        item['schedule'] = response.xpath("//div[contains(@class, 'market_location')]/text()").extract()[5].strip()

        #Getting Manager
        item['manager'] = response.xpath("//div[contains(@class, 'market_location')]/text()").extract()[3].strip()

        #URL
        item['url'] = response.xpath("//meta[@property='og:url']/@content").extract()

        #Get credit-debit info
        credit_response = response.xpath("//span[contains(@class, 'dufb')]/text()").extract()
        if len(credit_response)>1:
            credit_response = credit_response[1]
        else:
            credit_response = []
        
        if len(credit_response)>0:
            item['creditDebit'] = "Yes"
        else:
             item['creditDebit'] = "No"

        #Get senior discount info
        senior_response = response.xpath("//span[contains(@class, 'wic-fmnp')]/text()").extract()

        if len(senior_response)>0:
            item['seniorDiscount'] = "Yes"
        else:
            item['seniorDiscount'] = "No"

        #Get SNAP info
        snap_response = response.xpath("//span[contains(@class, 'snap-ebt')]/text()").extract()

        if len(snap_response)>0:
            item['snap'] = "Yes"
        else:
            item['snap'] = "No"
            
        yield item
#scrapy crawl nmFarm_scraper -o NMfarmersmarket.csv
        