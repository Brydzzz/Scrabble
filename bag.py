import random


class Bag:
    def __init__(self):
        self._inside = {
            "A": 9,
            "Ą": 1,
            "B": 2,
            "C": 3,
            "Ć": 1,
            "D": 3,
            "E": 7,
            "Ę": 1,
            "F": 1,
            "G": 2,
            "H": 2,
            "I": 8,
            "J": 2,
            "K": 3,
            "L": 3,
            "Ł": 2,
            "M": 3,
            "N": 5,
            "Ń": 1,
            "O": 6,
            "Ó": 1,
            "P": 3,
            "R": 4,
            "S": 4,
            "Ś": 1,
            "T": 3,
            "U": 2,
            "W": 4,
            "Y": 4,
            "Z": 5,
            "Ź": 1,
            "Ż": 1,
            "?": 2,
        }

    @property
    def inside(self):
        return self._inside

    def draw_letter(self):
        """
        Returns randomly drawn letter from bag.
        If letter is not available (its count is 0),
        draws another letter
        If there no letters left in bag returns "_"
        """
        if self.get_left() == 0:
            return "_"
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
        for i in range(7):
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
