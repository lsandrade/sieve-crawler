# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import csv
import urllib.request
import sys

class Crawler():

    urls = []

    # set main URL
    def setUrl(self,url):
        self.url = url

    # get main URL
    def getUrl(self):
        return self.url

    # save URL visited in an array
    # return index of array
    def keepUrl(self,url):
        self.urls.append(url)
        return len(self.urls)-1

    # return array of visited URLs
    def getUrlsVisited(self):
        return self.urls

    # get an URL visited from array according an index
    def getUrlsVisitedByIndex(self,i):
        return self.urls[i]

    # verify if is a valid URL.
    # criteria: starts with the main URL and it was not visited preveously
    def isValidUrl(self,url):
        if url[:33]==self.url and url not in self.urls:
            return True
        else:
            return False

    # verify if an URL contais a Product.
    # In this domain, product's URL ends with "/p"
    def isProduct(self,url):
        if url[-2:]=="/p":
            return True
        else:
            return False

    # Getting all links from a page
    def getAllLinks(self,url):
        links = []
        r = requests.get(url)
        soup = BeautifulSoup(r.text,"html.parser")
        for a in soup.findAll('a',href=True):
            links.append(a['href'])
        return links

    # creating objects to read and write csv file
    def createCsv(self,title):
        writer = open(title, 'w',encoding='utf-8')
        self.title = title

        writer.write('ref,name,price,availability,description,url\n')
        writer.close()

        
    # getting csv title
    def getCsvTitle(self):
        return self.title

    # getting product data from URL
    def getProduct(self,url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text,"html.parser")
        ref = soup.find('label',class_='sku-ean-code').string
        name = soup.find('div',class_='productName').string
        try:
            price = soup.find('strong',class_='skuBestPrice').string
            availability = "Yes"
        except AttributeError:
            price = "*"
            availability = "No"
        description = soup.find('div',class_='productDescription').text
        
        product = {'ref':ref, 'name':name, 'price':price, 'availability':availability, 'description': description, 'url':url}
        
        return product

    #store product in CSV File
    def storeProduct(self,product):
        writer = open(self.title, 'a', encoding='utf-8')
        writer.write(product['ref']+","+product['name']+","+product['price']+","+product['availability']+","+product['description']+","+product['url']+"\n")
        writer.close()


    def getStoredProductByIndex(self,i):
        reader = open(self.title,'r',encoding='utf-8')
        lines = reader.read().splitlines()
        reader.close()
        return lines[i+1].split(',')