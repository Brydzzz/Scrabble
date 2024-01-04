from scrabble import Game
from constants import HAND_EMPTY_LETTER_SYMBOL


def test_check_one_word_rule_same_row():
    game = Game("single", "player1")
    board_before_moves = game.board.cells
    game.get_player(0)._played_cells = [(3, 4), (3, 5), (3, 6)]
    assert game.check_one_word_rule(board_before_moves, 0) is True


def test_check_one_word_rule_same_col():
    game = Game("single", "player1")
    board_before_moves = game.board.cells
    game.get_player(0)._played_cells = [(4, 3), (5, 3), (6, 3)]
    assert game.check_one_word_rule(board_before_moves, 0) is True


def test_check_one_word_rule_possible_cells_rows_descending_order():
    game = Game("single", "player1")
    board_before_moves = game.board.cells
    game.get_player(0)._played_cells = [(7, 8), (6, 8)]
    assert game.check_one_word_rule(board_before_moves, 0) is True


def test_check_one_word_rule_possible_cells_cols_descending_order():
    game = Game("single", "player1")
    board_before_moves = game.board.cells
    game.get_player(0)._played_cells = [(8, 7), (8, 6)]
    assert game.check_one_word_rule(board_before_moves, 0) is True


def test_check_one_word_rule_cols_not_correct():
    game = Game("single", "player1")
    board_before_moves = game.board.cells
    game.get_player(0)._played_cells = [(3, 4), (3, 5), (3, 6), (3, 11)]
    assert game.check_one_word_rule(board_before_moves, 0) is False


def test_check_one_word_rule_rows_not_correct():
    game = Game("single", "player1")
    board_before_moves = game.board.cells
    game.get_player(0)._played_cells = [(4, 3), (5, 3), (6, 3), (11, 3)]
    assert game.check_one_word_rule(board_before_moves, 0) is False


def test_check_one_word_added_to_end_and_start_col():
    game = Game("single", "player1")
    game.board.update_board(" X ", 7, 3)
    board_before_moves = game.board.cells
    game.get_player(0)._played_cells = [(4, 3), (5, 3), (6, 3), (8, 3)]
    assert game.check_one_word_rule(board_before_moves, 0) is True


def test_check_one_word_added_to_end_and_start_row():
    game = Game("single", "player1")
    game.board.update_board(" X ", 3, 7)
    game.board.update_board(" X ", 3, 8)
    board_before_moves = game.board.cells
    game.get_player(0)._played_cells = [(3, 4), (3, 5), (3, 6), (3, 9)]
    assert game.check_one_word_rule(board_before_moves, 0) is True


def test_check_one_word_adde_to_two_words_row():
    game = Game("single", "player1")
    game.board.update_board(" X ", 3, 7)
    game.board.update_board(" X ", 3, 10)
    board_before_moves = game.board.cells
    game.get_player(0)._played_cells = [
        (3, 4),
        (3, 5),
        (3, 6),
        (3, 8),
        (3, 11),
    ]
    assert game.check_one_word_rule(board_before_moves, 0) is False


def test_check_one_word_adde_to_two_words_col():
    game = Game("single", "player1")
    game.board.update_board(" X ", 7, 3)
    game.board.update_board(" X ", 10, 3)
    board_before_moves = game.board.cells
    game.get_player(0)._played_cells = [
        (4, 3),
        (5, 3),
        (6, 3),
        (8, 3),
        (11, 3),
    ]
    assert game.check_one_word_rule(board_before_moves, 0) is False


def play_game_end_empty_bag_few_letters_left():
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


# play_game_end_empty_bag_few_letters_left()
# play_game_one_letter_in_bag()
