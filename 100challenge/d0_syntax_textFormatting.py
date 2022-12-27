message1 = 'File %s is deleted'
print(message1 % ("letter.xdd"))


message2 = 'File %s has size %d KB'
print(message2 % ("letter.xdd",100))


message3 = 'File {1:s} has size {0:d} KB'
print(message3.format(150, 'text.txt'))


