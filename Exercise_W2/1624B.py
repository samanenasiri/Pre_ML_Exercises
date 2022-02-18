# def is_AP():
#     if abs(a-b)==abs(b-c): 
#         return True
#     else :
#         return False 

# def create_AP():
#     if is_AP==False:
#         for m in range(100):
#             if a<b and a<c:
#                 a=a*m
#                 if is_AP:
#                     result=m,a,b,c
#                     print("m is:",m,"and your AP",a,b,c)

#                     break
#             if b<a and b<c:
#                 b=b*m
#                 if is_AP:
#                     result=m,a,b,c
#                     print("m is:",m,"and your AP",a,b,c)
#                     break 
#             if c<a and c<b:
#                 c=c*m
#                 if is_AP:
#                     result=m,a,b,c
#                     print("m is:",m,"and your AP",a,b,c)
#                     break 
#         return result 
# a, b, c = map(int, input().split())             
# print(create_AP())             





#میشه با فاصله ورودی هاتو چاپ کنی 
#   a, b, c = map(int, input().split())


for i in range(int(input())):
    a, b, c = map(int, input())

    if ((a+c) % (2*b) == 0)  or  (2*b-c > 0 and (2*b-c)%a == 0)  or  (2*b-a > 0 and (2*b-a)%c == 0):
        print("YES")
    else:
        print("NO")

        
