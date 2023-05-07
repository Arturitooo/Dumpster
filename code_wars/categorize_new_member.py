def open_or_senior(data):
    categories = []
    for x in data:
        age = x[0] 
        handicap = x[1]
        if age >= 55 and handicap>=7:
            categories.append("Senior")
        else:
            categories.append("Open")
    return categories


open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)])