def high_and_low(numbers):
    numbers = numbers.split(" ")
    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i])
    return str(max(numbers)) + " " + str(min(numbers))


print(high_and_low("1 2 6 4 5"))
