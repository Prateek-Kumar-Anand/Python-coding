import openpyxl
print ("hellow user.")
print ("please entre the path ")
path = str(input())
print ("entre the file name")
name =str(input())
file_path=path + "/" + name
wb=openpyxl.load_workbook(file_path)
print(wb)
print("do you want to add a sheet")
addingsheet=input()
if addingsheet== 'yes':
    wb.create_sheet(addingsheet)
else :
    print("okay sir")
print ("work done")