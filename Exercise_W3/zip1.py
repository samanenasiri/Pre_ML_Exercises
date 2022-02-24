
def my_zip(*n) :
    min_len= len(n[0])
    for i in n:
        if len(i) < min_len:
            min_len = len(i)   
    count=0
    list1=[]
    while count<min_len:
        my_list=[]
        for i in n:
            my_list.append(i[count])
        list1.append(my_list)    
        count+=1 
    return list1              
a=[1,2,3,4,5,6]
b=(7,8,9)
c=[10,11]
d=(12,13,14,15,16)

print(my_zip(a,b,c,d))