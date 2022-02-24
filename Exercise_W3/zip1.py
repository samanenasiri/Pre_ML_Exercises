a=[1,2,3,4,5,6]
b=(7,8,9)
c=[10,11]
d=(12,13,14,15,16)


def my_zip(*n) :
    min_len= len(n[0])
    for i in n:
        if len(i) < min_len:
            min_len = len(i)   
    index=0
    list1=[]
    while index<min_len:
        list2=[]
        for i in n:
            list2.append(i[index])    
        list1.append(list2)    
        index+=1 
    return list1              
print(my_zip(a,b,c,d))