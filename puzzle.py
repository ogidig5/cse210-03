import random

class Word:
    def __init__(self):
        fileObject = open("list_words.txt", "r")
        data = fileObject.read()
        self._word = random.choice(data.split())
class Puzzle(Word):
    def __init__(self):

        # Calling constructor of the word class
        Word.__init__(self)
       
class Player:

    def __init__(self):
        self._puzzle = Puzzle()
        self._guess = ""
        self._guesses = []
        self._guesses_left = 6
        self._guesses_allowed = 6
    def guess_word(self):
        self._guess = input("Enter a letter: ")
        self._guesses.append(self._guess)
    def check_guess(self):
        if self._guess in self._puzzle._word:
            print("Correct!")
        else:
            print("Incorrect!")
            self._guesses_left -= 1
    def display_word(self):
        print("The word is: ", self._puzzle._word)
    def display_guesses(self):
        print("Your guesses: ", self._guesses)
    def display_guesses_left(self):
        print("Guesses left: ", self._guesses_left)
    def play_game(self):
        while self._guesses_left > 0:
            self.guess_word()
            self.check_guess()
            self.display_guesses()
            self.display_guesses_left()
            if self._guesses_left == 0:
                print("\nYou lost!")
                print(self.display_word())
                break
            if self._guess == self._puzzle._word:
                print("\nYou won!")
                print(self.display_word())
                break

obj1 = Puzzle()
obj2 = Player()
obj2.play_game()

