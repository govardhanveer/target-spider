#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Author: Govardhan Veer
date: 09 May 2021
"""
import scrapy
import json
import re
from bs4 import BeautifulSoup as bs
from scrapy_selenium import SeleniumRequest

class TargetspiderSpider(scrapy.Spider):
    name = 'targetspider'

    def __init__(self, url=None, **kwargs):
        super( TargetspiderSpider, self).__init__(url=url, **kwargs)
        self.start_urls = [f'{self.url}']       # Accepting URL as argument
        self.declare_xpath()
    
    def declare_xpath(self):
        """ Defining all xpath required for extraction """
        self.titleXpath = '//*[@id="viewport"]/div[4]/div/div[1]/div[2]/h1/span/text()'
        self.jsonXpath = '//script[@type="application/ld+json"]//text()'
        self.priceXpath = '//*[@id="viewport"]/div[4]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/text()'
        self.specsXpath = '//*[@id="specAndDescript"]/div[1]/div[1]'

    def start_requests(self):
        """Making requests using the scrapy_selenium"""
        try:
            yield SeleniumRequest(
                url = self.url,
                wait_time = 3,
                callback = self.parse_product_details, 
                dont_filter = True    
            )
            self.driver.close()
        except Exception as e :
            print("Error at start_requests(self) = ", e)
            pass
        
    def parse_product_details(self,response):
        """ Extraction of Product Details """
        try:
            #Extract the product price
            og_price = response.xpath('//div[@data-test="product-price"]//text()').extract_first()
            price_result = re.search(r'([0-9\.]+)', og_price )  #extract only digits from a proce string
            price = price_result.group(0) if price_result else ""
            #Extract title of a product
            title = response.xpath(self.titleXpath).extract_first()
            #Extract the 'application/ld+json' to get the currency mainly
            json_data = json.loads( response.xpath( self.jsonXpath ).extract_first())
            data = {}
            if json_data and isinstance(json_data, dict):
                data['tcin'] = str( json_data['@graph'][0]['sku'] ).strip()
                data['upc'] =  json_data['@graph'][0]['gtin13']
                data['price'] = response.xpath( self.priceXpath ).extract_first()
                data['currency'] =  json_data['@graph'][0]['offers']['priceCurrency']
                data['description'] = str( json_data['@graph'][0]['description'] ).strip()
            #Extract the product specifications
            specs_dict = {}
            specification_div = response.selector.xpath( self.specsXpath ).extract_first()
            #Convert text to BeautifulSoup
            soup = bs( specification_div , "lxml" )            
            all_div = soup.find_all('div')
            #Applying ignore case : as these keys isnt mentioned in test
            ignore_keys = ['TCIN','UPC','Item Number (DPCI)','Origin','Size']
            for div in all_div:
                b = div.find_all('b')
                if b:
                    key = b[0].text
                    value = div.text
                    value = re.sub(key, ' ', value)
                    key = re.sub(r'\:', ' ', key)
                    if key not in specs_dict.keys():
                        if key.strip() not in ignore_keys:
                            specs_dict[key.strip()] = value.strip()
            yield {
                "url" : response.request.url,
                "tcin" : data['tcin'],
                "upc" : data["upc"],
                "og_price" : og_price,
                "price" : price,
                "currency" : data['currency'],
                "title" : title,
                "description" : data['description'],
                "specs" : specs_dict
            }
        except Exception as e:
            print("Error at parse_product_details(self,response) = ", e)
            pass
