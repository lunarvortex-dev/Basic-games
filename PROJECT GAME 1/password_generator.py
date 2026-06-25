import random

alphabet = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "0123456789"
symbols = "!@#$%^&*()-+"

collection = alphabet + numbers + symbols

length = int(input("Enter the length of the password: "))

password = ""
for i in range(length):
    char = random.choice(collection)
    password += char
    
print("Generated Password:", password)
