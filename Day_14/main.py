import random
import os

clear = lambda: os.system('cls')
data = [{
    'name': 'Ronaldo',
    'follower_count': 123,
    'description': 'Footballer',
    'country': 'Portugal'
},
{
    'name': 'Ronal',
    'follower_count': 13,
    'description': 'Footballer',
    'country': 'Portugal'
},
{
    'name': 'Ronald',
    'follower_count': 143,
    'description': 'Footballer',
    'country': 'Portugal'
},
{
    'name': 'Rona',
    'follower_count': 23,
    'description': 'Footballer',
    'country': 'Portugal'
},]

def check_answer(guess, account_a, account_b):
    if account_a > account_b:
        return guess == 'a'
    elif account_b > account_a: 
        return guess == 'b'

score = 0
account_b = random.choice(data)

game_should_continue = True
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}")
    print("VS")
    print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}")
    guess = input("Who has more follower? Type \'A\' or \'B\'.").lower()
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess=guess, account_a=a_follower_count, account_b=b_follower_count)

    clear()

    if is_correct:
        score += 1
        print(f"You are right. Current score: {score}")
    else:
        game_should_continue = False
        print(f"You are wrong. You final score: {score}")