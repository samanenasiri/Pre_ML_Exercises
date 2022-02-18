
for i in range(int(input())):
    a,b,c = map(int,input())
    if (c<b+a) and (b<a+c) and (a<b+c) :
        print("YES")
    else:
        print("NO")    