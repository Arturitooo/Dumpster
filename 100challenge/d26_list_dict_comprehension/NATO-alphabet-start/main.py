student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv(r"C:\Users\Art\Documents\GitHub\learning\100challenge\d26_list_dict_comprehension\NATO-alphabet-start\nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}

print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
provided_word = input("Please provide the word to transform: ").upper()

decoded_word = [phonetic_dict[letter] for letter in provided_word]
print(decoded_word)