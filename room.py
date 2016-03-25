from data import Map, Current_Point, Segment, Corner
import copy
import math
import numpy
anti_region = [[6,0], [7,0], [8,0], [9,0], [10,0],
[6,1], [7,1], [8,1], [9,1], [10,1],
[6,2], [7,2], [8,2], [9,2], [10,2]]
invalids = [[0,0],[0,1],[0, 4], [0, 5],
 [1, 0], [1,5], 
 [2,0], [2, 5], 
 [3,0], [3, 5], 
 [4, 0], [4, 5], 
 [5,0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], 
 [6, 3], [6, 5], 
 [7, 3], [7, 5], 
 [8, 3], [8, 5], 
 [9, 3], [9, 5], 
 [10, 3], [10, 4], [10, 5]]
map1 = Map(invalids, 10, 5)
map1.master_creation()


def other_data(current_data, data_list):
	if current_data == data_list[0]:
		return data_list[1]
	else:
		return data_list[0]

class New_Map(object):
	def __init__(self, corners, segments):
		self.corners = corners
		self.segments = segments

new_segments = []
new_corners = []
for i in xrange(len(map1.segments)):
	new_segments.append(copy.copy(map1.segments[i]))
for i in xrange(len(map1.corners)):
	new_corners.append(copy.copy(map1.corners[i]))


for i in xrange(len(new_corners)):
	for u in xrange(len(new_corners[i].point_connections)):
		new_corners[i].corner_connections[u] = None
		new_corners[i].segment_connections[u] = None

for i in xrange(len(new_segments)):
	new_segments[i].corners = []

for i in xrange(len(new_segments)):
	for u in xrange(2):
		if u == 1:
			test_point = copy.copy(new_segments[i].includes[1])
		else:
			test_point = copy.copy(new_segments[i].includes[-2])
		for z in xrange(len(new_corners)):
			for x in xrange(len(new_corners[z].point_connections)):
				if test_point == new_corners[z].point_connections[x]:
					new_corners[z].segment_connections[new_corners[z].point_connections.index(test_point)] = new_segments[i]
					new_segments[i].corners.append(new_corners[z])
for i in xrange(len(new_corners)):
	for u in xrange(len(new_corners[i].segment_connections)):
		new_corners[i].corner_connections[u] = other_data(new_corners[i], new_corners[i].segment_connections[u].corners)

map2 = New_Map(new_corners, new_segments)



class Leg(object):
	def __init__(self, corners, segment):
		self.corners = [corners[0], corners[1]]
		self.segments = [segment]
		self.other_leg = None
		self.direction = None

	def ccw(self, A, B, C):
		return (B[0] - A[0]) * (C[1] - A[1]) > (B[1] - A[1]) * (C[0] - A[0])

	def direction_set(self):
		if self.ccw(self.other_leg.corners[-1].point, self.corners[0].point, self.corners[1].point):
			self.direction = "Counter"
		else:
			self.direction = "Clock"

def other_data(current_data, data_list):
	if current_data == data_list[0]:
		return data_list[1]
	else:
		return data_list[0]

def slope_find(first_point, second_point):
	slope = []
	slope.append(second_point[0] - first_point[0])
	slope.append(second_point[1] - first_point[1])
	return slope

def markers_create(corner):
	if corner.point == [5,3]:
		for i in xrange(len(corner.segment_connections)):
			print str(corner.segment_connections[i].includes)
	corner.markers = []
	for i in xrange(len(corner.segment_connections) - 1):
		corner.markers.append([corner.segment_connections[i], corner.segment_connections[i + 1]])
	corner.markers.append([corner.segment_connections[0], corner.segment_connections[-1]])
	if corner.markers[0] == corner.markers[1]:
		corner.markers.remove(corner.markers[0])

def possibles_decide(leg):
	possibles = []
	proxy_segs = copy.copy(leg.corners[-1].segment_connections)
	proxy_segs.remove(leg.segments[-1])
	for i in xrange(len(proxy_segs)):
		if leg.ccw(leg.corners[-2].point, leg.corners[-1].point, proxy_segs[i].includes[-2]) and leg.direction == "Counter":
			possibles.append(proxy_segs[i])
		elif not leg.ccw(leg.corners[-2].point, leg.corners[-1].point, proxy_segs[i].includes[-2]) and leg.direction == "Clock":
			possibles.append(proxy_segs[i])
	for i in xrange(len(possibles)):
		if vector_solve(possibles[i], leg):
			return possibles[i]
	for i in xrange(len(proxy_segs)):
		if slope_find(leg.corners[-1].point, proxy_segs[i].includes[-2]) == slope_find(leg.segments[-1].includes[-2], leg.corners[-1].point):
			print "Proxy Seg: " + str(proxy_segs[i].includes)
			print "Same Slope"
			return proxy_segs[i]

