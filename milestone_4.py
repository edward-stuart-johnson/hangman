class Hangman():

    def __init__(self, word_list, num_lives=5):
        import random

        self.word_list = list(word_list) # A list of words
        self.word = random.choice(word_list) #The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script
        self.word_guessed = list(["_"] * len(word)) # A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
        self.num_letters = int(len(set(word))) # The number of UNIQUE letters in the word that have not been guessed yet
        self.num_lives = int(num_lives) # The number of lives the player has at the start of the game.
        self.list_of_guesses = list() #[,] # A list of the guesses that have already been tried. Set this to an empty list initially

    def check_guess(self, guess):
        guess = guess.lower() #Convert the guess into lower case.
        if guess in self.word: # check whether guessed letter is in word at all
            print(f"Good guess! {guess} is in the word.")
            for letter_position in range(len(word)): # go through each position in the word to check if an "_" must be replaced by the successfully guessed letter
                if self.word[letter_position] == guess:
                    self.word_guessed[letter_position] = guess
            # print(self.word_guessed)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("I am thinking of a word. Please guess a letter in the word: ") # asks user to guess a letter

            if len(guess) > 1 or guess.isalpha() == False: # checks if the length of the input is equal to 1 and the input is alphabetical:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess) # append the guess to the list_of_guesses


if __name__ == '__main__':
    import random
    word_list = ["banana"] #,"tomato", "apple",  "orange", "mango"]

    print(word_list)
    word = random.choice(word_list)
    print(word)

    print("running Hangman...")

    current_game = Hangman(word_list)

    current_game.ask_for_input()