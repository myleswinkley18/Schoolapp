from node import node
from collections import OrderedDict
class graph(object):
	
	def __init__ (self, number):
		self.graphType = number
		self.totalNodes = []
		self.allNodeNames = {}
	def createNodes(self):
		#create points
		arrX = [2, 4, 2, 4, 2, 3, 2, 3, 4]
		arrY = [2, 2, 4, 4, 5, 5, 6, 6, 6]
		
		for i in range(0, len(arrX)):
			tempNode = node(arrX[i], arrY[i], i)
			
			self.totalNodes.append(tempNode)
			self.allNodeNames[tempNode.nodeNumber] = tempNode

		#create connection
		connectionList = [
		[1, 2],
		[0, 3],
		[0, 4],
		[1, 8],
		[2, 5, 6],
		[4, 7],
		[4, 7],
		[6, 5, 8],
		[7, 3],
		]
		for i in range(0, len(self.totalNodes)):
			tempNode = self.totalNodes[i]
			tempConnections = {}
			for number in connectionList[i]:
				tempConnections[self.totalNodes[number].nodeNumber] = 0
			tempNode.connectedNodes = tempConnections
		

		#create distances
		
		for n in range(0, len(self.totalNodes)-1):
			for connectedNode in self.allNodeNames[n].connectedNodes:
				#import pdb; pdb.set_trace()
				tempDistance = distanceBetween(self.allNodeNames[n], self.allNodeNames[connectedNode])
				self.allNodeNames[n].connectedNodes[connectedNode] = tempDistance
				

def distanceBetween(node1, node2):
	x1 = node1.x
	y1 = node1.y
	x2 = node2.x
	y2 = node2.y

	distance = (((x1 - x2)**2) + ((y1 - y2)**2))**0.5
	return distance