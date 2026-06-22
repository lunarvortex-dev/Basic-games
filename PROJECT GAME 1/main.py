import random

print("\nPlease choose as per given key : 1 for stone , 2 for paper , 3 for scissors")

Computer = random.choice([1,2,3])

user = int(input("Enter your choice : "))
youdict = {1:"Stone",2:"Paper",3:"Scissors"}

wins = {1: 3, 2: 1, 3: 2}

if user not in [1, 2, 3]:
    print("Invalid input!")
else:
    Computer = random.choice([1, 2, 3])

    print(f"Computer chose {youdict[Computer]} and You chose {youdict[user]}")

    if user == Computer:
        print("It's a Draw!")

    elif wins[user] == Computer:
        print("You win!")

    else:
        print("You lose!")
