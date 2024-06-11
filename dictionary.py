#dictionary
student={
    "name":"George",
    "reg_no" : 145,
    "Age" : 12,
    "email": "George@gmail.com"
}
print (student.items())
for x in student.keys():
    print (x)
for value in student.values():
    print (value)
for key, value in student.items():
    print (key,value)
print (student)

