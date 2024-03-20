''' 
Write a Python Program  to find common letters between two strings
eg- NAINA  REENE 
Ans- N
'''


s1=input("write first word : ")
s2=input("write Second word : ")

str1=set(s1)
str2=set(s2)

common= str1 & str2
print(common)