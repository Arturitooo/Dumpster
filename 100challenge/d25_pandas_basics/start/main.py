#lines = []
#with open(r"C:\Users\Art\Documents\GitHub\learning\100challenge\d25_pandas_basics\start\weather_data.csv") as weather:
#    lines.append(weather.readlines())
#print(lines)

#import csv

#with open(r"C:\Users\Art\Documents\GitHub\learning\100challenge\d25_pandas_basics\start\weather_data.csv") as weather:
#    data = csv.reader(weather)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)

import pandas

data = pandas.read_csv(r"C:\Users\Art\Documents\GitHub\learning\100challenge\d25_pandas_basics\start\weather_data.csv")


data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))  

print(data["temp"].mean())
print(data["temp"].max())

print(data["condition"])

#print row
print(data[data.day == "Monday"])

#print row when temperature was highest
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(f"Celsius: {monday.temp}")
monday["temp"] = monday["temp"] * 1.8 + 32
print(f"fahrenheit: {monday.temp}")

#create a dataframe from scratch
data_dict = {
    "students":["Amy","James","Angela"],
    "scores:":[76,56,65]   
}
data2 = pandas.DataFrame(data_dict)

print(data2)
data2.to_csv(r"C:\Users\Art\Documents\GitHub\learning\100challenge\d25_pandas_basics\start\new_data.csv")

print("\nLet's talk about squirrels for a while \n")
squirrel_data = pandas.read_csv(r"C:\Users\Art\Documents\GitHub\learning\100challenge\d25_pandas_basics\start\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = squirrel_data["Primary Fur Color"]
gray_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"]=="Gray"])
cinnamon_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"]=="Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"]=="Black"])

dictionary = {
    "Fur color:":["Gray", "Cinnamon", "Black"],
    "Number of squirrels:":[gray_squirrels_count,cinnamon_squirrels_count,black_squirrels_count]}
data3 = pandas.DataFrame(dictionary)
print(data3)
data3.to_csv(r"C:\Users\Art\Documents\GitHub\learning\100challenge\d25_pandas_basics\start\squirrels_colors.csv")