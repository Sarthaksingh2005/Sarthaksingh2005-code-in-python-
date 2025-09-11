#EXCEPTIONAL HANDLING
#try catch block
print("basic try-except block:")
try:
    num=int(input("enter a number:"))
    print("you entered:",num)
except ValueError:
    print("enterd invalid number")




#multiple except block
print("multiple expect block")
try:
    a=int(input("enter a value:"))
    b=int(input("enter value of b: "))
    result=a/b
    print("result",result)
except ZeroDivisionError:
    print("division by 0 is not allowed")
except:
    print("error:please enter a valid integer")




#finally block
print("finally block demostration")
try:
    file=open("simple.txt","w")
    file.write("this is test file")
except Exception as e:
    print("error in writing file")
finally:
    file.close()
    print("file is closed ")





#raise keyword
print("raise custom exception")
def checkpos(n):
    if(n<=0):
        raise ValueError("only a positive number")
    return n
try:
    num=int(input("enter a positive number"))
    checkpos(num)
except ValueError as ve:
    print("custom value",ve)
