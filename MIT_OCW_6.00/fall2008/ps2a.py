'''Max unbuyable number of McNuggets'''

import math

# Global variables http://stackoverflow.com/questions/855493/referenced-before-assignment-error-in-python

num_consecutive = 0  # number of consecutive nuggets that could be bought
start_nuggets = 1  # technically could be the smallest multiple of nuggets possible, but problem states to start 1
current_nuggets = start_nuggets
last_unbuyable = start_nuggets

# 4a + 9b + 20c = n
# [1] set upper bound on how many max packs are possible in permutations. Need ceiling for max to work with range()
a = math.ceil(current_nuggets / 6)
b = math.ceil(current_nuggets / 9)
c = math.ceil(current_nuggets / 20)


def check_nuggets():
	# check bounds
		# sum of smallest buyable quantity must be smaller than tested value
		# otherwise, increment until it is, then loop through the nugget buying
		# kind of dumb if numbers are hard coded, but useful for next problem, when numbers are variable

	global num_consecutive
	global start_nuggets
	global current_nuggets
	global last_unbuyable
	global a, b, c

	while(current_nuggets < 6):
		last_unbuyable = current_nuggets
		current_nuggets += 1

	print("last_unbuyable {} current_nuggets {}".format(last_unbuyable, current_nuggets))

	while num_consecutive < 6:  # from problem 2, we know for a 6pack, we need 6 consecutive values to get every possible value after
		a = math.ceil(current_nuggets / 6)  # Forgot to add this initially. a, b, c will stay at global 0 forever otherwise
		b = math.ceil(current_nuggets / 9)
		c = math.ceil(current_nuggets / 20)
		sum_nuggets()  # [2] http://stackoverflow.com/questions/189645/how-to-break-out-of-multiple-loops-in-python

	print("Largest number of McNuggets that cannot be bought in exact quantity: {}".format(last_unbuyable))

def sum_nuggets():

	global current_nuggets
	global num_consecutive
	global last_unbuyable
	global a, b, c

	# [2] why use separate function?
	for x in range(0, a):
		for y in range(0, b):
			for z in range(0, c):
				if(x*6 + y*9 + z*20 == current_nuggets):
				# if true, increment current_nuggets and num_consecutive, return
					current_nuggets += 1
					num_consecutive += 1
					print("{} can be bought with {}x6 {}x9 {}x20".format(current_nuggets, x, y, z))
					return
	# if no match is found after exhausting all combinations, clear num_consecutive, update last_unbuyable, increment current_nuggets, return
	print("{} cannot be bought".format(current_nuggets))
	last_unbuyable = current_nuggets
	current_nuggets += 1
	num_consecutive = 0
	return


if __name__ == '__main__':
	check_nuggets()


'''Notes
[1]: Should I have the a b c division check inside check_bounds() or defined at the top? Global seems to give some advantages
[2]: in the case that a match is found before each variable's maximum range is reached, break will only leave one loop when all loops need to stop.
Return is best solution for this.

'''