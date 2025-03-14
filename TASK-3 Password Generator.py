import random
import string

def generate_pass(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = " "
    for i in range(length):
        password += random.choice(characters)
    return password

length = input("Enter the required password length : ")

if length.isdigit():
    length = int(length)
    if length > 0:
        password = generate_pass(length)
        print(f"Generated Password : {password}")
    else:
        print("Please enter a positive number...")
else:
    print("Invalid input! Please enter a number...")