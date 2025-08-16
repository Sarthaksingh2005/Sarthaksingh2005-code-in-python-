"""
#gcd#
import math
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)


a=int(input("enter a number: "))
b=int(input("enter a number: "))
print("the gcd is: ",gcd(a,b))
"""
#amstrong number#
import math

def am(a):
    # count digits
    temp = a
    c = 0
    while temp > 0:
        c += 1
        temp //= 10

    # calculate Armstrong sum
    temp = a
    num = 0
    while temp > 0:
        d = temp % 10
        num += math.pow(d, c)
        temp //= 10

    return num

x = int(input("Enter number: "))
res = am(x)
if res == x:
    print("Armstrong number")
else:
    print("Not Armstrong number")





def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # check divisors up to sqrt(n)
        if n % i == 0:
            return False
    return True

# Example usage
x = int(input("Enter a number: "))
if is_prime(x):
    print(x, "is a Prime number")
else:
    print(x, "is NOT a Prime number")




def print_divisors(n):
    print(f"Divisors of {n} are:", end=" ")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
    print()

# Example usage
x = int(input("Enter a number: "))
print_divisors(x)
