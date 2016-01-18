"""Computing Prime numbers
Author: Chang Li
All code original.

"""

import math  # http://stackoverflow.com/questions/9439480/from-import-vs-import
import pydoc

prime_ordinal = 1  # since 2 is the first prime but not generated, we already have a prime to start with

prime_ordinal_des = int(input('Enter the Xth prime number you want to find: '))  # input() gives a string, remember to convert to int!!

test_val = 2  # [1] Current number tested for primality


while prime_ordinal < prime_ordinal_des:

	is_prime = True  # starting value of prime value is true, will change to false when checking primality
	test_val += 1  # iterate to check the next number for primality
	#  [1]

	for x in range(2, math.ceil(math.sqrt(test_val)) + 1):  # the maximum possible factor is for x^2 = x * x. So use sqrt() and round up (range does not include end number) to find possible range
		if(test_val % x) == 0:  # number is divisible by current iteration of x, immediately know it is not prime
			is_prime = False
			break  # check the next iteration

	if is_prime:
		prime_ordinal += 1

print('The prime at position {} is {}'.format(prime_ordinal_des, test_val))  # [1]

# NOTES
"""
[1]:
Originally, test_val starts at 3 and was incremented at the end of the loop. The problem with this is that at the print statement, test_val would be +OBO.
So instead of doing test_val-1 for the print statement at the end, just rearrange starting test_val to 2, and increment at the beginning of the loop. Saves an operation.
"""
