from bag import Bag


class Hand:
    """
    :param letters: letters in hand
    :type letters: list
    """

    def __init__(self, bag: Bag):
        self._bag = bag
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

    def replace_letter(self, new_letter, index):
        self._letters[index] = new_letter

    def draw_to_seven_letters(self):
        for letter in self.letters:
            if letter == "_":
                new_letter = self._bag.draw_letter()
                letter = new_letter
