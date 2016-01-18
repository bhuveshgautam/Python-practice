"""
Author: Chang Li
Functions given: load_words, get_frequency_dict
"""

import random
import pydoc

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!

def check_lose_conditions(current_fragment, wordlist):

    # True if lose condition is met. False if lose condition not yet met

    if len(current_fragment) > 3:
        for word in wordlist:
            if current_fragment == word:  # word is formed, lose
                return "is a word"
            if current_fragment == word[:len(current_fragment)]:
                # no exact word match, check if word can form from fragment. It it can, continue game
                return "continue"

        #arrives here if word cannot be formed by fragment, lose
        return "no word begins with"

    else:  # make sure fragment of 3 characters or fewer can still produce word
        for word in wordlist:
            if current_fragment == word[:len(current_fragment)]:
                return "continue"  # can stop at first word that can still be matched

        # arrives here if no words can form with fragment, lose
        return "no word begins with"




def play_ghost(wordlist):
    print("Welcome to Ghost!")

    current_player =  0  # 0 is player 1, 2 is player 2. Assigned so to make switching easier
    player1_score, player2_score = 0, 0
    player_input = ""
    current_fragment = ""
    
    while True:
        print("\nPlayer {}'s turn.".format(current_player + 1))
        print("Current word fragment:", current_fragment)
        
        # input word
        player_input = input("Player " + str(current_player + 1) + " says letter: ")
        if player_input in string.ascii_letters and player_input != "":
            # add input to fragment
            current_fragment += player_input.lower()
            result = check_lose_conditions(current_fragment, wordlist)

            # execute below for losing
            if result == "is a word":
                print("Player {} loses because {} {}".format(current_player + 1, current_fragment, result))
                print("Player", (current_player ^ 1) + 1, "wins!")
                break
            elif result == "no word begins with":
                print("Player {} loses because {} {}".format(current_player + 1, result, current_fragment))
                print("Player", (current_player ^ 1) + 1, "wins!")
                break
            
            # execute below for continuing
            current_player = current_player ^ 1 # bitwise XOR. 0 becomes 1, 1 becomes 0. Functions that use current_player will add 1 separately

        else:
            print(player_input, "is not a valid input. Please try again.")





play_ghost(wordlist)