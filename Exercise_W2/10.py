

#الف
message="Babak Khorramdin"
a=message[0]
print(a)
#ب
b=message[4]
print(b)
#پ
message_list=message.split()
b=message_list[0]
c=message_list[1]
print(b , c )
#ت
d=message[0:12:2]
print(d)

#د
for char in message:
    if char=="m":
        print('TRUE')
        break

print(message.find("k"))




#نمایش وارونه یک رشته 
name="Sara Nasiri"
name_index=len(name)
while name_index>0:
    revers_name=name[name_index-1]
    print(revers_name ,end=" ")
    name_index=name_index-1

