import random


class Bag:
    def __init__(self):
        self.inside = {
            "a": 9,
            "ą": 1,
            "b": 2,
            "c": 3,
            "ć": 1,
            "d": 3,
            "e": 7,
            "ę": 1,
            "f": 1,
            "g": 2,
            "h": 2,
            "i": 8,
            "j": 2,
            "k": 3,
            "l": 3,
            "ł": 2,
            "m": 3,
            "n": 5,
            "ń": 1,
            "o": 6,
            "ó": 1,
            "p": 3,
            "r": 4,
            "s": 4,
            "ś": 1,
            "t": 3,
            "u": 2,
            "w": 4,
            "y": 4,
            "z": 5,
            "ź": 1,
            "ż": 1,
            "?": 2,
        }

    def draw_letter(self):
        """
        Returns randomly drawn letter from bag.
        If letter is not available (its count is 0),
        draws another letter
        """
        drawn_letter = random.choice(list(self.inside.keys()))
        while not self.check_letter_availability(drawn_letter):
            drawn_letter = random.choice(list(self.inside.keys()))
        self.inside[drawn_letter] -= 1
        return drawn_letter

    def generate_hand(self):
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
