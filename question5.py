'''
Find out pairs with given sum value of an array 
array=[5,7,4,3,9,8,19,21]
sum=17                                          
'''

def twosum(arr,sum1):
    arr.sort()
    left=0
    right=len(arr)-1
    
    while(left<=right):
        if (arr[left]+arr[right]>sum1):
            right=right-1
        elif (arr[left]+arr[right]<sum1):
            left=left+1
        elif (arr[left]+arr[right]==sum1):
            print("Values are: ",arr[left],arr[right])
            left=left+1
            right=right-1

arr=[5,7,4,3,9,8,19,21]
sum1=17

twosum(arr,sum1)
    

