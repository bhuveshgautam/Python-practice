# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

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
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
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

def play_ghost():
    print("Welcome to Ghost!")

    current_player = "Player 1"
    player1_score, player2_score = 0, 0
    player_input = ""
    current_fragment = ""
    
    while True:
        print(current_player, "goes first.")
        print("Current word fragment:", current_fragment.lower())
        
        # input word
        player_input = input(current_player, "says letter: ")
        if player_input in string.ascii_letters:
            # add input to fragment
            # check if word can be formed with fragment. If not, lose and break
            # check if fragment is a word > 3 characters. If it is, lose and break

            # switch current player
        else:
            print(player_input, "is not a valid input. Please try again.")

