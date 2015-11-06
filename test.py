from node import node
#newNode = node(3, 4)
#print newNode

class testClass(object):
	def __init__(self, x, y):
		myNode = node(x, y)

thing = testClass(5, 6)
print thing.myNode