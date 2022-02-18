for i in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    a.sort()
    for k in range(n//2):
        print(a[k],a[0])