import unittest

from crawler import Crawler


class CrawlerTest(unittest.TestCase):

	# out crawler to be tested
	crawler = Crawler()

	# test if crawler was created
	def testCrawler(self):
		self.assertIsInstance(self.crawler,Crawler,"Not a Crawler.")

	# test if URL is OK
	def testUrl(self):
		url = "http://www.epocacosmeticos.com.br"
		self.crawler.setUrl(url)
		self.assertEqual(self.crawler.getUrl(),url, "Wrong URL.")


if __name__ == '__main__':
    unittest.main()