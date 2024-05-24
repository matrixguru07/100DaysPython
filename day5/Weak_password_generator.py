import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# welcoming text

print("\n Hey there welcome!! this is password generator: \n")

no_letters = int(input("How many letters you want?\n "))
no_symbols = int(input("How many symbols you want?\n "))
no_numbers = int(input("How many numbers you want?\n "))

password = ""

for x in range(1,no_letters+1):
    password += random.choice(letters)

for x in range(1,no_symbols+1):
    password += random.choice(symbols)
    
for x in range(1,no_numbers+1):
    password += random.choice(numbers)

    
print(f"Your password is: {password}")
print("Thanks for using :) ")
