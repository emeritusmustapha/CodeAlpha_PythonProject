import random

words = ["python", "hangman", "developer", "internship", "codealpha"]

chosen_word = random.choice(words)
guessed = []
tries = 6

print("Let's play Hangman!")

while tries > 0:
    hidden = ""
    for letter in chosen_word:
        if letter in guessed:
            hidden += letter + " "
        else:
            hidden += "_ "
    
    print("\nWord:", hidden)
    print("Tries left:", tries)
    print("Letters guessed:", guessed)
    
    guess = input("Guess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Just one letter please")
        continue
    
    if guess in guessed:
        print("You already tried that one")
        continue
    
    guessed.append(guess)
    
    if guess in chosen_word:
        print("Yeah, that's in there")
    else:
        tries -= 1
        print("Nope, not in the word")
    
    all_good = True
    for letter in chosen_word:
        if letter not in guessed:
            all_good = False
            break
    
    if all_good:
        print("\nYou got it! The word was", chosen_word)
        break

if tries == 0:
    print("\nYou lost. The word was", chosen_word)

print("Game over")
