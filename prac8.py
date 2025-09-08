#list comprehension
words=["apple","banana","orange","cherry","blueberry"]

1.#convert list of strings to uppercase
upper_words=[word.upper() for word in words]
print("upper case:",upper_words)

#2.list comprehension with if condition
len_word=[word for word in words if len(word)>5]
print("answer:",len_word)

#list comprehension with if else condition
word_list = [word.upper() if len(word) > 5 else word.lower() for word in words]
print("Words Label:", word_list)


#4.nested list comprehension
#                //expression      //outer loop     //inner loop
multipication_table=[[i*j for j in range(1,4)] for i in range(1,4)]
print("multipication table:",multipication_table)

#5 flatten a 2d list

flat_list=[num for row in multipication_table for num in row]
print("flateen list:",flat_list)
