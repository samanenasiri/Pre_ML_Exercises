for i in range(int(input())):
    M=input("your string contains 0 ,1:")
    z=M.count("0")
    print(z)
    o=M.count("1")
    print(o)
    if z<o :
        print(M.replace("1","-"))
        print (min(z,o))   
    if z>o:
        print(M.replace("0","-"))  
        print (min(z,o))   
    if z==o:
        print (0)     


        
for i in range(int(input())):
    M=input()
    z=M.count("0")
    o=M.count("1")
    if z==o:
        print (0)  
    else:
        print (min(z,o))   
   