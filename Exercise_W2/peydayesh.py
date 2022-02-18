


def find(num1, num2, num3):
    my_list=[]
    my_list.append(num1)
    my_list.append(num2)
    my_list.append(num3)
    for i in range(1,5):
        if i not in my_list:
            missed_number=i
    return missed_number
num1,num2,num3 = map(int,input().split())    
print(find(num1,num2,num3)) 

