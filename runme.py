
from crawler import Crawler

url = "http://www.epocacosmeticos.com.br"
title = "products.csv"
products = 0

c = Crawler()
c.setUrl(url)
c.createCsv(title)
c.keepUrl(url)


for link in c.getAllLinks(url):
	if c.isValidUrl(link):
		c.keepUrl(link)

print(str(len(c.getUrlsVisited())))


for page in c.getUrlsVisited():
	print("*")

	for link in c.getAllLinks(page):
		if c.isValidUrl(link):
			index = c.keepUrl(link)
			c.getAllLinks(link)
			print(str(len(c.getUrlsVisited()))+" visited - "+c.getUrlsVisitedByIndex(index))
			
			if c.isProduct(link):
				product = c.getProduct(link)
				c.storeProduct(product)
				products += 1

			print (str(products)+" Products.")
