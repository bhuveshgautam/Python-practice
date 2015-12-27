'''Unbuyable McNuggets'''

###
# template of code for Problem 4 of Problem Set 2, Fall 2008
###

bestSoFar = 0     # variable that keeps track of largest number
                  # of McNuggets that cannot be bought in exact quantity
packages = (6, 9, 20)   # variable that contains package sizes


# if defining functions isn't allowed... need to find another way to implement this
# http://stackoverflow.com/a/3357445 This one is really clever. Uses StopIteration exception. Clean.
# http://stackoverflow.com/a/654002 for-else construction. Not perfect.

num_consecutive = 0

for n in range(1, 200):   # only search for solutions up to size 150
    # complete code here to find largest size that cannot be bought
    # when done, your answer should be bound to bestSoFar
    a = math.ceil(current_nuggets / packages[0])
    b = math.ceil(current_nuggets / packages[1])
    c = math.ceil(current_nuggets / packages[2])

    for x in range(0, a):
        for y in range(0, b):
            for z in range(0, c):
                try:
                    if(x * packages[0] + y * packages[1] + z * packages[2] == n):
                        num_consecutive += 1
                        raise StopIteration

    # if code reaches here, no matches were found
    bestSoFar = n
    num_consecutive = 0
    # exception before/after the nonmatching n code shouldn't matter with the continue there... but this is visually more explicit
    except StopIteration:
        if(num_consecutive == packages[0]):
            break
        continue  # [1]


print("Given package sizes {}, {}, and {}, the largest number of McNuggets that cannot be bought in exact quantity is: {}".format(packages[0], packages[1], packages[2], bestSoFar))

'''
How does Python like their variables naming? camelCase? words_with_underscores?? User preference?? AHHH
[1] Need to do some debugging to figure out how the control flow works with the break and continue there
'''
