def game(num):
    my_list=[]
    my_list.append(int(num % 10))
    my_list.append(int(num / 10))   
    result=max(my_list[0],my_list[1])-min(my_list[0],my_list[1])
    return result
print(game(int(input("num:"))))



def game1(num):
    my_list=[]
    while (num):
        a=int(num % 10)
        my_list.append(a)
        num = int(num / 10)
    print(my_list)     
    result=max(my_list[0],my_list[1])-min(my_list[0],my_list[1])
    return result
print(game1(int(input("num:"))))