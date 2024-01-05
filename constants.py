# board constants
BOARD_SIZE = 16
BOARD_CENTER = (8, 8)
ROW_COL_NUMBERS = [str(number) for number in range(1, BOARD_SIZE)]

# hand constants
HAND_SIZE = 7
HAND_LETTER_NUMBERS = [str(number) for number in range(1, HAND_SIZE + 1)]

# letters constants
LETTERS_VALUES = {
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
LETTERS_BAG_COUNT = {
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
BLANK_POSSIBLE_VALUES = [
    "A",
    "Ą",
    "B",
    "C",
    "Ć",
    "D",
    "E",
    "Ę",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "Ł",
    "M",
    "N",
    "Ń",
    "O",
    "Ó",
    "P",
    "R",
    "S",
    "Ś",
    "T",
    "U",
    "W",
    "Y",
    "Z",
    "Ź",
    "Ż",
]

# represenation of empty letters
HAND_EMPTY_LETTER_SYMBOL = "_"
NO_LETTER_SYMBOL = (
    "___"  # its length has to be 3, cannot contain space, letters or ?
)

# names of files with word list
WORDS_BINARY = "words_binary.txt"
ALLOWED_WORDS = "words.txt"
