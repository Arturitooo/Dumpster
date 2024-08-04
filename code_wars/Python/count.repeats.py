def count_repeats(txt):
    list = txt.split(" ")
    counter = 0
    for word in list:
        internal_counter = 0
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                internal_counter += 1
        if internal_counter > counter:
            counter = internal_counter
    return counter


print(count_repeats("hello"))
