#tuple#
numbers=(10,20,30,40,50)
print("original tuple",numbers)

#2.indexing and slicing
print("first element",numbers[0])
print("last element",numbers[-1])
print("slicing[1:4]",numbers[1:4])

#concatenation and repitation
new_tuple=numbers+(60,70)
print("after concatenation",new_tuple)
print("repitation (*2)",numbers*2)

#4 membership
print("is 30 in tuple?",30 in numbers)
print("is 100 not in tuple",100 not in numbers)

#5 built in function 
print("length of a tuple:",len(numbers))
print("minimum values:",min(numbers))
print("maximum values:",max(numbers))
print("sum of element",sum(numbers))

#6 Methods
print("length of tuple:",len(numbers))
print("minimum value: ",min(numbers))
print("maximum values:",max(numbers))
print("sum of element:",sum(numbers))

#7 convert to list(modify)
temp_list=list(numbers)
temp_list.append(60)
temp_list[2]=35
numbers=tuple(temp_list)
print("after modification: ",numbers)

#8 nested tuple
nested=((1,2),(3,4,5))
print("nested tuple:",nested)
print("access nested element [1][2]:",nested[1][2])

#9 tuple unpacking 
a,b,c,d,e,f=numbers
print("unpacked values:",a,b,c,d,e,f)

#final tuple
print("final tuple:",numbers)
