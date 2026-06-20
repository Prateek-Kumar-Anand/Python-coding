import openpyxl
import pandas as pd
import os


print ("hellow user.")
print('your current directry is ')
a=os.getcwd()
print(a)


print ("please entre the path ")
path = str(input())

print ("entre the file name")
name =str(input())
file_path=path + "/" + name
wb=openpyxl.load_workbook(file_path)

print('your workbook name is ')
print(wb)

print('CHOOSE SHEETS')
s=wb.sheetnames()
print(s)

user_input=input()
sheet=wb.get_sheet_by_name(user_input)
S=sheet.title
print(s)