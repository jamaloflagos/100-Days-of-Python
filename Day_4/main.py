import random
user_choice = int(input("What do you choose? Type for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0, 2)
print(computer_choice)
# 0 for rock 1 for paper 2 for scissors
if user_choice == 0:
    if computer_choice == 0:
        print("The computer chose rock. It\'s a draw!")
    elif computer_choice == 1:
        print("The computer chose paper. You lose the game!")
    elif computer_choice == 2:
        print("The computer chose scissors. You win the game!")
elif user_choice == 1:
    if computer_choice == 0:
        print("The computer chose rock. You win the game!")
    elif computer_choice == 1:
        print("The computer chose paper. It\s a draw!")
    elif computer_choice == 2:
        print("The computer chose scissors. You lose the game!")
elif user_choice == 2:
    if computer_choice == 0:
        print("The computer chose rock. You lose the game!")
    elif computer_choice == 1:
        print("The computer chose paper. You win the game!")
    elif computer_choice == 2:
        print("the computer chose scissors. It\'s a draw!")
else:
    print("You chose a wrong number. Choose the right number, 0, 1 or 2.")