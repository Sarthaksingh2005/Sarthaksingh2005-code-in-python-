#set
fruit={"apple","banana","cherry"}
print("original set:",fruit)

#2. add,remove element
fruit.add("orange")
fruit.remove("banana")
fruit.discard("grape")
print("after process: ",fruit) 

#3.set operation
a={1,2,3,4,}
b={3,4,5,6}
print("union",a|b)
print("intersection",a&b)
print("difference",a-b)
print("symmetric difference",a^b)

#4 membership
print("is 2 in set a?",2 in a)
print("is 7 not in set b?",7 not in b)

#5 built in function
nums={10,20,30,40,50}
print("length:",len(nums))
print("min:",min(nums))
print("max:",max(nums))
print("sum:",sum(nums))

#6.copy set
nums_copy=nums.copy()
print("copied set:",nums_copy)

#7 frozen set
frozen=frozenset([1,2,3])
print("frozen set",frozen)