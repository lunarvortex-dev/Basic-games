import random

computer = random.randint(0, 100)
step = 0

while True:
    user1 = int(input("Enter your number (0-100): "))

    if user1 < 0 or user1 > 100:
        print("Enter your choice in the valid range!")
        continue

    step += 1

    if user1 == computer:
        print("You have guessed it perfectly!")
        print(f"You guessed the number in {step} steps.")
        break
    elif user1 > computer:
        print("Lower number please!")
    else:
        print("Higher number please!")
