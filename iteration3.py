
def Segment(object):
	def __init__(self, *corner_point):
		self.includes = corner_point
		self.locations = []
		self.corners = []
	def includes_append(self, connections):
		for i in xrange(len(connections) - 1):
			self.includes.append(connections[i])
	def corners_append(self):
		self.corners.append(self.includes[0], self.includes[1])
def Corner(object):
	def __init__(self, point, point_connections):
		self.point = point
		self.point_connections = point_connections
		self.point_slopes = []
		self.segment_connections = []
		self.corner_connections = []
	def slopes_append(self, slopes):
		for i in xrange(len(slopes) - 1):
			self.point_slopes.append(slopes[i])

	def segment_connections_append(self, segment):
		self.segment_connections.append(segment)

	def corner_connections_append(self, corner):
		self.corner_connections.append(corner)

		



def Map(object):
	def __init__(self, invalids, xdimen, ydimen):
		self.invalids = invalids
		self.scanned_list = 0
		self.xdimen = xdimen
		self.ydimen = ydimen
		self.corners = []
		self.corner_points = []
		self.rooms = []
		self.segments = []
		self.corner_iterator = 0
		self.current_segment
		self.current_corner
	def master_creation(self):
		self.current_corner = Corner(self.invalids[0], point_scan(self.invalids[0]))
		self.corners.append(self.current_corner)
		while(self.corners[-1] != self.current_corner):
			for i in xrange(len(self.current_corner.point_connections) - len(self.current_corner.segment_connections)):
				segment_draw(i)
			self.corner_iterator += 1
			self.current_corner = self.corners[self.corner_iterator]
	


	
	def segment_draw(self, iterator_counter):
		self.segments.append(self.current_corner.point, self.current_corner.point_connections[-iterator_counter])
		self.current_segment = self.segments[-1]
		done = False
		draw_point = self.current_segment.points[-1]
		slope = self.current_corner.point_slopes
		while(not done):
			draw_point[0] += slope[0]
			draw_point[1] += slope[1]
			if draw_point in self.invalids:
				if connections_analyze(point_scan(draw_point)):
					self.current_segment.includes_append(draw_point)
				else:
					done = True
					continue
			else:
				done = True
				continue
		self.corners.append(Corner(self.current_segment.includes[-1], point_scan(self.current_segment.includes[-1])))
		self.current_corner.corner_connections_append(self.corners[-1])
		self.current_corner.segment_connections_append(self.current_segment)
		self.corners[-1].segment_connections_append(self.current_segment)
		self.corners[-1].corner_connections_append(self.current_corner)

	def point_scan(self):
		connections = []
		test_point = self.current_point
		for x in xrange(-1, 1):
			for y in xrange(-1 ,1):
				test_point[0] += x
				test_point[1] += y
			if test_point in self.invalids:
				connections.append(test_point)
				self.scanned_list += 1
			test_point = self.current_point
		return connections

	def connections_analyze(self, connections):
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
	def slope_find(self, origin_point, *points):
		master_slope = []
		for i in xrange(len(points)):
			slope = []
			slope[0] = points[i][0] - origin_point[0]
			slope[1] = points[i][1] - origin_point[1]
			master_slope.append(slope)
		if len(points) == 1:
			return slope
		else:
			 return master_slope


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
		self.current_segment.points.append(midpoint(new_segment[0], new_segment[-1]))

	def midpoint(self, first_point, second_point):
		midpoint = []
		midpoint[0] = (first_point[0] + second_point[0]) / 2
		midpoint[1] = (first_point[1] + second_point[1]) / 2
		return midpoint





