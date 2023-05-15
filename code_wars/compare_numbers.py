def compare(a, b):
    aa = str(a)
    bb = str(b)
    counter = 0
    sum = 0
    for char_a in aa:
        for char_b in bb:
            if char_a == char_b:
                counter += 1
            else:
                sum +=1
    result = int(100*counter / sum)
    return str(result)+"%"

print(compare(10,15))