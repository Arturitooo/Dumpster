def three_powers(n):
    for i in range(0, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                if n == (2**i) + (2**j) + (2**k):
                    return True
                    break
    return False


print(three_powers(8))
