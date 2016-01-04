from string import *


def countSubStringMatch(target, key):

    key_instances = 0

    #find the first appearance
    #find the next appearance, with the last found appearance's index + 1. (Can't do last index + len(key) for repeating strings like finding "hihi" in "hihihi")
    key_index = target.find(key)

    while key_index != -1:
        key_index = target.find(key, key_index + 1)
        key_instances += 1

    print("""The string "{}" appears in "{}" {} times. """.format(key, target, key_instances))


def countSubStringMatchRecursive(target, key):
    
    # since a counter is not supplied within the arguments, solution is to call another function that passes a counter (but that seems cheap)
    # other solution is to return an int... but how to make sure it doesn't reset to 0 every time...?

    key_index = target.find(key)

    if key_index == -1:  # base case, can leave
        key_instances = 0
        return key_instances
    else:  # match found, increment
        key_instances = 1  # add one for this recursion frame
        key_instances += countSubStringMatchRecursive(target[key_index + 1:], key)
        print("""The string "{}" appears in "{}" {} times. """.format(key, target, key_instances))
        return key_instances


if __name__ == '__main__':
    target = "atgacatgcacaagtatgcat"
    key = "atgc"
    countSubStringMatchRecursive(target, key)