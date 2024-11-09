print("Welcome to to Treasure Island.")
print("Your mission is to find treasure.")
choice1 = input("You\'re at a cross road. Where do you want to go? Type \"left\" or \"right\".\n").lower()
if choice1 == 'left':
    choice2 = input("You came to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. type \"swim\" to swim across.\n").lower()
    if choice2 == 'swim':
        print("Game Over.")
    else:
        choice3 = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose?\n").lower()
        if choice3 == "yellow":
            print("You found the Treasure.")
        elif choice3 == "red" or choice3 == "blue":
            print("Game Over.")
        else:
            print("You chose a door that does not exist. Game Over.")
else: 
    print("Game Over.")