from fjallfarenexcel import fjallfarenexcel
from slugify import slugify

class fjallfarenex(object):
	def __init__(self):
		self.base_url = 'http://www.fjallraven.com/'
		self.excel = fjallfarenexcel()

	def getBaseURL(self):
		return self.base_url

	def getSlug(self, text):
		return slugify(text)

	def getExcelData(self):
		return self.excel.getRealData()

