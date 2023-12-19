class Player:
    def __init__(self, name: str, words: list[str] = None):
        self._name = name
        self._words = words if words else []
        self._points = 0

    @property
    def name(self):
        return self._name

    @property
    def words(self):
        return self._words

    @property
    def points(self):
        return self._points

    def set_words(self, new_words: list[str]):
        self._words = new_words

    def add_word(self, new_word: str):
        self._words.append(new_word)

    def calculate_points(self):
        letter_values = {
            "A": 1,
            "Ą": 5,
            "B": 3,
            "C": 2,
            "Ć": 6,
            "D": 2,
            "E": 1,
            "Ę": 5,
            "F": 5,
            "G": 3,
            "H": 3,
            "I": 1,
            "J": 3,
            "K": 2,
            "L": 2,
            "Ł": 3,
            "M": 2,
            "N": 1,
            "Ń": 7,
            "O": 1,
            "Ó": 5,
            "P": 2,
            "R": 1,
            "S": 1,
            "Ś": 5,
            "T": 2,
            "U": 3,
            "W": 1,
            "Y": 2,
            "Z": 1,
            "Ź": 9,
            "Ż": 5,
            "?": 0,
        }
        total_points = 0
        for word in self.words:
            for char in word.upper():
                total_points += letter_values.get(char, 0)
        self._points = total_points