def merge_strings(first, second):
    for i in range(len(first)):
        if first[i:] == second[: len(first) - i]:
            return first[:i] + second
    return first + second


print(merge_strings("xabc", "ab"))
