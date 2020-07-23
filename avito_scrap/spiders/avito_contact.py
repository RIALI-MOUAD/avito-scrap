# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import requests
import pandas as pd

data=pd.read_csv("C://Users//mouad//avito_scrap//avito_cat.csv")
urls=list(data['url'])
"""
for ur in urls:
    page=requests.get("https://www.avito.ma/fr/el_jadida/t%C3%A9l%C3%A9phones/Iphone_6_Plus_128g_39986721.htm")
    soupe=BeautifulSoup(page.content, 'html.parser')
    L=soupe.findAll('script')
    l=[i.strip() for i in str(L).split('\n')]
    for i in l:
        if ("phone: \"0" in i)==True:
            break
        
l[l.index(i)][12:22]
"""
class AvitoContactSpider(scrapy.Spider):
    name = 'avito_contact'
    #allowed_domains = ['https://www.avito.ma']
    start_urls = urls

    def parse(self, response):
        name=response.xpath('//strong/text()').extract()[-2].strip()
        district=response.xpath('//span[@itemprop="name"]/text()').extract()[-3].strip()
        ville=response.xpath('//span[@itemprop="name"]/text()').extract()[2].strip()
        description=response.xpath('//meta[@name="description"]/@content').extract_first()
        vues=response.xpath('//span[@style="vertical-align:middle;margin-left: 3px;"]/text()').extract()[-1].strip()
        date_offre=response.xpath('//abbr[@class="date dtstart value"]/@title').extract_first()
        L=response.xpath('//script').extract()
        l=[str(i) for i in L]
        for i in l:
            if ("phone: \"0" in i)==True:
               break
        g=l[l.index(i)].split(',')     
        for j in g :
            if ("phone: \"0" in j)==True:
                break
        
        num=g[g.index(j)][23:33]
        res={
            'nom':name,
            'ville':ville,
            'region':district,
            'datte offre':date_offre,
            'description':description,
            'vues':vues,
            'phone number':num,
            }
        yield res
        
        NEXT_PAGE_SELECTOR = '/html/body/div[2]/div[4]/div[1]/div[3]/div[1]/ul/li[3]/a/@href'
        next_page = response.xpath(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
            response.urljoin(next_page),
            callback=self.parse)
            