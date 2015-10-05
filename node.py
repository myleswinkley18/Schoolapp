class node(object):
	#relatedNode = []
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.coor = [x, y]
		connectedNodes = []