def find_word_with_smallest_difference(words):
    def calculate_difference(word):
        difference = 0
        for i in range(len(word)-1):
            difference += abs(ord(word[i+1]) - ord(word[i]))
        print(difference)
        return difference
        

    words_list = words.split(", ")
    smallest_difference = float('inf')
    smallest_word = ""

    for word in words_list:
        difference = calculate_difference(word)
        if difference < smallest_difference:
            smallest_difference = difference
            smallest_word = word

    print("Najmenšia hodnota rozdielu medzi písmenami má slovo:", smallest_word)
    print("Súčet týchto hodnôt je:", smallest_difference)

find_word_with_smallest_difference("Adolf, Gregor, Filip")