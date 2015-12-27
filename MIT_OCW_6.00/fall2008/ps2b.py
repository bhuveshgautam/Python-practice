'''Unbuyable McNuggets'''

###
# template of code for Problem 4 of Problem Set 2, Fall 2008
###

import math

bestSoFar = 0     # variable that keeps track of largest number
                  # of McNuggets that cannot be bought in exact quantity
packages = (6, 9, 20)   # variable that contains package sizes


# if defining functions isn't allowed... need to find another way to implement this
# http://stackoverflow.com/a/3357445 This one is really clever. Uses StopIteration exception. Clean.
# http://stackoverflow.com/a/654002 for-else construction. Not perfect.

num_consecutive = 0


for n in range(10):   # only search for solutions up to size 150
    # complete code here to find largest size that cannot be bought
    # when done, your answer should be bound to bestSoFar
    a = math.ceil(n / packages[0])
    b = math.ceil(n / packages[1])
    c = math.ceil(n / packages[2])

    print("n is {}, {} {} {}".format(n, a, b, c))

    buyable = False

    for x in range(a):
        for y in range(b):
            for z in range(c):
                if((x*packages[0] + y*packages[1] + z*packages[2]) == n):
                    print("{} {} {} = {}".format(x, y, z, x*packages[0] + y*packages[1] + z*packages[2]))
                    num_consecutive += 1
                    buyable = True
                    break
            if buyable:
                print("First")
                break
        if buyable:
            print("Second")
            break
    
    # code here executes if loops finished without a match OR if for break with a match
    if not buyable:
        bestSoFar = n
        num_consecutive = 0


print("Given package sizes {}, {}, and {}, the largest number of McNuggets that cannot be bought in exact quantity is: {}".format(
    packages[0], packages[1], packages[2], bestSoFar))

'''
How does Python like their variables naming? camelCase? words_with_underscores?? User preference?? AHHH
[1] Need to do some debugging to figure out how the control flow works with the break and continue there
'''
