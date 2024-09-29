# with open("weather_data.csv", "r") as csv:
#     content = csv.read()
# data = content.split("\n")
# print(data)
# import csv
#
# with open("weather_data.csv", "r") as data_csv:
#     data = csv.reader(data_csv)
#     temp = []
#     for row in data:
#         if row[1] != 'temp':
#             temp.append(int(row[1]))
#
# print(temp)
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data)
import pandas
print(pandas.read_csv("weather_data.csv"))