import random

print("This is a Password generator")
Chars=("abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

number=int(input("Amount of passwords you want to generate: "))

length=int(input("Enter your password length: "))

print("Here are your passwords :   ")

for passwords in range(number):
    password=""
    for c in range (length):
        password += random.choice(Chars)
    print(password)