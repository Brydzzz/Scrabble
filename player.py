from hand import Hand
from constants import LETTERS_VALUES


class Player:
    """
    Attributes
    ----------
    name : str
        player's name
    words : list
        list of words that player created
    points: int
        player's points
    played_cells: list
        list of cells played by player in a round
        each cell is represent as tuple - (row, col)
    hand: Hand
        player's hand - letters they have
    """

    def __init__(
        self, hand: Hand, name: str = "Player  1", words: list[str] = None
    ):
        self._name = name
        self._words = words if words else []
        self._points = 0
        self._played_cells = []
        self._hand = hand

    @property
    def name(self):
        return self._name

    @property
    def words(self):
        return self._words

    @property
    def points(self):
        return self._points

    @property
    def played_cells(self):
        return self._played_cells

    @property
    def hand(self):
        return self._hand

    def reset_played_cells(self):
        self._played_cells = []

    def add_played_cell(self, new_cell: tuple):
        self._played_cells.append(new_cell)

    def set_words(self, new_words: list[str]):
        self._words = new_words

    def add_words(self, new_words):
        self._words.extend(new_words)

    def calculate_points(self):
        """
        calculate player's points and adds them to points attribute
        """
        letter_values = LETTERS_VALUES
        total_points = 0
        minus_points = 0
        word_points = 0
        for word in self.words:
            for char in word.upper():
                word_points += letter_values.get(char, 0)
        for letter in self.hand.letters:
            minus_points += letter_values.get(letter, 0)
        total_points = word_points - minus_points
        total_points = total_points if total_points > 0 else 0
        self._points = total_points
