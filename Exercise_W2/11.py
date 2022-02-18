import random
computer_choice=random.randint(1,20)
user_coice=int(input("enter a number:"))
step=1
while  step<5:
    if computer_choice==user_coice:
        print("great! you win! computer choice is",computer_choice,"too" )
        break
    if computer_choice!=user_coice:
        print (" not correct! you have one more chance:") 
        user_coice=int(input("enter another number:"))
        step+=1
if step==5:
    print("you lose :( the answer is :", computer_choice) 
  





