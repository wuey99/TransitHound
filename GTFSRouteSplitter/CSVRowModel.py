#-----------------------------------------------------------------------------
# CSVRowModel
#-----------------------------------------------------------------------------
class CSVRowModel(object):

	#-----------------------------------------------------------------------------
	def __init__(self, headerNames):
		self._headerNames = headerNames
		self._headerNamesList = headerNames.split(",")
		self._properties = {}

	#-----------------------------------------------------------------------------
	def addColumns(self, row):
		if len(row) != len(self._headerNamesList):
			print "error in csv row"

			return


		for i in xrange(0, len(self._headerNamesList)):
			self._properties[self._headerNamesList[i]] = row[i]

	#-----------------------------------------------------------------------------
	def getProperty(self, name):
		return self._properties[name]

	#-----------------------------------------------------------------------------
	def writeHeader(self, f):
		f.write(self._headerNames + "\n");

	#-----------------------------------------------------------------------------
	def writeRow(self, f):
		for i in xrange(0, len(self._headerNamesList)):
			if i < len(self._headerNamesList) - 1:
				f.write(self.getProperty(self._headerNamesList[i]) + ",")
			else:
				f.write(self.getProperty(self._headerNamesList[i]) + "\n")

