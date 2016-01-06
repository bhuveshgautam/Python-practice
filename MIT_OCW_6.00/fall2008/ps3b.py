from string import *

def countSubStringMatch(target, key):

    a = ()
    key_index = 0

    while True:
        key_index = target.find(key, key_index)
        if key_index != -1:
            a = a + (key_index,)
            key_index += 1
        else:
            break


    print("""Finding "{}" in target string "{}" has starting points {} """.format(key, target, a))
    return a


if __name__ == '__main__':

    target1 = 'atgacatgcacaagtatgcat'
    target2 = 'atgaatgcatggatgtaaatgcag'

    key10 = 'a'
    key11 = 'atg'
    key12 = 'atgc'
    key13 = 'atgca'

    countSubStringMatch(target1, key10)