from node import node
from graph import graph
import math

graph1 = graph(0)
allNodes = graph1.createNodes()
print graph1.totalNodes[0].connectedNodes

"""
def distanceBetween(self, node1, node2):
	x1 = node1.x
	y1 = node1.y
	x2 = node2.x
	y2 = node2.y

	distance = ((x1 - x2)**2) + ((y1 - y2)**2))**0.5
	return distance

distanceBetween(graph1.totalNodes[0], graph1.totalNodes[1])
"""
