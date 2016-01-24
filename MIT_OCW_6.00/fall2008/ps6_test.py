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


    # testing time limits
    k_1 = get_time_limit(points_dict, 1)
    k_2 = get_time_limit(points_dict, 2)
    k_3 = get_time_limit(points_dict, 3)
    k_4 = get_time_limit(points_dict, 4)
    print(k_1, k_2, k_3, k_4)