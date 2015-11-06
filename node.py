from collections import OrderedDict
class node(object):
	#relatedNode = []
	def __init__(self, x, y, name):
		self.x = x
		self.y = y
		self.coor = [x, y]
		self.connectedNodes = {}
		self.nodeNumber = name 


