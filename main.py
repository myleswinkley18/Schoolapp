from node import node, path
from graph import graph
#from test import test
import math
from collections import OrderedDict

graph1 = graph(0)
graph1.createNodes()
#print graph1.totalNodes[0].connectedNodes
#print graph1.totalNodes[0].connectedNodes

def bestPath(startNode, endNode):
	mapGraph = graph(0)
	mapGraph.createNodes()
	previous = {}
	distance = OrderedDict()
	total = []
	print "ok"
	for vertex in mapGraph.allNodeNames:
		#import pdb; pdb.set_trace()
		previous[vertex] = None
		distance[vertex] = 10000
		total.append(vertex)

	#import pdb; pdb.set_trace()
	distance[startNode] = 0	
	hasBeenDeleted = []
	keepGoing = True
	while keepGoing:
		currentNodes = {}
		for canUse in total:
			if canUse not in hasBeenDeleted:
				currentNodes[canUse] = distance[canUse]
		sortedCurrent = sorted(currentNodes.items(), key=lambda x: x[1])[0]
		shortestNode = sortedCurrent[0]
		hasBeenDeleted.append(shortestNode)
		#import pdb; pdb.set_trace()
		if shortestNode == endNode:
			u = endNode
			path = []
			while previous[u] != None:
				path.insert(0, u)
				u = previous[u]
			return path
		for neighbor in mapGraph.allNodeNames[shortestNode].connectedNodes:
			alt = distance[shortestNode] + mapGraph.allNodeNames[shortestNode].connectedNodes[neighbor]
			if alt < distance[neighbor]:
				distance[neighbor] = alt
				previous[neighbor] = shortestNode
		if len(total) == len(hasBeenDeleted):
			keepGoing = False
	print distance
	print previous
navigate = input("Start Navigation? (y/n) :")
startNode = input("Where are you now?: ")
endNode = input("Where would you like to go?: ")
bestPath = bestPath(startNode, endNode)
print bestPath



