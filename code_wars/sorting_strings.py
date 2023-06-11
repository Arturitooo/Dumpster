array = ["Telescopes", "Glasses", "Eyes", "Monocles"]
print(array)

for x in range(len(array)):
    for i in range(0,len(array)):
        if array[i] == array[-1]:
            break
        elif len(array[i]) > len(array[i+1]):
            change = array[i]
            array[i] = array[i+1]
            array[i+1] = change

print(array)

#refactored version:
def sort_by_length(array):
    return sorted(array, key=len)

print(array)