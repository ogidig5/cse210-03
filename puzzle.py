import random

class Word:
    def __init__(self):
        words = ["ace", "books", "chest"]
        self._word = random.choice(words)
class Puzzle(Word):
    def __init__(self):

        # Calling constructor of the word class
        Word.__init__(self)
        print("Calling protected member of base class: ",
            self._word)

obj1 = Puzzle()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protedted member of obj1: ", obj1._word)

