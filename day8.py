"""import random
choices=["rock", "paper", "scissors"]
while True:
    
    user_choice=input("Enter rock, paper, or scissors : ").lower()
    if user_choice == "quit":
        print("Thanks for playing!")
       break
    #if user_choice not in choices:
      #  print("Invalid choice. Please try again.")
     #   continue
    #computer_choice=random.choice(choices)
    #print(f"Computer chose: {computer_choice}")
    #if user_choice == computer_choice:
     #   print("It's a tie!")
    #elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
     #   print("You win!")   
        
    #else:
     #   print("Computer wins!")"""
        
        
  #tuple=double hunxa 
  #set=unique hunxa set ma duplicate value hunna
""""a= (1, 2, 3, 4, 5)
print(type(a))
print(a[0])

b=list(a)#tuple lai list ma convert grnee
print(b)
b[0]=100
a=tuple(b)
print(a) """
""""data={1,2,3,"hello","testing",5,1,1}
print(data)"""
#pydandic v2
#Function Classssssssssss   hami le fuction banauda print bhitra nagrne 

""""def test():
   # a=10
    #print("This is the value of a", a)
    print("bad habits")
    return [1,2,3,4,5],[6,7,8,9,10]
print(test())"""
""""def sum_of_list():
    a=[1,2,3,4,5]
    total=0
    for i in a:
        total=total+i
    return total
print(sum_of_list())"""
""""def check_number(num):
    if num%2==0:
        return "Even" #returntype  same  grnu prxa
    else:
        return "Odd"
result=check_number(10)
print(result)


result=check_number(15)
print(result)    """
num=[1,2,3,4,10,5,6,7,8,9]
"""def max_number(num):
    max_num=num[0]
    for i in num:
        if i>max_num:
            max_num=i
    return max_num
print(max_number(num))"""

def max_find(a,b,c):
    if a>=b and  a>=c:
      return(a)
    elif b>=a and b>=c:
        return(b)
    else:
        return(c)
print(max_find(5,9,7))    


     
    
    
    




