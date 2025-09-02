'''1.reverse a string
def ulta(sen):
 return sen[::-1]
sen=input("enter the word:")
print("reverse:",ulta(sen))


"2.check if string is palindrome"
def check(s):
 return s==s[::-1]
print(check("nitin"))
print(check("rahul"))


"3.count vowel in a string"
def cc(s):
 c=0
 vowel="aeiouAEIOU"
 for char in s:
   if char in  vowel:
    c=c+1
 return c
print(cc("programmimg"))
'

'find frequency of each character'
def ff(s):
    fre={}
    for char in s:
        fre[char]=fre.get(char,0)+1
    return fre
print(ff("banana"))
'''

    