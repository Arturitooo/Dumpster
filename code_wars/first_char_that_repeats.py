def first_dup(s):
    word_list = list(s.strip(" "))
    for i in range(0,len(s)):
        letter1 = (word_list[i])
        print(letter1)
        for j in range(i+1, len(s)):
            letter2 = (word_list[j])
            print(letter2)
            if letter1 == letter2:
                print(f"bingo <3, the magic letter is: {letter2}")
                quit()

    return letter1

first_dup("hello")