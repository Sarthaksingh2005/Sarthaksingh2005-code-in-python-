#creating list#
numbers=[10,20,30,40,50]
print("original list:",numbers)

#indexing and slicing#
print("first:",numbers[0])
print("last",numbers[-1])
print("revrse",numbers[::-1])

#update element
numbers[2]=35
print("updated list:",numbers)

#add element
numbers.append(60)
numbers.insert(2,25)
numbers.extend([70,80])#add multiple element
print("after addition",numbers)

#remove element
numbers.remove(25)
popped=numbers.pop()
del numbers[1]
print("after removal",numbers)
print("popped element",popped)

#searching
print("sorted list",40 in numbers)
print("is 100 not there in list?",100 not in numbers)

#7.sorting and reversing
numbers.sort()
print("sorted list",numbers)
numbers.sort(reverse=True)
print("decending order",numbers)
numbers.reverse()
print("reversed list:",numbers)

#copying
copy_list=numbers.copy()
print("copied list:",copy_list)

#9 nested list
nested=[[1,2,3],[4,5,6]]
print("nested list:",nested)
print("access nested element [1][2]",nested[1][2])

# final list
print("final list",numbers)



