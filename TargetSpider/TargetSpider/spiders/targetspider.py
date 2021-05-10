import scrapy
import json
import re
from bs4 import BeautifulSoup as bs

class TargetspiderSpider(scrapy.Spider):
    name = 'targetspider'
    allowed_domains = ['https://www.target.com/']
    # start_urls = ['https://www.target.com/p/toddler-girls-shanel-fisherman-sandals-cat-jack/-/A-81204099?preselect=80859208']
    
    def __init__(self, url=None, **kwargs):
        super( TargetspiderSpider, self).__init__(url=url, **kwargs)
        self.start_urls = [f'{self.url}']
        self.declare_xpath()
    
    def declare_xpath(self):
        self.titleXpath = '//*[@id="viewport"]/div[4]/div/div[1]/div[2]/h1/span/text()'
        self.jsonXpath = '//script[@type="application/ld+json"]//text()'
        self.priceXpath = '//*[@id="viewport"]/div[4]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/text()'
        self.specsXpath = '//*[@id="specAndDescript"]/div[1]/div[1]'

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)

        data = {}
        data['url'] = response.request.url
        data['response_url'] = response.url
        # data['html'] = response.body_as_unicode()
        data['title'] = response.xpath( self.titleXpath ).extract_first()
        
        json_data = json.loads( response.xpath( self.jsonXpath ).extract_first())

        if json_data and isinstance(json_data, dict):
            data['tcin'] = str( json_data['@graph'][0]['sku'] ).strip()
            data['upc'] =  json_data['@graph'][0]['gtin13']
            data['price'] = response.xpath( self.priceXpath ).extract_first()
            data['currency'] =  json_data['@graph'][0]['offers']['priceCurrency']
            data['description'] = str( json_data['@graph'][0]['description'] ).strip()
            
            specification_div = response.xpath( self.specsXpath ).extract_first()

            soup = bs( specification_div )
            
            all_div = soup.find_all('div')
            data_dict = {}
            ignore_keys = ['TCIN','UPC','Item Number (DPCI)','Origin','Size']
            for div in all_div:
                b = div.find_all('b')
                if b:
                    key = b[0].text
                    value = div.text
                    value = re.sub(key, ' ', value)
                    key = re.sub(r'\:', ' ', key)
                    if key not in data_dict.keys():
                        if key not in ignore_keys:
                            data_dict[key.strip()] = value.strip()

            #print(data_dict)
            data['specs'] = data_dict
        else:
            print("Xpath for json data isnt worked ... \n")
        yield data
