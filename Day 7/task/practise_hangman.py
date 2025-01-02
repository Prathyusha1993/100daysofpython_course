# hangman practise:
import random
from hangman_words import word_list
import hangman_art


lives = 6
print(hangman_art.logo)
chosen_word = random.choice(word_list)
print(chosen_word)

game_over = False
placeholder = ''
for position in range(len(chosen_word)):
    placeholder += '_'
print('Word to guess:' + placeholder)
display = ''
correct_letters = []
while not game_over:
    guess = input('Can you guess the letter: ').lower()

    if guess in correct_letters:
        print(f'you already guessed this letter {guess}')
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print('You lose!')


    if '_' not in display:
        game_over = True
        print('You win!')

    print(hangman_art.stages[lives])