import random

print("\nPlease choose as per given key : 1 for stone , 2 for paper , 3 for scissors")

Computer = random.choice([1,2,3])

user = int(input("Enter your choice : "))
youdict = {1:"Stone",2:"Paper",3:"Scissors"}

if(user not in [1,2,3]):
    print("Invalid input!")
else:
    print(f"Computer chose {youdict[Computer]} and You chose {youdict[user]}")

if(Computer == user):
    print("Its a Draw!")
elif(Computer == 1 and user == 2):
    print("You win!")
elif(Computer == 1 and user == 3): 
    print("You lose!")
elif(Computer == 2 and user == 1):
    print("You lose!")
elif(Computer == 2 and user == 3):
    print("You win!")
elif(Computer == 3 and user == 1):
    print("You win!")
elif(Computer == 3 and user == 2):
    print("You lose!")

