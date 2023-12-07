from bag import Bag


class Hand:
    def __init__(self, bag: Bag):
        self._letters = bag.generate_hand()

    @property
    def letters(self):
        return self._letters

    def __str__(self):
        return "| " + " | ".join(self.letters) + " |"

    def remove_letter(self, number):
        self._letters[number - 1] = "_"

    def get_letter(self, number):
        letter = self.letters[number - 1]
        return letter
