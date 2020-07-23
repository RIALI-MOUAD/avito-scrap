# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import requests

page_categ=requests.get("https://www.avito.ma/fr/maroc/pour_la_maision_et_jardin-%C3%A0_vendre")
soup_informat=BeautifulSoup(page_categ.content , 'html.parser')
s2=soup_informat.find('div' , {'class':"pagination text-center"})
N_max=(int(s2.findAll('li')[-2].text.strip()))


class AvitoCategSpider(scrapy.Spider):
    name = 'avito_categ'
    allowed_domains = ['https://www.avito.ma']
    start_urls = ["https://www.avito.ma/fr/maroc/pour_la_maision_et_jardin-"+"%"+"C3"+"%"+"A0_vendre?sp=1&o=%d"%i for i in range(1,N_max+1)]

    def parse(self, response):
        print(response.url)
        nom=response.xpath("//div[@class='ctext3 fs12']/h2[@class='fs14']/a/text()").extract()
        nature_offre= response.xpath("//div[@class='ctext3 fs12']/span[@class='item-info-extra fs14']/small/strong/text()").extract()
        jour= response.xpath("//div[@class='item-age']//strong/text()").extract() 
        image=response.xpath("//div[@class='item-img']/img/@data-original").extract() 
        prix=response.xpath("//div[@class='item-price']//span[@class='price_value']/text()").extract()
        ville= response.xpath("//div[@class='ctext3 fs12']/span[@class='item-info-extra fs14']//a/text()").extract() 
        data=zip(nom,image,ville,jour,nature_offre,prix)
        for item in data :
            res={
                'nom':item[0],
                'image':item[1],
                'ville':item[2],
                'date':item[3],
                'nature d\'annonce':item[4],
                'prix':item[5],
            }
            yield res        
