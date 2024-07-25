def solution(n):
    sv = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
        5000: "V̅",
        10000: "X̅",
    }
    sv_keys = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000]
    i = 0
    list = []

    # loop through each value in the integer
    for char in str(n):
        # accordingly set base value, based on integer length - 1 / 10 / 100 / 1000 and loop iteration
        match len(str(n)) - i:
            case 1:
                base_index = 0
            case 2:
                base_index = 2
            case 3:
                base_index = 4
            case 4:
                base_index = 6
            case 5:
                base_index = 8

        base_key = sv_keys[base_index]
        base_value = sv[base_key]

        if int(char) == 0:
            pass
        elif 0 < int(char) < 4:
            list.append(int(char) * base_value)
        elif int(char) == 4:
            base_key = sv_keys[base_index + 1]
            prim_value = sv[base_key]
            list.append(f"{base_value}{prim_value}")
        elif int(char) == 5:
            base_key = sv_keys[base_index + 1]
            prim_value = sv[base_key]
            list.append(f"{prim_value}")
        elif 5 < int(char) < 9:
            base_key = sv_keys[base_index + 1]
            prim_value = sv[base_key]
            list.append(f"{prim_value}{base_value*(int(char) - 5)}")
        elif int(char) == 9:
            base_key = sv_keys[base_index + 2]
            prim_value = sv[base_key]
            list.append(f"{base_value}{prim_value}")
        i += 1

    return print("".join(list))


solution(12989)
