''' find the missing number in the array '''

def number(a):
    
    n=a[-1]
    total= n*(n+1)//2
    sum2=sum(a)

    Result=total-sum2
    print("missing number is: ",Result)

a=[1,2,4,5,6,7]
number(a)