from data import Map
from data import Current_Point
from data import Segment
from data import corner
import numpy
invalids = [[0,0],[0,1],[0,2], [0,3], [0, 4], [0, 5],
 [1, 0], [1,5], 
 [2, 5], 
 [3, 5], 
 [4, 0], [4, 5], 
 [5,0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], 
 [6, 3], [6, 5], 
 [7, 3], [7, 5], 
 [8, 3], [8, 5], 
 [9, 3], [9, 5], 
 [10, 3], [10, 4], [10, 5]]
map1 = Map(invalids, 10, 5)
map1.master_creation()




def overall_room_creation():
	rooms = []
	for i in map1.corners:
		for u in i.markers:
			leg_one = Leg(i, u[0], u[1])
			leg_two = Leg(i, u[1], u[0])
			leg_one.other_leg = leg_two
			leg_two.other_leg = leg_one
			done = True
			while(not done):
				if leg_one.startup() and leg_two.startup():
					pass
				else:
					done = False
					continue
			rooms.append(Leg(leg_one.corners, leg_two.corners, leg_one.segments, leg_two.segments))





class Room(object):
	def __init__(self, corners_one, corners_two, segments_one, segments_two):
		self.corners = self.combo_corner(corners_one, corners_two)
		self.segments = self.combo_segment(segments_one, segments_two)
	def combo_corner(self, corners_one, corners_two):
		corners = []
		for i in corners_one:
			corners.append(i)
		for i in corners_two:
			corners.append(i)
		corners.remove(corners_two[0])
		if corners_one[-1] == corners_two[-1]:
			corners.remove(cornes_one[-1])
		return corners

	def combo_segment(self, segments_one, segments_two):
		segments =[]
		for i in segments_one:
			segments.append(i)
		for i in segments_two:
			segments.append(i)
		segments.remove(segments_two[0])
		if segments_one[-1] == segments_two[-1]:
			segments.remove(segments_one[-1])
		return segments





class Leg(object):
	def __init__(self, corner, segment, other_segment):
		self.corners = [corner]
		self.segments = [segment]
		self.other_leg = None
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
		possibles = self.ccw_scan(self.corners[-1])
		if len(possibles) == 0:
			return False
		self.last_slope = (self.corners[-2].point, self.corners[-1].point)
		for i in possibles:
			if self.slope_value(self.slope(self.corners[-1].point, i.point)):
				new_seg = self.corners[-1].segment_connections[self.corners[-1].corner_connections.index(i)]
				break
		if new_seg in locals():
			if self.boundary_check() and (self.corners[-1] != self.other_leg.corners[-1]):
				self.segments.append(new_seg)
				self.corners.append(self.corners[-1].corner_connections[self.corners[-1].segment_connections.index(new_seg)])
			else:
				return False
			if [self.segments[-2], self.segments[-1]] in self.corners[-1].markers:
				self.corners[-1].markers.remove([self.segments[-2], self.segments[-1]])
			elif [self.segments[-1], self.segments[-2]] in self.corners[-1].markers:
				self.corners[-1].markers.remove([self.segments[-2], self.segments[-1]])
		else:
			return False
		return True

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





