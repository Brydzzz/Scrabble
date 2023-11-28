from bag import Bag


class Hand:
    def __init__(self, bag: Bag):
        self.letters = bag.generate_hand()

    def __str__(self):
        return "| " + " | ".join(self.letters) + " |"

    def remove_letter(self, number):
        self.letters[number - 1] = "_"

    def get_letter(self, number):
        letter = self.letters[number - 1]
        return letter
