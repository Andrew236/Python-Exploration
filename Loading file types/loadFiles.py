import os
import pandas 


#In this file I am using pandas to load different
#file type and data
#I then print that data in the file!

df1 = pandas.read_csv("supermarkets.csv")
print(df1)

#here is how to d the same thing with a json file:
df2 = pandas.read_json("supermarkets.json")
print(df2)

#loading excell file
df3 = pandas.read_excel("supermarkets.xlsx",sheet_name=0)
print(df3)

#loading a txt file which the data is seperated by 
#commas 

df4 = pandas.read_csv("supermarkets-commas.txt")
print(df4)

#loading a txt file which the data is seperated by semi
#colons
#note that the default sperator for a csv is a comma so up above
#it does not need to be changed

df5 = pandas.read_csv("supermarkets-semi-colons.txt",sep=";")
print(df5)

#dealing with data that doesn't have a header 

#df6 = pandas.read_csv("data.txt",header = None)
#print(df6)

#NOTE YOU THEN HAVE TO ASSING THE COLUMNS:
#df6.columns = ["ID", "ADDRRESS"]