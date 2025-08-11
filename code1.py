"""
# Count digits in a number


num = int(input("Enter a number: "))


num = abs(num)

count = 0


if num == 0:
    count = 1
else:
    while num > 0:
        num //= 10  
        count += 1

print("Number of digits:", count)

#reverse a number
num=int(input("enter a number"))
rev=0
while num>0:
    d=num%10
    rev=rev*10+d
    num=num//10

print("the reverse is:",rev)

 
#check palindrome
n=int(input("enter a number: "))
temp=n
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
if temp==rev:
 print("number is palindrome")
else:
    print("not palindrome")

"""
