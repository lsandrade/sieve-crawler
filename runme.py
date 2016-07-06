
from crawler import Crawler
from math import sqrt
import concurrent.futures

# URL
url = "http://www.epocacosmeticos.com.br"
# files' title
title = "products.csv"
# How many products did we store?
products = 0

# 1 - create crawler
c = Crawler()
# 2 - set base url
c.setUrl(url)
# 3 - Create csv file
c.createCsv(title)
# 4 - keep base url in visited urls
c.keepUrl(url)

# 5 - start getting all links on base url
for link in c.getAllLinks(url):
	if c.isValidUrl(link):
		c.keepUrl(link)

# print test
#print(str(len(c.getUrlsVisited())))
print("Runing...\n")

# How many pages did we visit?
i = 0

# 8 - Get all links from a page
def start(link):
	global products
	global i
	
	if c.isValidUrl(link):
		i+=1
		c.keepUrl(link)
		c.getAllLinks(link)
		#print(str(i)+" pages visited. URL: "+link)
			
		if c.isProduct(link):
			product = c.getProduct(link)
			c.storeProduct(product)
			products += 1

		#print (str(products)+" Products stored.\n")

# 7 - For all pages visited, start collecting all links
def visited (page):
	with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
		{pool.submit(start, link): link for link in c.getAllLinks(page)}

# 6 - Visit all pages in URLs saved
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
	{pool.submit(visited, page): page for page in c.getUrlsVisited()}

print("Finished.")