def vector_solve(segment, leg):
	print str(leg.corners[1].point)
	y_1 = leg.corners[-1].point[1] - leg.corners[-2].point[1]
	y_2 = other_data(leg.corners[-1], segment.corners).point[1] - leg.corners[-1].point[1]
	x_1 = leg.corners[-1].point[0] - leg.corners[-2].point[0]
	x_2 = other_data(leg.corners[-1], segment.corners).point[0] - leg.corners[-1].point[0]
	dot_product = (x_1*x_2) + (y_1*y_2)
	denominator = (math.sqrt(pow(x_1, 2) + pow(y_1, 2))) * (math.sqrt(pow(x_2, 2) + pow(y_2, 2)))
	angle = math.acos(dot_product/denominator)
	if angle >= (3.14592/2):
		return False
	else:
		return True


class Room(object):
	def __init__(self, corners_one, corners_two, segments_one, segments_two):
		self.corners = self.info_sort(corners_one, corners_two)
		self.segments = self.info_sort(segments_one, segments_two)
		self.draw_check(corners_one, corners_two)
	def info_sort(self, info_one, info_two):
		array = []
		for i in xrange(len(info_one)):
			array.append(info_one[i])
		for i in xrange(len(info_two)):
			if info_two[i] not in array:
				array.append(info_two[i])
	def draw_check(self, corners_one, corners_two):
		if corners_one[-1] == corners_two[-1]:
			return 0
		slope = slope_find(corners_one[-1].point, corners_two[-1].point)
		draw_point = corners_one[-1].point
		draw_point[0] += slope[0]
		draw_point[1] += slope[1]
		new_segment = Segment(corners_one[-1].point, draw_point, corners_one[-1])
		new_segment.corners.append(corners_two[-1])
		while(draw_point != corners_two[-1].point):
			new_segment.includes.append(copy.copy(draw_point))
			draw_point[0] += slope[0]
			draw_point[1] += slope[1]




def room_creation(map2):
	rooms = []
	for i in xrange(len(map2.corners)):
		markers_create(map2.corners[i])
	for i in xrange(len(map2.corners)):
		for u in xrange(len(map2.corners[i].markers)):
			print str(map2.corners[i].segment_connections[0].includes)
			if len(map2.corners[i].markers) == 0:
				continue
			leg_one = Leg([map2.corners[i], other_data(map2.corners[i], copy.copy(map2.corners[i].markers[u][0].corners))], map2.corners[i].markers[u][0])
			leg_two = Leg([map2.corners[i], other_data(map2.corners[i], copy.copy(map2.corners[i].markers[u][1].corners))], map2.corners[i].markers[u][1])
			del map2.corners[i].markers[u]
			leg_one.other_leg = leg_two
			leg_two.other_leg = leg_one
			leg_one.direction_set()
			leg_two.direction_set()
			i = 0
			append = True
			print "Inital Leg One Seg: " + str(leg_one.segments[0].includes)
			print "Initial Leg Two Seg: " + str(leg_two.segments[0].includes)
			while possibles_decide(leg_one) and possibles_decide(leg_two):
				i += 1
				leg_one.segments.append(possibles_decide(leg_one))
				try:
					if [leg_one.segments[-1], leg_one.segments[-2]] in leg_one.corners[-1].markers:
						leg_one.corners[-1].markers.remove([leg_one.segments[-1], leg_one.segments[-2]])
					else:
						leg_one.corners[-1].markers.remove([leg_one.segments[-2], leg_one.segments[-1]])
					leg_two.segments.append(possibles_decide(leg_two))
					if [leg_two.segments[-1], leg_two.segments[-2]] in leg_two.corners[-1].markers:
						leg_two.corners[-1].markers.remove([leg_two.segments[-1], leg_two.segments[-2]])
					else:
						leg_two.corners[-1].markers.remove([leg_two.segments[-2], leg_two.segments[-1]])
				except ValueError:
					print "Yeah"
				if leg_one.segments[-1] == leg_two.segments[-1]:
					print "Same"
					break
				leg_one.corners.append(other_data(leg_one.corners[-1], leg_one.segments[-1].corners))
				leg_two.corners.append(other_data(leg_two.corners[-1], leg_two.segments[-1].corners))
				if leg_one.corners[-1] == leg_two.corners[-1]:
					if [leg_one.segments[-1], leg_two.segments[-1]] in leg_one.corners[-1].markers:
						leg_one.corners[-1].markers.remove([leg_one.segments[-1], leg_two.segments[-1]])
						append = False
					else:
						leg_one.corners[-1].markers.remove([leg_two.segments[-1], leg_one.segments[-1]])
						append = False
			for i in xrange(len(leg_one.segments)):
				print 'Leg One Segment %s: ' % i + str(leg_one.segments[i].includes)
			for i in xrange(len(leg_two.segments)):
				print 'Leg Two Segment %s: ' % i + str(leg_two.segments[i].includes)
			if append == True:
				rooms.append(Room(copy.copy(leg_one.corners), copy.copy(leg_two.corners), copy.copy(leg_one.segments), copy.copy(leg_one.corners)))
	return rooms




rooms = room_creation(map2)


