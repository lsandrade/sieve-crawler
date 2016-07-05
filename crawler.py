

import requests


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
