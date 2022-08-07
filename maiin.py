
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = [int(x[1]) for x in data if x[1].isdigit()]
#     print(data)
#     print(temperatures)
#     for row in data:
#         print(row)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# monday = data[data.day == "Monday"]
# print(monday.temp * 1.8 + 32, " fahrenheit")

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56,65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("New_Data.csv")





