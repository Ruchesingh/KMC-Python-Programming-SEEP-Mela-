import random
#print(random.random()*100)
#print(random.randint(10,20))
#a=["Ruchee", "Suman", "Sujan", "Ram", "Shyam"]
#print(random.choice(a)) 

# Guesssing the number game
#count=0
#number=random.randint(10,20)
#while True:
    #guess=int(input("Enter the number between 10 and 20: "))
    #count+=1
    #if guess==number:
        #print(f"Congratulations! You guessed the number in {count} attempts.")
        #play_again=input("Do you want to play again? (yes/no): ")
        #if play_again.lower()=="yes":
         #   number=random.randint(10,20)
        #    count=0
       # else:
      #      print("Thank you for playing!")
     #       break
        
    #else:
        #print("Wrong guess. Try again!")
   # guess=int(input("Enter the number between 10 and 20: "))
   # count+=1
   # if guess==number:
       # print("You want to paly again? (yes/no)")
       # play_again=input()
       # if play_again.lower()=="yes":
           # number=random.randint(10,20)
           # count=0
       # else:
           # print("Thank you for playing!")
           # break
           
           
#guess_attempts=5
#number=random.randint(10,20)
#while guess_attempts>0:
 #   guess=input("Enter the number between 10 and 20: ")
  #  if guess==number:
   #     print(f"Congratulations! You guessed the number in  attempts.")
    #    break
    #else:
     #   guess_attempts-=1
      #  print(f"Wrong guess. You have {guess_attempts} attempts left.")
#if guess_attempts==0:
 #   print(f"Game over! The correct number was {number}.")   
 
#games_data=["r","p","s"]
#data=random.choice(games_data)
#print(data)

#while True:
 #   user_data=input("Enter r,p,s: ")
  #  if user_data==data:
   #     print("Draw!")
    #elif (user_data=="r" and data=="s") or (user_data=="p" and data=="r") or (user_data=="s" and data=="p"):
     #   print("You win!")
    #else:
     #   print("You los

user_score = 0
computer_score = 0

rounds = 3

print(" Game: Higher Number Wins")

for i in range(rounds):
    print(f"Round {i+1}")
    
    user = int(input("Enter a number between 1 and 10 : "))
    computer = random.randint(1, 10)
    
    print("Computer chose:", computer)

    if user > computer:
        print("You win this round!")
        user_score += 1
    elif computer > user:
        print("Computer wins this round!")
        computer_score += 1
    else:
        print("Draw!")

print(" Final Score")
print("You:", user_score)
print("Computer:", computer_score)

if user_score > computer_score:
    print(" You are the winner!")
elif computer_score > user_score:
    print(" Computer wins!")
else:
    print("It's a tie!") 
     

 

    
           
        
        
        
        
        
        
        
        