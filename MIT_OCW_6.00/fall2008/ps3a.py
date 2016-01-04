from string import *

def countSubStringMatch(target, key):

    key_instances = 0

    #find the first appearance
    #find the next appearance, with the last found appearance's index + 1. (Can't do last index + len(key) for repeating strings like finding "hihi" in "hihihi")
    key_index = target.find(key)

    while key_index != -1:
        key_index = target.find(key, key_index + 1)
        key_instances += 1

    print("""The string "{}" appears in {} {} times. """.format(key, target, key_instances))


def countSubStringMatchRecursive(target, key):
    
    key_instances = 0


if __name__ == '__main__':
    target = "atgacatgcacaagtatgcat"
    key = "atgc"
    countSubStringMatch(target, key)