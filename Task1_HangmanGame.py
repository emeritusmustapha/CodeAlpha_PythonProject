import random

word_list = ["python", "hangman", "developer", "internship", "codealpha"]

word = random.choice(word_list).lower()
guessed_letters = []
attempts_left = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.\n")

while attempts_left > 0:
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    
    print(f"Word: {display}")
    print(f"Attempts left: {attempts_left}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    
    guess = input("Guess a letter: ").strip().lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue
    
    guessed_letters.append(guess)
    
    if guess in word:
        print("Good guess!\n")
    else:
        attempts_left -= 1
        print(f"Wrong guess! '{guess}' is not in the word.\n")
    
    if all(letter in guessed_letters for letter in word):
        print(f"Congratulations! You guessed the word: {word}")
        break
else:
    print(f"Game over! The word was: {word}")

print("Thanks for playing!")
