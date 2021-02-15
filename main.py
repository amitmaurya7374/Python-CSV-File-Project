"""In this Project we will learn about csv and Pandas libary"""
"""
what is csv data?
csv stands for comma seprated value.
"""
# Not a better approach for handling a csv data
# with open("weather_data.csv") as file:
#     data = file.readlines()
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":  # excludimg a temp label
#             temperature.append(int(row[1]))
# print(temperature)

"""The above code  is only good for small row of data . what if we have lots 
of lot row of data then we will use a pandas libary which is built for data analysis.
"""
import pandas as pd

"""Only thesee thing we have to do as compare to above code . :)"""
"""
Some Notes:
In pandas we have DataFrames and Series 
DataFrames => is actually a whole table 
Series is equivalent to list .It is a kind a single column from a table

"""
data = pd.read_csv("weather_data.csv")
print(data)  # this is a dataframe
print(data["temp"])  # this will give a temperature, this is a Series

"""COnverting a dataframe into a dictionary"""
data_dict = data.to_dict()
print(data_dict)

"""converting a series into a list"""
data_list = data["temp"].to_list()
print(data_list)  # give a temperature list

# way to long
# average = 0
# total = 0
# for temp in data_list:
#     print(temp)
#     total += temp
#     average = total / len(data_list)
# print(f"average: {int(average)}")


"""We have computations method in pandas"""
average_temp = data["temp"].mean()
print(average_temp)

# getting a maximun value from a series
max_temp = data["temp"].max()
print(max_temp)

# Gettting a  Data in Columns

condition = data["condition"]  # one way to use
print(condition)

condition_2 = data.condition  # second way to access column by dot operation
print(condition_2)

# Getting hold of entire row
"""Syntax : whole_table[column_that_i_want_to_search_through == "condition"]
for eg:
    data[data["conditon"] == "Rain"]
"""
first_row = data[data.day == "Monday"]
print(first_row)

condition_row = data[data["condition"] == "Rain"]
print(condition_row)

# Getting a entire row which has max temperature
max_temp_row = data[data["temp"] == data["temp"].max()]
print(max_temp_row)

# Getting a single value from a entire row
monday = data[data.day == "Monday"]
mon_condition = monday.condition
mon_temp = monday.temp
temp_in_f = ((mon_temp * 9 / 5) + 32)
print(f"temp in f :{temp_in_f}")
print(mon_condition)

# creating a data frame from a scratch
score_dict = {
    "name": ["Amit", "Luci", "Imaginary_friend"],
    "score": [78, 666, 100]
}
score_data_table = pd.DataFrame(score_dict)
print(score_data_table)
# we can also convert this into a csv file
score_data_table.to_csv("score_data.csv")
