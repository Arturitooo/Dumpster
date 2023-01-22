#shortened_ifs https://www.udemy.com/course/python-dla-srednio-zaawansowanych/learn/lecture/14213764#overview

#part1
price = 123
bonus = 23
bonus_granted = True

price -= bonus if bonus_granted else price 
print(price)

#part2

rating = 5

print('very good') if rating==5 else print("good") if rating == 4 else print('weak')