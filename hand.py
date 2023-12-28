from bag import Bag


class Hand:
    """
    Attributes
    ----------
    letters : list
        a list of letters in hand
    """

    def __init__(self, bag: Bag):
        self._letters = bag.generate_hand()

    @property
    def letters(self):
        return self._letters

    def __str__(self):
        return "| " + " | ".join(self.letters) + " |"

    def hand_to_previous_state(self, previous_letters):
        """
        Changes hand letters to given previous letters
        """
        self._letters = previous_letters

    def remove_letter(self, number):
        """
        Removes letter from hand - replaces it with "_"
        """
        self._letters[number - 1] = "_"

    def get_letter(self, number):
        letter = self.letters[number - 1]
        return letter

    def replace_letter(self, new_letter, index):
        """
        Replaces letter specified by index for new_letter
        """
        self._letters[index] = new_letter

    def draw_to_seven_letters(self, bag: Bag):
        """
        Replaces empty letters ("_") with new randomly drawn letters
        """
        seven_letters = []
        for letter in self.letters:
            if letter == "_":
                new_letter = bag.draw_letter()
                letter = new_letter
            seven_letters.append(letter)
        self._letters = seven_letters
