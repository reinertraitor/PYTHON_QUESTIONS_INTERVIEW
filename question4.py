'''
Write a python program to convert two lists into dictionary
 '''


def list_to_dict():
    key=[1,2,3]
    values=["a","b","c"]

    result=dict(zip(key,values))
    print(result)

list_to_dict()

def dict_to_tuple():
    
    x={1: 'a', 2: 'b', 3: 'c'}
    for i in x.items():
        print(i)

dict_to_tuple()

