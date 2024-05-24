#hard_password_generator using python
import random

#creating a list of required symbols ,letters and numbers
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Hey! there you took right choice to protect your account :)")

no_letters = int(input("how many letters you want? \n"))
no_numbers = int(input("how many numbers you want? \n"))
no_symbols = int(input("how many symbols you want? \n"))

password = []

for word in range(1,no_letters):
    password.append(random.choice(letters))

for word in range(1,no_numbers):
    password.append(random.choice(numbers))

for word in range(1,no_symbols):
    password.append(random.choice(symbols))

#shuffling words in a list in random manner
 
random.shuffle(password)

new_password = ""

for word in password:
    new_password += word

print(f"Your strong Password is: {new_password}")