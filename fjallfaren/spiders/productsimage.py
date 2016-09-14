from fjallfaren.items import FjallfarenItem
import datetime
import scrapy
import urllib

from fjallfaren.excel.fjallfarenex import fjallfarenex
# from scrapy_splash import SplashRequest

import time

class ProductImage(scrapy.Spider):
	name = 'fjallfaren-product-image'
	start_urls = []
	base_url = 'http://www.fjallraven.com/'

	def __init__(self):
		self.fjallfarenex = fjallfarenex()
		self.getUrls()

	def getUrls(self):
		datas = self.fjallfarenex.getExcelData()
		for data in datas:
			search = {'limit': 'all','q': data['TYPE']}
			self.start_urls.append(self.base_url + 'search/?' + urllib.urlencode(search))

	def parse(self, response):
		for item in response.css('.item'):
			ahref = item.css('a')
			# yield SplashRequest(ahref.xpath("@href").extract_first(), self.parse_detail, args={'wait': 0.5})
   			yield scrapy.Request(ahref.xpath("@href").extract_first(), self.parse_detail)

	def parse_detail(self, response):
		time.sleep(5)
		# print(response.css('.more-views ul li'))
		for li in response.css('.more-views ul li'):
			img = li.css('a img')
			zoomurl = img.xpath("@data-zoom").extract_first()
			yield FjallfarenItem(title='title', pubDate='2016-02-21', file_urls=[zoomurl])


