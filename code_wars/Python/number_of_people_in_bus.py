def number(bus_stops):
    people = 0
    for bus_stop in bus_stops:
        people = people + bus_stop[0] - bus_stop[1]
    return people


print(number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]))  # 17
