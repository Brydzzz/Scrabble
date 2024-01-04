import random
from constants import LETTERS_BAG_COUNT, HAND_EMPTY_LETTER_SYMBOL, HAND_SIZE
from copy import deepcopy


class Bag:
    """
    Attributes
    ----------
    inside: dict
        inside of the bag, dict keys - letters
        and dict values - amount of a letter in a bag
    """

    def __init__(self):
        self._inside = deepcopy(LETTERS_BAG_COUNT)

    @property
    def inside(self):
        return self._inside

    def draw_letter(self):
        """
        Returns randomly drawn letter from bag.
        If letter is not available (its count is 0),
        draws another letter
        If there no letters left in bag
        returns HAND_EMPTY_LETTER_SYMBOL from constans
        """
        if self.get_left() == 0:
            return HAND_EMPTY_LETTER_SYMBOL
        else:
            drawn_letter = random.choice(list(self.inside.keys()))
            while not self.check_letter_availability(drawn_letter):
                drawn_letter = random.choice(list(self.inside.keys()))
            self._inside[drawn_letter] -= 1
            return drawn_letter

    def exchange_letter(self, exchanged_letter):
        """
        Increases exchanged letter count in bag by 1
        Returns randomly drawn letter
        """
        drawn_letter = self.draw_letter()
        self._inside[exchanged_letter] += 1
        return drawn_letter

    def generate_hand(self):
        """
        Returns a "hand" -  a list of seven randomly drawn letters
        """
        hand = []
        for i in range(HAND_SIZE):
            hand.append(self.draw_letter())
        return hand

    def print_bag(self):
        """
        Prints info about letters in bag
        """
        used_letters = []
        for key, value in self.inside.items():
            if value == 0:
                used_letters.append(key)
            else:
                print(f"There are {value} '{key}' left.")
        print(f"Used letters: {used_letters}")

    def check_letter_availability(self, drawn_letter):
        """
        Returns True if letter in bag.
        """
        return self.inside.get(drawn_letter) != 0

    def get_left(self):
        """
        Returns how many letter are left in bag
        """
        return sum(list(self.inside.values()))
