import random
import hangman_words
import hangman_art
stages=hangman_art.stages
lives=6
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
placeholder=""
blank=len(chosen_word)
for i in range(blank):
    placeholder+="-"
print(placeholder)
game_over=False
correct_letter=[]
while not game_over:
    print(f"****** {lives}/6Lives ******")
    guess = input("Guess a letter: ").lower()
    if len(guess)>1:
        print("Sorry, only one letter can be guessed")
    else:
            if guess in correct_letter:
                print(f"You've already guessed the letter{guess}")
            display=""
            for letter in chosen_word:
                if letter == guess:
                    display+=letter
                    correct_letter.append(guess)
                elif letter in correct_letter:
                    display+=letter
                else:
                    display+="-"
            print(display)
            if guess not in chosen_word:
                lives-=1
                print("WRONG :) ----- You lose a life")
                print(stages[lives])
            if lives==0:
                print(f"Game over , The word was {chosen_word}")
                print(stages[lives])
                game_over=True
            if "-" not in display:
                game_over=True
                print(f"You guessed the word {display}")
                print("You Win !")
