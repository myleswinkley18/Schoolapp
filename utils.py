
def Segment(object):
	def __init__(self):
		self.includes = []
		self.locations = []
	def includes_append(self, connections):
		self.includes.append(connections)

def Map(object):
	def __init__(self, invalids, xdimen, ydimen):
		self.invalids = invalids
		self.xdimen = xdimen
		self.ydimen = ydimen
		self.corners = []
		self.rooms = []
		self.segments = []
		self.current_corner
		self.current_segment
	def point_scan(self):
		connections = []
		test_point = self.current_point
		for x in xrange(-1, 1):
			for y in xrange(-1 ,1):
				test_point[0] += x
				test_point[1] += y
			if test_point in self.invalids:
				connections.append(test_point)
			test_point = self.current_point
		return connections

	def connections_analyze(connections):
		if len(connections) == 3:
			if abs(connections[1][0] - connections[0][0]) == abs(connections[2][0] - connections[1][0]):
				return True
			else:
				return False
		if len(connections) == 2:
			self.current_segment.includes_append(connections)
			draw()
		else:
			return False
			slope_find()
	def slope_find(self, origin_point, *points):
		for i in xrange(len(points) - 1):
			



	def draw(self):
		new_segment = []
		first_point = self.current_segment.includes[-2]
		second_point = self.current_segment.includes[-1]
		slope = slope_find(first_point, second_point)
		done = False
		while(not done):
			second_point[0] += slope[0]
			second_point[1] += slope[1]
			if second_point in self.invalids:
				done = True
				continue
			new_segment.append(second_point)
		self.current_segment.includes_append(new_segment)
	def 





