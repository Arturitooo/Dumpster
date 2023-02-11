import os
#use "a"-append mode to add new text, w to write (overwrite)
with open(r"C:\Users\Art\Documents\GitHub\learning\100challenge\d24_upgraded_snake_game\hello.txt", mode="a") as file:
    file.write("\nI'm quite a nice guy!")

#read from file
#import os
#the "read" mode is set up as default one
#with open(r"C:\Users\Art\Documents\GitHub\learning\100challenge\d24_upgraded_snake_game\hello.txt") as file:
#    contents = file.read()
#    print(contents)