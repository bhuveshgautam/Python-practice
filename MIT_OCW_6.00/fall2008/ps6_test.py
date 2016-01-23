from ps6 import *



if __name__ == '__main__':
    word_list = load_words()
    get_words_to_points(word_list)  # points_dict is global, no need to assign it again
    

    # test 1
    hand = get_frequency_dict("hi")
    word = pick_best_word(hand, points_dict)
    print(word, points_dict[word])

    # test 2
    hand = get_frequency_dict("acmz")
    word = pick_best_word(hand, points_dict)
    print(word, points_dict[word])