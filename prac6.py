#1.create dictionary
student={"name":"Alice","age":20,"marks":85}
print("original dicitonary: ",student)

#2. acess values 
print("name:",student["name"])
print("age",student.get("age"))

#3.add/update/remove
student["grade"]="A"
student["marks"]=90
student.pop("age")
print("after modification",student)

#4.dictnory methods
print("keys:",student.keys())
print("values",student.values())
print("items",student.items())

#5 loop through dictonary
for key,value in student.items():
    print(key,":",value)

#6 nested dictnory
students={
    1:{"name":"Alice","marks":90},
    2:{"name":"bob","marks":75}
}
print("nested dictonay:",students)
print("access bob's marks:",students[2]["marks"])

#7 copy dictnory
copy_student=student.copy()
print("copied dictnory:",copy_student)
