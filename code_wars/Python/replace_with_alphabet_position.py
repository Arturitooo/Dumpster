def alphabet_position(text):
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
    text = text.lower()
    response = []
    for char in text:
        if char not in alphabet:
            pass
        else:
            response.append(str(alphabet.index(char) + 1))
    return (" ").join(response)


print(alphabet_position("hej"))
