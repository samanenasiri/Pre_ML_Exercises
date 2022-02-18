def my_multiple(x,y):
    a,m=1,0
    while a<=y:
        m+=x
        a+=1
    return m 
print(my_multiple(int(input("x:")),int(input("y:"))))      

