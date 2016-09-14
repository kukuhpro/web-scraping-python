from excel import excel
import os.path

class fjallfarenexcel(excel):
	rows = ''
	heading = []
	values = []
	BASE_DIR = os.path.dirname(os.path.dirname(__file__))

	def __init__(self):
		self.filename = self.BASE_DIR + '/excel/files/STOCK_OPNAME_SAGARMATHA_GEAR_OK.xlsx'
		self.read_only = True
		self.setup()
		self.processData()

	def setup(self):
		self.setWorkBook()
		self.setWorkSheet('Sheet1')

	def processHeadTitle(self):
		x = 0
		for row in self.rows:
			y = 0
			for cell in row:
				if not cell.value == None:
					self.heading.append(cell.value)
				y = y + 1
			if x < 2 and len(self.heading) > 0:
				break
			x = x + 1

	def processValue(self):
		x = 0
		for row in self.rows:
			y = 0
			dictc = {}
			for cell in row:
				if not cell.value == None and not cell.value in self.heading:
					dictc[self.heading[y]] = cell.value
					y = y + 1
			if dictc:
				self.values.append(dictc)
			x = x + 1

	def processData(self):
		self.rows = self.getRows()
		self.processHeadTitle()
		self.processValue()

	def getRealData(self):
		return self.values



