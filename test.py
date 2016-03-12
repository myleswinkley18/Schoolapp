class Leg(object):
	def __init__(self, corner, segment, other_segment, other_legs):
		self.corners = [corner]
		self.segments = [segment]
		self.other_leg = other_leg
		self.y_distance = None
		self.x_distance = None
		self.other_segment = other_segment
		self.last_slope = None
		self.direction = None

	def startup(self):
		self.distance_set
		if self.ccw(self.other_segment.includes[0], self.corners[0].point, self.other_data(self.corners[0].point, self.segments[0]).point):
			self.direction = "Counter_Clock"
		else:
			self.direction = "Clock"
		done = True
		while(not done):
			possibles = self.ccw_scan(self.corners[-1])
			if len(possibles) == 0:
				done = True
				continue
			self.last_slope = (self.corners[-2].point, self.corners[-1].point)
			for i in possibles:
				if self.slope_value(self.slope(self.corners[-1].point, i.point)):
					new_seg = self.corners[-1].segment_connections[self.corners[-1].corner_connections.index(i)]
					break
			if new_seg in locals():
				if self.boundary_check()  and self.corners[-1] == self.other_leg.corners[-1]:
					self.segments.append(new_seg)
					self.corners.append(self.corners[-1].corner_connections[self.corners[-1].segment_connections.index(new_seg)])
			else:
				break

	def distance_set(self):
		if self.corners[-1].point[0] > self.other_leg.corners[-1].point[0]:
			self.x_distance = True
		else:
			self.x_distance = False
		if self.corners[-1].point[1] > self.other_leg.corners[-1].point[1]:
			self.y_distance = True
		else:
			self.y_distance = False

	def boundary_check(self):
		if self.corners[-1].point[0] > self.other_leg.corners[-1].point[0]:
			if self.x_distance == True:
				return False
			else:
				return True
		else:
			if self.x_distance == True:
				return True
			else:
				 return False
		if self.corners[-1].point[1] > self.other_leg.corners[-1].point[1]:
			if self.y_distance == True:
				return True
			else:
				return False
		else:
			if self.x_distance == True:
				return False
			else:
				return True
		

	def slope_value(self, test_slope):
		indicator = True
		#incicator is always set to True, if it is not then the function quits because one of the terms has been violated and it is set to false
		#determines if the new slope is the "opposite" of self.last_slope
		if self.last_slope[0] >= 0 and test_slope[0] >= 0:
			pass
		elif self.last_slope[0] <= 0 and test_slope[0] <= 0:
			pass
		else:
			indicator = False
			return indicator
		if self.last_slope[1] >= 0 and test_slope[1] >= 0:
			pass
		elif self.last_slope[1] <= 0 and test_slope[0] <= 0:
			pass
		else:
			indicator = False
			return indicator
		return indicator
			

	def slope(self, first_point, second_point):
		slope = []
		slope.append(second_point[0] - first_point[0])
		slope.append(second_point[1] - first_point[1])
		return slope

	def ccw_scan(self, corner):
		possible = copy.deepcopy(corner.corner_connections)
		for i in possible:
			test = ccw(self.corners[0].point, self.corners[1].point, i.point):
			if self.direction == "Clock" and test:
				possible.remove(i)
			elif self.direction == "Counter_Clock" and not test:
				possible.remove(i)
		return possible



	def other_data(self, data, segment):
		#given data in a 2 length array, it finds the index of the other data point that is not the input
		#returns the other data
		if data == segment.corner_connections[0]:
			return segment.corner_connections[1]
		else:
			return segment.corner_connections[0]
	def ccw(self, A, B, C):
    	return (C[1]-A[1])*(B[0]-A[0]) > (B[1]-A[1])*(C[0]-A[0])
