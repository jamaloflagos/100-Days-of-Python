import string
import random
uppercase_letters = list(string.ascii_uppercase)
lowercase_letters = list(string.ascii_lowercase)
uppercase_letters.extend(lowercase_letters)
letters = uppercase_letters
numbers = list(string.digits)
symbols = list(string.punctuation)
password_list = []
password = ""

print("Welcome to PyPassword Generator")
amount_of_letters = int(input("How many letters would you want in your password?\n"))
amount_of_numbers =int(input("How many numbers would you want?\n"))
amount_of_symbols =int(input("How many symbols would you want?\n"))


for char in range(0, amount_of_letters):
    password_list.append(random.choice(letters))

for char in range(0, amount_of_numbers):
    password_list.append(random.choice(numbers))

for char in range(0, amount_of_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)


for char in password_list:
    password += char

print(f"Your password is: {password}")