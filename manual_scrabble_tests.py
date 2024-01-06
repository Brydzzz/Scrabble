"""
Functions that I have not been able to write as automatic tests
"""
from scrabble import Game
from constants import HAND_EMPTY_LETTER_SYMBOL


def play_game_end_empty_bag_few_letters_left():
    """
    Sets the game to a state when there are no letters in the bag
    and the player has only 2 letters left in his hand
    """
    players_names = ["end game"]
    game = Game("single", players_names)
    game.bag._inside = {
        "A": 0,
        "Ą": 0,
        "B": 0,
        "C": 0,
        "Ć": 0,
        "D": 0,
        "E": 0,
        "Ę": 0,
        "F": 0,
        "G": 0,
        "H": 0,
        "I": 0,
        "J": 0,
        "K": 0,
        "L": 0,
        "Ł": 0,
        "M": 0,
        "N": 0,
        "Ń": 0,
        "O": 0,
        "Ó": 0,
        "P": 0,
        "R": 0,
        "S": 0,
        "Ś": 0,
        "T": 0,
        "U": 0,
        "W": 0,
        "Y": 0,
        "Z": 0,
        "Ź": 0,
        "Ż": 0,
        "?": 0,
    }
    game.get_player(0).hand._letters = [
        "T",
        "O",
        HAND_EMPTY_LETTER_SYMBOL,
        HAND_EMPTY_LETTER_SYMBOL,
        HAND_EMPTY_LETTER_SYMBOL,
        HAND_EMPTY_LETTER_SYMBOL,
        HAND_EMPTY_LETTER_SYMBOL,
    ]
    game.play_game()


def play_game_one_letter_in_bag():
    """
    Sets the game to a state when there are is one letter in the bag
    and the player has only 2 letters left in his hand
    """
    players_names = ["end game"]
    game = Game("single", players_names)
    game.bag._inside = {
        "A": 1,
        "Ą": 0,
        "B": 0,
        "C": 0,
        "Ć": 0,
        "D": 0,
        "E": 0,
        "Ę": 0,
        "F": 0,
        "G": 0,
        "H": 0,
        "I": 0,
        "J": 0,
        "K": 0,
        "L": 0,
        "Ł": 0,
        "M": 0,
        "N": 0,
        "Ń": 0,
        "O": 0,
        "Ó": 0,
        "P": 0,
        "R": 0,
        "S": 0,
        "Ś": 0,
        "T": 0,
        "U": 0,
        "W": 0,
        "Y": 0,
        "Z": 0,
        "Ź": 0,
        "Ż": 0,
        "?": 0,
    }
    game.get_player(0).hand._letters = [
        "T",
        "O",
        HAND_EMPTY_LETTER_SYMBOL,
        HAND_EMPTY_LETTER_SYMBOL,
        HAND_EMPTY_LETTER_SYMBOL,
        HAND_EMPTY_LETTER_SYMBOL,
        HAND_EMPTY_LETTER_SYMBOL,
    ]
    game.play_game()


if __name__ == "__main__":
    play_game_end_empty_bag_few_letters_left()
    play_game_one_letter_in_bag()
