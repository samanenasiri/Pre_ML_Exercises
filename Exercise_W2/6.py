def multi4():
    my_list=[]
    for i in range(22,106):
        if i%4==0:
            my_list.append(i)
    return my_list        
print(multi4()) 