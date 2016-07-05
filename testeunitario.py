import unittest
import requests

from crawler import Crawler


class CrawlerTest(unittest.TestCase):

	# our crawler to be tested
	crawler = Crawler()
	url = "http://www.epocacosmeticos.com.br"

	# test if crawler was created
	def testCrawler(self):
		self.assertIsInstance(self.crawler,Crawler,"Not a Crawler.")
		

	# test if URL is OK
	def testUrl(self):
		self.crawler.setUrl(self.url)
		index = self.crawler.keepUrl(self.url)

		self.assertEqual(self.crawler.getUrl(),self.url, "Wrong URL.")
		self.assertNotEqual(self.crawler.getUrl(), "http://www.google.com", "It's weird!")
		self.assertEqual(requests.get(self.url).status_code,200, "URL can't be accessed.")
		self.assertEqual(self.crawler.getUrlsVisitedByIndex(index),self.url,"Url visited is not the Url saved.")

	# Test if our crawler can keep an array of URLs visited
	def testArrayofUrls(self):
		urls = ["http://www.google.com/2","http://www.facebook.com"]
		
		self.crawler.keepUrl(urls[0])
		self.crawler.keepUrl(urls[1])
		
		self.assertEqual(self.crawler.getUrlsVisited(),urls,"Array of URLs is wrong.")
		self.assertEqual(self.crawler.getUrlsVisitedByIndex(1),urls[1],"URL saved is wrong")

	# Verify if the URL is valid
	def testValidUrl(self):
		url1 = "http://www.google.com/1"
		url2 = "#"
		url3 = "http://www.epocacosmeticos.com.br/inner-restore-intensif-senscience-mascara-reconstrutora/p"

		self.assertFalse(self.crawler.isValidUrl(url1), "Not a valid URL.")
		self.assertFalse(self.crawler.isValidUrl(url2), "Not a valid URL.")
		self.assertFalse(self.crawler.isValidUrl(self.url), "Not a valid URL.")
		self.assertTrue(self.crawler.isValidUrl(url3), "Not a valid URL.")
	
	# Check if a page is Product page or Normal page
	def testUrlProduct(self):
		url3 = "http://www.epocacosmeticos.com.br/inner-restore-intensif-senscience-mascara-reconstrutora/p"
		
		self.assertTrue(self.crawler.isProduct(url3),"I'ts not a product.")
		self.assertFalse(self.crawler.isProduct(self.url),"I'ts not a product.")
		self.assertFalse(self.crawler.isProduct("http://www.epocacosmeticos.com.br/cabelos"),"I'ts not a product.")

	# Get all links from page visited
	def testGetAllLinks(self):
		simple_page = "http://mussumipsum.com/"

		self.assertEqual(len(self.crawler.getAllLinks(simple_page)),7,"List of links muts contain 7 links.")


	# create CSV to store data
	def testCreateCsvFile(self):
		title = "file.csv"

		self.crawler.createCsv(title)
		
		self.assertEqual(self.crawler.getCsvTitle(),title,"Csv doesn't exists")

	# get product data from URL
	def testProductData(self):
		url3 = "http://www.epocacosmeticos.com.br/inner-restore-intensif-senscience-mascara-reconstrutora/p"
		url4 = "http://www.epocacosmeticos.com.br/vip-old-spice-perfume-para-o-corpo/p"

		#product available
		product = self.crawler.getProduct(url3)

		self.assertEqual(product['name'],"Inner Restore Intensif Senscience - Máscara Reconstrutora","Name wrong")
		self.assertEqual(product['ref'],"0074469445320","Ref wrong")
		self.assertEqual(product['price'],"R$ 62,40","Price wrong")
		#self.assertEqual(product['description'],"","Name wrong")
		self.assertEqual(product['availability'],"Yes","Availability wrong")

		#product unavailable
		product = self.crawler.getProduct(url4)
		self.assertEqual(product['price'],"*","Price wrong")
		self.assertEqual(product['availability'],"No","Availability wrong")


	# Verify if a product was saved in the store data
	def testStoreProduct(self):
		url3 = "http://www.epocacosmeticos.com.br/inner-restore-intensif-senscience-mascara-reconstrutora/p"
		
		product = self.crawler.getProduct(url3)

		self.crawler.storeProduct(product)

		self.assertEqual(self.crawler.getStoredProductByIndex(0)[0],product['ref'],"Product not sotred.")


	# Test time of execution with multithread

if __name__ == '__main__':
    unittest.main()