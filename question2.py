'''
Write a python program to count the frequecny of the words appearing in the string

Eg- raaj plays badminton very carefully
 '''
count=0
str1=input("write a sentence: ")
char=input("write the character you want to search: ")

for i in str1:
    if i==char:
        count+=1
    
print(count)