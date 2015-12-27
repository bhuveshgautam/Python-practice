'''Max unbuyable number of McNuggets'''

import math

# Global variables http://stackoverflow.com/questions/855493/referenced-before-assignment-error-in-python

num_consecutive = 0  # number of consecutive nuggets that could be bought
start_nuggets = 1  # technically could be the smallest multiple of nuggets possible, but problem states to start 1
current_nuggets = start_nuggets
last_unbuyable = start_nuggets

# 4a + 9b + 20c = n
# [1] set upper bound on how many max packs are possible in permutations. Need ceiling for max to work with range()
a = math.ceil(current_nuggets / 6) + 1
b = math.ceil(current_nuggets / 9) + 1
c = math.ceil(current_nuggets / 20) + 1


def check_nuggets():

	global num_consecutive
	global start_nuggets
	global current_nuggets
	global last_unbuyable
	global a, b, c

	#while(current_nuggets < 6):
	#	last_unbuyable = current_nuggets  # looks less silly when pack quantities are variable
	#	current_nuggets += 1

	while num_consecutive < 6:  # from problem 2, we know for a 6pack, we need 6 consecutive values to get every possible value after
		a = math.ceil(current_nuggets / 6) + 1  # Forgot to add this initially. Otherwise, a, b, c will stay 0 forever
		b = math.ceil(current_nuggets / 9) + 1
		c = math.ceil(current_nuggets / 20) + 1
		sum_nuggets()  # [2] http://stackoverflow.com/questions/189645/how-to-break-out-of-multiple-loops-in-python

	print("Largest number of McNuggets that cannot be bought in exact quantity: {}".format(last_unbuyable))

def sum_nuggets():

	global current_nuggets
	global num_consecutive
	global last_unbuyable
	global a, b, c

	# [2] why use separate function?
	for x in range(a):
		for y in range(b):
			for z in range(c):
				if(x*6 + y*9 + z*20 == current_nuggets):
					print("{} is bought with {} {} {}".format(current_nuggets, x, y, z))
					current_nuggets += 1
					num_consecutive += 1
					return
	# if this is reached, all combinations have been exhausted without a match
	print("{} unbuyable".format(current_nuggets))
	last_unbuyable = current_nuggets
	current_nuggets += 1
	num_consecutive = 0
	return

# if I don't have this, the proram will have no errors, but doesn't seem to ever execute. Will examine this more later.
# http://stackoverflow.com/questions/22492162/understanding-the-main-method-of-python
if __name__ == '__main__':
	check_nuggets()


'''Notes
[1]: Should I have the a b c division check inside check_bounds() or defined at the top? Global seems to give some advantages
^This question has been indirectly answered. Passing the variables might be more convenient than the walls of global keyword.
Will need to check how variables passed in functions work in Python.
[2]: in the case that a match is found before each variable's maximum range is reached, break will only leave one loop when all loops need to stop.
Return is best solution for this.

'''