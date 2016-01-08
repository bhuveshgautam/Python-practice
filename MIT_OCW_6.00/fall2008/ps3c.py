from string import *

# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

def subStringMatchExact(target, key):

    a = ()
    key_index = 0

    while True:
        key_index = target.find(key, key_index)
        if key_index != -1:
            a = a + (key_index,)
            key_index += 1
        else:
            break
    return a

def constrainedMatchPair(first_match, second_match, length):
    # first_match and _second_match are both tuples, return should also be tuple
    filtered = ()

    for x in range(len(first_match)):
        for y in range(len(second_match)):
            #  starting index of first string + length of first string + 1 = starting index of second string
            if (first_match[x] + length + 1 == second_match[y]):
                filtered += (first_match[x],)
    return filtered

### the following procedure you will use in Problem 3


def subStringMatchOneSub(key,target):  # why would you make everything (target, key) up to now and switch them here? ;A;
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print ('breaking key',key,'into',key1,key2)
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print ('match1',match1)
        print ('match2',match2)
        print ('possible matches for',key1,key2,'start at',filtered)
    return allAnswers
        



if __name__ == '__main__':
    subStringMatchOneSub("ATGC", "ATGACATGCA")