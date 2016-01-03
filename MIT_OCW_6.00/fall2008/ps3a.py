from string import *

def countSubStringMatch(target, key):

    key_instances = 0

    #find the first appearance
    #find the next appearance, with the last found appearance's index + 1. (Can't do last index + len(key) for repeating strings like finding "hihi" in "hihihi")



def countSubStringMatchRecursive(target, key):
    
    key_instances = 0
