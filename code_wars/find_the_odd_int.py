
def find_it(seq):
    for num in seq:
        counter = seq.count(num)
        if counter % 2 == 1:
            return num
    return None


numbers_list = [1,1,2,2,3,4,4,5,5,4,1]
print(find_it(numbers_list))