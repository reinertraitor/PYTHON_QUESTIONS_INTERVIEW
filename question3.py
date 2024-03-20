'''
Write a python program  to count the frequeny of the words appearing in the string '''

def frq_words():
    str1=input("Give a string")

    li=str1.split()
    d={}

    for i in li:
        if i not in d.keys():
            d[i]=0
        d[i]=d[i]+1 

    print(d)   


frq_words()