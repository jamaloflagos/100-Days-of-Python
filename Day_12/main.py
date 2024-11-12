import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too Low.")
        return turns - 1
    else:
        print(f"You got it. The answer was {answer}")

def set_difficulty():
    difficulty_level = input("Choose a difficulty level. Type \'easy\' or \'hard\': ").lower()

    if difficulty_level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
def game():
    answer = random.randint(1, 100)
    print(answer)
    print("Welcome to the Number Playing Game.")
    print("I am thinking of a number between 1 and 100.")
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess=guess, answer=answer, turns=turns)

        if turns == 0:
            print("You\'ve run out of attempts, you lose.")
            return
        elif guess != answer:
            print("Guess again")

game()