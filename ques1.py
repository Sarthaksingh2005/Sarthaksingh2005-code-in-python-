'''functions
1.no argument,no return type'''
def greet():
    print("hello world")    
greet()




"2.with argument,no return type"
def table(n):
    for i in range(1,11):
        print("table=",n*i)
table(5)






'''deafult parameter'''
def give(name="lackross"):
    print("josu",name)
give()
give("the")





""" keyword argument"""
def intro(name,age):
    print(f"my name is {name} and my age is {age}")

intro(name="lackross",age="20")