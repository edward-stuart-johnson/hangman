import random

word_list = ["tomato", "apple", "banana", "orange", "mango"]

print(word_list)

word = random.choice(word_list) # chooses a word at random from the word_list

print(word)

guess = input("Please enter a single letter: ") # asks user to guess a letter

if len(guess) == 1 and guess.isalpha(): # checks if the length of the input is equal to 1 and the input is alphabetical:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")