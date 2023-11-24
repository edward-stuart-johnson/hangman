import random

word_list = ["tomato", "apple", "banana", "orange", "mango"]

print(word_list)

word = random.choice(word_list) # chooses a word at random from the word_list

print(word)

def ask_for_input():
    while True:
        guess = input("I am thinking of a word. Please guess a letter in the word: ") # asks user to guess a letter

        if len(guess) == 1 and guess.isalpha(): # checks if the length of the input is equal to 1 and the input is alphabetical:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

def check_guess(guess):
    guess = guess.lower() #Convert the guess into lower case.
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

ask_for_input()