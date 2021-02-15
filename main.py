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
print(data) # this is a dataframe
print(data["temp"])  # this will give a temperature, this is a Series

