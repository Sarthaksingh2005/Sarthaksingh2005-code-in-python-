#file handling
import os
#create and write to a file
with open("sample.txt","w") as file:
    file.write("hello,this is first line")
    file.write("this is second line")
print("file created and written")

#read the whole file
with open("sample.txt","r") as file:
    content=file.read()
print("read full content")
print(content)

#append newlines
with open("sample.txt","a") as file:
    file.write("this line was appended")
    file.write("another appended line")
print("new line append")

#read file line by line
print("read file line by line")
with open("sample.txt","r")as file:
    for line in file:
        print(line.strip())

#delete the file
os.remove("sample.txt")
print("file deleted succesfully")