# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import requests

page=requests.get('https://www.avito.ma/')
soup=BeautifulSoup(page.content, "html.parser")
categories_parser=soup.find('div' ,{'class' : 'categories'})
categories_parser2=categories_parser.findAll('div' , {'class' : 'bottom'})
categories=[i.h3.text for i in categories_parser2]
link_parser=categories_parser.findAll('a' ,{'class':"categories_homepage"})
links=[i['href'] for i in link_parser]
N_max=[]
for link in links:
    page_categ=requests.get(link)
    soup_informat=BeautifulSoup(page_categ.content , 'html.parser')
    s2=soup_informat.find('div' , {'class':"pagination text-center"})
    try :
        N_max.append(int(s2.findAll('li')[-2].text.strip()))
    except:
        continue
links.pop(-2)
links
urls=[] 
for i in range(len(links)):
    urls=urls+[links[i]+'?o=%d'%d for d in range(1,N_max[i]+1)] 
    

class AvitoSpiderSpider(scrapy.Spider):
    name = 'avito_spider'
    allowed_domains = ['https://www.avito.ma/']
    start_urls = urls

    def parse(self, response):
        nom=response.xpath("//div[@class='ctext3 fs12']/h2[@class='fs14']/a/text()").extract()
        nature_offre= response.xpath("//div[@class='ctext3 fs12']/span[@class='item-info-extra fs14']/small/strong/text()").extract()
        ville= response.xpath("//div[@class='ctext3 fs12']/span[@class='item-info-extra fs14']//a/text()").extract() 
        jour= response.xpath("//div[@class='item-age']//strong/text()").extract() 
        image=response.xpath("//div[@class='item-img']/img/@data-original").extract() 
        url=response.xpath('//h2[@class="fs14"]/a/@href').extract()
    #    categ=['informatique']*N_max[0]+['vehicule']*N_max[1]+['immobilier']*N_max[2]+['pour la maison et le jardin']*N_max[3]+['emploie']*N_max[4]
        data=zip(nom,image,ville,jour,nature_offre,url)
        for item in data :
            res={
                'nom':item[0],
                'image':item[1],
                'ville':item[2],
                'date':item[3],
                'nature d\'annonce':item[4],
                'url':item[5],
            }
            yield res
