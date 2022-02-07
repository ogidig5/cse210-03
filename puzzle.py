import random
from puzzle_2 import main_2
#TODO: Add a check to see if the player got the word right
#TODO: Replace some of the wording in the code so it says what our instructor is asking us
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
        self._guesses_left = 15
        self._guesses_allowed = 15
    def guess_word(self):
        print("The number of letters are: ", len(self._puzzle._word))
        print("The first letter is: ", self._puzzle._word[0], "\nAnd the last one is: ",self._puzzle._word[-1])
        self._guess = input("\nEnter a letter: ")
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
#TODO: Add a check to see if the player got the word right
                if self._guesses in self._puzzle._word:
                    print("You got it!")
                    print(self.display_word())
                    break
                break

def main():
    obj1 = Puzzle()
    player = Player()
    player.play_game()

print("Welcome to the word game!")
print("\nThere are multiple rooms, which one do you want to go to?(1/2) ")
print("Just remember, room 1 has thousands of words, room 2 has only ten words.")
choice = input("\nEnter 1 or 2: ")

if choice == "1":
    print("You are in room 1")
    print("You have over four hundred thousand words to guess.")
    print("You have 15 guesses.")
    print("You can only guess one letter at a time.")
    print("Good luck!")
    main()

elif choice == "2":
    print("You are in room 2")
    print("You have ten words to guess.")
    print("You have 15 guesses.")
    print("You can only guess one letter at a time.")
    print("Good luck!")
    main_2()

