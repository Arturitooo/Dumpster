def high(x):
    # slice the whole sentence into single word
    list = x.split(" ")
    top_score = 0
    winning_word = ""
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    # loop through word
    for word in list:
        word_score = 0

        # loop through letters
        for letter in word:
            word_score = word_score + alphabet.index(letter) + 1
            print(word_score, word)
        # check if better score
        if word_score > top_score:
            top_score = word_score
            winning_word = word
    return winning_word


print(high("man i need a taxi up to ubud"))
