'''Max unbuyable number of McNuggets'''

import math

num_consecutive = 0  # number of consecutive nuggets that could be bought
start_nuggets = 1  # technically could be the smallest multiple of nuggets possible, but problem states to start 1
current_nuggets = start_nuggets

# 4a + 9b + 20c = n
# [1] set upper bound on how many max packs are possible in permutations
a = current_nuggets / 6
b = current_nuggets / 9
c = current_nuggets / 20


def check_nuggets():
	while numConsecutive < 6:  # from problem 2, we know for a 6pack, we need 6 consecutive values to get every possible value after
		sum_nuggets()  # [2] http://stackoverflow.com/questions/189645/how-to-break-out-of-multiple-loops-in-python
		

def sum_nuggets():
	# [2] why use separate function?
	# for range in a
		# for range in b
			# for range in c
				# check if Diophantine equation is true. 
				# if true, increment current_nuggets, RETURN true
	# if no match is found after exhausting all combinations, increment num_consecutive, RETURN false



'''Notes
[1]: Should I have the a b c division check inside check_bounds() or defined at the top? Global seems to give some advantages
[2]: in the case that a match is found before each variable's maximum range is reached, break will only leave one loop when all loops need to stop.
Return is best solution for this.

'''