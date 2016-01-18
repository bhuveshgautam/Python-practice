"""Unbuyable McNuggets
Author: Chang Li
Variables given: bestSoFar, packages
"""

###
# template of code for Problem 4 of Problem Set 2, Fall 2008
###

import math
import pydoc

bestSoFar = 0     # variable that keeps track of largest number
                  # of McNuggets that cannot be bought in exact quantity
packages = (6, 9, 20)   # variable that contains package sizes


# if defining functions isn't allowed... need to find another way to implement this

num_consecutive = 0


for n in range(1, 200):   # only search for solutions up to size 150
    # complete code here to find largest size that cannot be bought
    # when done, your answer should be bound to bestSoFar
    a = math.ceil(n / packages[0]) + 1
    b = math.ceil(n / packages[1]) + 1
    c = math.ceil(n / packages[2]) + 1

    buyable = False

    for x in range(a):
        for y in range(b):
            for z in range(c):
                if((x*packages[0] + y*packages[1] + z*packages[2]) == n):
                    num_consecutive += 1
                    buyable = True
                    break
            if buyable:
                break
        if buyable:
            break
    
    # code here executes if loops finished without a match OR if for break with a match
    if not buyable:
        bestSoFar = n
        num_consecutive = 0


print("Given package sizes {}, {}, and {}, the largest number of McNuggets that cannot be bought in exact quantity is: {}".format(
    packages[0], packages[1], packages[2], bestSoFar))

"""
How does Python like their variables naming? camelCase? words_with_underscores?? User preference?? AHHH

# http://stackoverflow.com/a/3357445 This one is really clever. Uses StopIteration exception. Clean.
^This is beautiful except for more than 2 levels, pointless over variable.
Also would've been preferable to define functions and use returns instead of looping.
"""
