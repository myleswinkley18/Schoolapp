import sys
import copy
import math
class Current_Point(object):
	def __init__(self, point):
		self.point = point
	def __copy__(self):
		return Current_Point(self.point)

class Segment(object):
	def __init__(self, corner_point, second_point, corner):
		self.includes = [corner_point, second_point]
		self.locations = []
		self.corners = [corner]
	def corners_append(self):
		self.corners.append(self.includes[0], self.includes[1])
class Corner(object):
	def __init__(self, point, point_connections):
		self.point = point
		self.point_connections = point_connections
		self.point_slopes = []
		self.segment_connections = []
		self.corner_connections = []
		self.markers = []
	def slopes_append(self, slopes):
		for i in xrange(len(slopes) - 1):
			self.point_slopes.append(slopes[i])
	def segment_connections_append(self, segment):
		self.segment_connections.append(segment)
	def point_connections_remove(self, point):
		self.point_connections.remove(point)
	def corner_connections_append(self, corner):
		self.corner_connections.append(corner)
class Map(object):
	def __init__ (self, invalids, xdimen, ydimen):
		self.invalids = invalids
		self.scanned_list = []
		self.xdimen = xdimen
		self.ydimen = ydimen
		self.corners = []
		self.corner_points = []
		self.rooms = []
		self.segments = []
		self.corner_iterator = 0
		self.current_segment = None
		self.current_corner = None
		self.current_point = None
		self.current_slope = None

	def data_sort(self, current_data, data_list):
		if current_data == data_list[0]:
			return data_list[0]
		else:
			return data_list[1]

	def master_creation(self):
		self.current_point = copy.deepcopy(Current_Point(self.invalids[0]))
		self.current_corner = copy.deepcopy(Corner(self.invalids[0], self.point_scan(self.current_point.point)))
		self.current_corner.point_slopes = self.slope_find(self.current_corner.point_connections)
		self.open_space_add(self.current_corner)
		self.corners.append(self.current_corner)
		done = False
		while(not done):
			for i in xrange(len(self.current_corner.point_connections)):
				if self.current_corner.segment_connections[i] == None:
					self.segment_draw(i)
			self.corner_iterator += 1
			try:
				self.current_corner = copy.deepcopy(self.corners[self.corner_iterator])
			except IndexError:
				done = True


	def open_space_add(self, corner): 
		corner.point_connections.remove(corner.point)
		for i in xrange(len(corner.point_connections)):
			corner.segment_connections.append(None)
			corner.corner_connections.append(None)

	def Open_Spot(self, list_a):
		for i in xrange(len(list_a)):
			if list_a[i] == None:
				return i
	def segment_draw(self, iterator_counter):
		self.segments.append(Segment(self.current_corner.point, self.current_corner.point_connections[iterator_counter], self.current_corner))
		self.current_segment = self.segments[-1]
		done = False
		draw_point = copy.deepcopy(self.current_segment.includes[-1])
		slope = self.slope_find(self.current_corner.point, draw_point)
		self.current_slope = copy.deepcopy(slope)
		while(not done):
			draw_point[0] += slope[0]
			draw_point[1] += slope[1]
			if draw_point in self.invalids:
				self.current_point = copy.deepcopy(Current_Point(draw_point))
				if self.connections_analyze(self.point_scan(self.current_point.point)):
					self.current_segment.includes.append(self.current_point.point)

				else:
					self.current_segment.includes.append(self.current_point.point)
					done = True
					continue
			else:
				self.draw()
				draw_point = copy.deepcopy(self.current_segment.includes[-1])
		done = False
		for i in xrange(len(self.corners)):
			if self.corners[i].point == self.current_segment.includes[-1]:
				reference_corner = self.corners[i]
				done = True
		if not done:
			self.corners.append(Corner(self.current_segment.includes[-1], self.point_scan(self.current_segment.includes[-1])))
			self.current_segment.corners.append(self.corners[-1])
			reference_corner = self.corners[-1]
			self.open_space_add(self.corners[-1])
			done = True
		reference_corner.segment_connections[reference_corner.point_connections.index(self.current_segment.includes[-2])] = copy.deepcopy(self.current_segment)
		reference_corner.corner_connections[reference_corner.point_connections.index(self.current_segment.includes[-2])] = copy.deepcopy(self.corners[-1])
		self.current_corner.segment_connections[iterator_counter] = copy.deepcopy(self.current_segment)
		self.current_corner.corner_connections[iterator_counter] = copy.deepcopy(self.corners[-1])
	def point_scan(self, point):
		connections = []
		test_point = list(point)
		for x in xrange(-1, 2):
			for y in xrange(-1, 2):
				test_point[0] += x
				test_point[1] += y
				if test_point in self.invalids:
					connections.append(test_point)
					self.scanned_list.append(test_point)
				test_point = list(point)
			test_point = list(point)
		return connections

	def connections_analyze(self, connections):
		current_index = connections.index(self.current_point.point)
		if len(connections) == 3:
			if abs(connections[current_index][0] - connections[0][0]) == abs(connections[current_index][0] - connections[2][0]):
				return True
			else:
				return False
		else:
				if abs(self.current_slope[0]) >= 1:
					test_point = copy.deepcopy(self.current_point.point)
					test_point[1] += 1
					if test_point in self.invalids:
						return False
					test_point[1] -= 2
					if test_point in self.invalids:
						return False
					return True
				else:
					test_point = copy.deepcopy(self.current_point.point)
					test_point[0] += 1
					if test_point in self.invalids:
						return False
					test_point[0] -= 2
					if test_point in self.invalids:
						return False
					return True


	def slope_find(self, origin_point, *points):
		master_slope = []
		for i in xrange(len(points)):
			slope = []
			slope.append(points[i][0] - origin_point[0])
			slope.append(points[i][1] - origin_point[1])
			master_slope.append(slope)
		if len(points) == 1:
			return slope
		else:
			 return master_slope


	def draw(self):
		segment = []
		first_point = copy.deepcopy(self.current_segment.includes[-2])
		second_point = copy.deepcopy(self.current_segment.includes[-1])
		slope = self.slope_find(first_point, second_point)
		done = False
		segment.append(copy.deepcopy(second_point))
		while(not done):
			second_point[0] += slope[0]
			second_point[1] += slope[1]
			if second_point in self.invalids:
				done = True
				continue
			else:
				segment.append(copy.deepcopy(second_point))
				self.current_segment.includes.append(copy.deepcopy(second_point))
		self.current_segment.locations.append(self.midpoint(segment[0], segment[-1]))
		mute_point = copy.deepcopy(Current_Point(self.current_segment.includes[-1]))
		mute_point.point[0] += slope[0]
		mute_point.point[1] += slope[1]
		self.current_segment.includes.append(mute_point.point)
	def midpoint(self, first_point, second_point):
		midpoint = []
		midpoint.append((first_point[0] + second_point[0]) / 2)
		midpoint.append((first_point[1] + second_point[1]) / 2)
		return midpoint

