import struct
from PIL import Image

im = Image.open('map.png', 'r')
dimensions = get_image_info(im)
pixel_values = list(im.getdata())
walls = []
wall = pixel_values[0]
for i in xrange(pixel_values.length() - 1):
	for y in xrange(dimensions[1]):
		for x in xrange(dimensions[0]):
			if (pixel_values[i] == wall):
				walls.append([x, y])

def get_image_info(data):
    if is_png(data):
        w, h = struct.unpack('>LL', data[16:24])
        width = int(w)
        height = int(h)
    else:
        raise Exception('not a png image')
    return width, height


class Map(object):
	def __init__(self):
		self.invalids = []
		self.xdimen = []
		self.ydimen = []
class Segment(object):
	def __init__(self):
		self.points = []
		self.corners = []
class Corner(object):
	def __init__(self):
		self.point = []
		self.connections = []
		self.segments = []
		self.corner_connections = []
		self.connection_slopes = []

map1 = Map.()
map_scan
global connection_counter = 0
global corner_counter = 0
global segment_counter = 0
global current_corner
def map_scan(map1):
	current_point = map1.invalids[0]
	while(True):
		corner[corner_counter] = Corner(current_corner, point_scan(current_point), None, slope_find(point_scan(current_point)))
		current_corner = corner[corner_counter]
		for i in xrange(corner[current_corner].connections.length()):
			segment_scan(current_corner, i)
		if (point_scan(current_corner.point) == 0):
			break


def segment_scan(current_corner, iterator):
	slope = current_corner.connection_slopes[iterator]
	point_list = []
	point_list.append(current_corner.point, current_corner.connections[iterator])
	while(True):
		test_point = point_list[point_list.length() - 1]
		test_point[0] += slope[0]
		test_point[1] += slope[1]
		if (connections_analyze(point_scan(test_point)) == False):
			break
		else:
			point_list.append(test_point)
	corner_counter += 1
	map1.invalids.remove(point_list[point_list.length() - 2])
	corner[corner_counter - 1].corner_connections = corner[corner_counter]
	corner[corner_counter] = Corner(point_list[point_list.length() - 1], point_scan(point_list.length() - 1), corner[corner_counter - 1], slope_find(point_list.length() - 1))
	segment[segment_counter] = Segment[point_list, [corner[corner_counter - 1].point, point_list[point_list.length() - 1]]]
	corner[corner_counter].segments = segment[segment_counter]
	corner[corner_counter - 1].segments = segment[segment_counter]
	global segment_counter += 1
	corner[corner_counter - 1].corner_connections = corner[corner_counter]
	global segment_counter += 1

def point_scan(point):
	test_point = point
	connections = []
	for x in xrange(-1, 1):
		for y in xrange(-1, 1):
			test_point[0] += x
			test_point[1] += y
		if test_point in map1.invalids:
			connections.append()
			global connection_counter += 1
	return connections

def slope_find(connections):
	first_point = connections[0]
	master_slope = []
	for i in xrange(connections.length() - 1):
		second_point = connections[i]
		slope = []
		slope[0] = second_point[0] - first_point[0]
		slope[1] = second_point[1] - first_point[1]
		master_slope.append(slope)
	return master_slope


def connections_analyze(connections):
	if connections.length() == 3:
		if abs(connections[0][0] - connections[1][0]) == abs(connections[2][0] - connections[1][0]):
			return True
		else:
			return False
	else: 
		return False
map_scan(map1)
corners_list = []
for i in xrange(0, global corner_counter)
	corners_list.append(corner[i])
segments_list = []
for t in xrange(0, global segment_counter):
	segments_list.append(segment[t])
class Room_Leg(object):
	def __init__(self):
		self.max_slope = []
		self.segments = []
		self.corners = []
class Room(object):
	def __init__(self):
		self.segments = []
		self.points
		self.corners = []
def draw(initial_point, final_point, slope):
	segment_append = []
	midpoint = []
	midpoint[0] = (initial_point[0] + final_point[0]) / 2)
	midpoint[1] = (initial_point[1] + final_point[1] / 2)
	current_point = initial_point
	while (current_point != final_point):
		current_point[0] += slope[0]
		current_point[1] += slope[1]
		segment_append.append(current_point)
	segment_append.append(midpoint[0], midpoint[1])
	return segment_append
global Room_Counter = 0


def master_object_create(corners_list, segments_list, connection_list):
	room_list
	while(corner_counter != 0):
		current_corner_one = corner[corner_counter.length() - 1]
		current_corner_two = current_corner_one
		leg[1] = Room_Leg(current_corner.connection_slopes[0], current_corner.segments[0], None)
		leg[2] = Room_Leg(current_corner.connection_slopes[1], current_corner.segments[1], None)
		while(True):
			leg[1].corners.append(current_corner_one)
			leg[2].corners.append(current_corner_two)
			if leg[1].corners[leg[1].corners.length() - 1].connection_slopes[leg[1].corners[leg[1].corners.length() - 1].connection_slopes.length() - 1] > 1):
				if (leg[2].corners[leg[2].corners.length() - 1].connection_slope[0] > 1):
					pass
			elif (leg[1].corners[leg[1].corners.length() - 1] == leg[2].corners[leg[2].corners.length() - 1):
				points = [draw(leg[1].corners[leg[1].corners.length() - 1].point, leg[2].corners[leg[2].corners.length() - 1].point, slope_find(leg[1].corners[leg[1].corners.length() - 1].point, leg[2].corners[leg[2].corners.length() - 1].point))]
				break
				
			else:
				break
			leg[1].corners.append(leg[1].corners[leg[1].corners.length() - 1].connection_slopes[leg[1].corners[leg[1].corners.length() - 1].connection_slopes.length() - 1])
			leg[2].corners.append(leg[2].corners[leg[2].corners.length() - 1].connection_slopes[0])
			leg[1].segments.append(leg[1].corners[leg[1].corners.length() - 1].segments[leg[1].corners[leg[1].corners.length() - 1].segments.length() - 1])
			leg[2].segments.append(leg[2].corners[leg[2].corners.length() - 1].segments[0])
		segments_list = []
		corners_list = []
		for i in xrange(leg[1].segments.length() - 1):
			try:
				points.append(leg[1].segments[i].points[0])
			except IndexError:
				pass
			segments_list.append(leg[1].segments[i])

		for u in xrange(leg[2].segments.length() - 1):
			try:
				points.append(leg[2].segments[i].points[0])
			except IndexError:
				pass
			segments_list.append(leg[2].segments[u])

		for z in xrange(1, leg[1].corners.length() - 1):
			corners_list.append(leg[1].corners[z])

		for t in xrange(1, leg[2].corners.length() - 1):
			corners_list.append(leg[2].corners[t])
		room[Room_counter] = Room(segments_list, points, corners_list)
		global room_counter += 1
		room_list.append(room[Room_Counter])
	for i in segments_list:
		Room_Connect(i, room_list)

def Room_Connect(segment, room_list):
room_join = []
for i in xrange(room_list.length() - 1):
	if segment in room_list[i]:
		room_join.append[room_list[i]]
for x in xrange(0, room_join.length() - 1):
	room_join[x].room_connections.append(segment)







		









