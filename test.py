import copy


numbers = [5, 3, 8, 9]


a = 5

b = 4


a = b


mx = 0

for i in xrange(len(numbers)):
	if numbers[i] > mx:
		mx = copy.deepcopy(numbers[i])
print mx
