#In this file I am using pandas to open a csv file 
#which contails data
#I then print that data in the file!

import os
import pandas

df1 = pandas.read_csv("supermarkets.csv")
print(df1)

#here is how to d the same thing with a json file:

df2 = pandas.read_json("supermarkets.json")
print(df2)