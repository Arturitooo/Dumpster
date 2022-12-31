#day8  

import os

def caesar(word, shift, direction):
    cipherText = ''
    for letter in word:
        if letter in alphabet:
            letter_position = alphabet.index(letter)
            if direction == "encode":    
                new_position = letter_position + shift
                new_letter = alphabet[new_position]  
                cipherText += new_letter
            elif direction == "decode":    
                new_position = letter_position - shift
                new_letter = alphabet[new_position]  
                cipherText += new_letter
            else:
                break
        else:
            cipherText += letter
    os.system('cls')
    print("The encoded text is: ", cipherText, '\n')


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
interactionHappened = False

while interactionHappened == False:
    direction = input('Type "encode" to encrypt, type "decode" to decrypt: ').lower()
    word = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    if shift > 26:
        shift = shift % 26 
    caesar(word, shift, direction)
    interactionHappened = input("do you want to continue? yes/no: ")
    if interactionHappened == "yes":
        interactionHappened = False
    else:
        print("That's such a shame, sorry to see you go. Bye bye!")
        interactionHappened = True