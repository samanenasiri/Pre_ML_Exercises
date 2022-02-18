def multi5_notmulti3():
    my_list=[]
    for i in range(20,200):
        if i%5==0 and i%3!=0:
            my_list.append(i)
    return my_list        
print(multi5_notmulti3()) 