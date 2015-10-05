
from node import node

class graph(object):
	
	def __init__ (self, number):
		self.graphType = number
		self.totalNodes = []
	def createNodes(self):
		arrX = [2, 2, 2, 2, 1, 2, 3, 4, 1, 2, 3, 4]
		arrY = [1, 2, 5, 3, 5, 5, 5, 5, 7, 7, 7, 7]
		for i in range(0, len(arrX)):
			tempNode = node(arrX[i], arrY[i])
			
			self.totalNodes.append(tempNode)
		self.createConnections()
	def createConnections(self):
		connectionList = [
		[1, 3],
		[0, 2],
		[1, 7],
		[0, 5],
		[5, 8],
		[6, 9, 3, 4],
		[5, 10, 7],
		[11, 6, 2],
		[4, 9],
		[8, 5, 10],
		[9, 6, 11],
		[7, 10],
		]
		for i in range(0, len(self.totalNodes)):
			tempNode = self.totalNodes[i]
			tempConnections = []
			for number in connectionList[i]:
				tempConnections.append(self.totalNodes[number])
			tempNode.connectedNodes = tempConnections
		return self.totalNodes