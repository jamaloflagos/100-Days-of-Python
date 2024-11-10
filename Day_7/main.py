import random

word_list = ['boy', 'girl', 'female', 'male']
display = []
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

for _ in range(word_length):
    display.append("_")  

end_of_game = False 

while not end_of_game:   
    guessed_letter = input("Guess a letter: ").lower()

    if guessed_letter in display:
        print(f"You have already guessed the letter {guessed_letter}")
        
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = letter

    if guessed_letter not in chosen_word   : 
        lives -= 1

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")
    
    if lives == 0:
        end_of_game = True
        print("You lose")