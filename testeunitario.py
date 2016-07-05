import unittest

from crawler import Crawler


class CrawlerTest(unittest.TestCase):

	crawler = Crawler()

	def testCrawler(self):
		self.assertIsInstance(self.crawler,Crawler,"Not a Crawler.")


if __name__ == '__main__':
    unittest.main()