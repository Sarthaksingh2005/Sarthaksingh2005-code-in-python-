"""
name = "Sarthak"
age = 21
print(f"My name is {name} and I am {age} years old.")  # f-string




#to reverse a string#
s=" the lackross josu"
print(s[ ::-1])




#input a list#
n=int(input("enter number of element: "))
list=[]

for i in range(n):
    val=(input(f"enter the element{i+1}: "))
    list.append(val)

print("your list=",list)





#using loop to process element of a list#
n = int(input("Enter the number of elements: "))
original = []
squared = []

for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    original.append(val)
    squared.append(val ** 2)

print("Original list:", original)
print("Squared list:", squared)



#loop in one line#
num=[x for x in range(1,6)]
print(num)

sq=[x**2 for x in range(1,6)]
print(sq)


#nested loop with list
matrix=[]
for i in range(3):
    rows=[]
    for j in range(3):
        rows.append(i*j)
    matrix.append(rows)

print(matrix)
"""