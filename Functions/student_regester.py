Student=[ ]
while True :
    print ('Enter ' + str(len(Student) +1) + ' student name or nothing to stop')
    name = input()
    if name == '' :
       break
    Student = Student + [name]
print('Student names are ')
for name in Student :
    print(' '+ name)