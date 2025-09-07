#String manipulation
name="lackross josu"
age=20
print(f"I am {name}and i am {age} yers old")

#2.string split
sentence="python is a very powerfull language"
words=sentence.split()
print("result=",words)

#3.join()
joined_sentence="|".join(words)
print("joined words:",joined_sentence)

#4.advance slicing
numbers=list(range(1,21))

#(a) every sec element
sec=numbers[::2]
print("every 2nd element:",sec)

#(b)last 5 element in reverse
ll=numbers[-1:-6:-1]
print("last number:",ll)

#(c) element from index 5 to 15
kk=numbers[15:4:-1]
print("result:",kk)