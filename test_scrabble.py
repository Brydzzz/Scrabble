from scrabble import Game
from constants import HAND_EMPTY_LETTER_SYMBOL, HAND_SIZE


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


def test_check_one_word_added_to_two_words_row():
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


def test_check_one_word_added_to_two_words_col():
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


def test_check_if_players_hands_empty_false():
    game = Game("pvp", ["john", "bob"])
    result = game.check_if_players_hands_empty()
    assert result is False


def test_check_if_players_hands_empty_true_one_player():
    game = Game("pvp", ["john", "bob"])
    game.get_player(0)._hand._letters = [
        HAND_EMPTY_LETTER_SYMBOL for _ in range(HAND_SIZE)
    ]
    result = game.check_if_players_hands_empty()
    assert result is True


def test_check_if_players_hands_empty_true_two_players():
    game = Game("pvp", ["john", "bob"])
    game.get_player(0)._hand._letters = [
        HAND_EMPTY_LETTER_SYMBOL for _ in range(HAND_SIZE)
    ]
    game.get_player(1)._hand._letters = [
        HAND_EMPTY_LETTER_SYMBOL for _ in range(HAND_SIZE)
    ]
    result = game.check_if_players_hands_empty()
    assert result is True


def test_validate_place_letter_inputs_correct(monkeypatch):
    game = Game("pvp", ["john", "bob"])

    def mock_check_if_cell_empty(x, y, z):
        return True

    def mock_get_letter(x, y):
        return "A"

    def mock_letter_around(x, y, z):
        return True

    monkeypatch.setattr(
        "board.Board.check_if_cell_empty", mock_check_if_cell_empty
    )
    monkeypatch.setattr("hand.Hand.get_letter", mock_get_letter)
    monkeypatch.setattr(
        "board.Board.check_if_letter_around", mock_letter_around
    )
    result, messages = game.validate_place_letter_inputs(1, 6, 7, 0)
    assert result is True
    assert messages == ""


def test_validate_place_letter_inputs_cell_not_empty(monkeypatch):
    game = Game("pvp", ["john", "bob"])

    def mock_check_if_cell_empty(x, y, z):
        return False

    def mock_get_letter(x, y):
        return "A"

    def mock_letter_around(x, y, z):
        return True

    monkeypatch.setattr(
        "board.Board.check_if_cell_empty", mock_check_if_cell_empty
    )
    monkeypatch.setattr("hand.Hand.get_letter", mock_get_letter)
    monkeypatch.setattr(
        "board.Board.check_if_letter_around", mock_letter_around
    )
    result, messages = game.validate_place_letter_inputs(1, 6, 7, 0)
    assert result is False
    assert messages == "Choosen field is not empty"


def test_validate_place_letter_inputs_empty_letter(monkeypatch):
    game = Game("pvp", ["john", "bob"])

    def mock_check_if_cell_empty(x, y, z):
        return True

    def mock_get_letter(x, y):
        return HAND_EMPTY_LETTER_SYMBOL

    def mock_letter_around(x, y, z):
        return True

    monkeypatch.setattr(
        "board.Board.check_if_cell_empty", mock_check_if_cell_empty
    )
    monkeypatch.setattr("hand.Hand.get_letter", mock_get_letter)
    monkeypatch.setattr(
        "board.Board.check_if_letter_around", mock_letter_around
    )
    result, messages = game.validate_place_letter_inputs(1, 6, 7, 0)
    assert result is False
    assert messages == "Cannot play empty letter"


def test_validate_place_letter_inputs_letter_not_adjacent(monkeypatch):
    game = Game("pvp", ["john", "bob"])

    def mock_check_if_cell_empty(x, y, z):
        return True

    def mock_get_letter(x, y):
        return "A"

    def mock_letter_around(x, y, z):
        return False

    monkeypatch.setattr(
        "board.Board.check_if_cell_empty", mock_check_if_cell_empty
    )
    monkeypatch.setattr("hand.Hand.get_letter", mock_get_letter)
    monkeypatch.setattr(
        "board.Board.check_if_letter_around", mock_letter_around
    )
    result, messages = game.validate_place_letter_inputs(1, 6, 7, 0)
    assert result is False
    assert messages == "Letter has to be adjacent to an already placed letter"


def test_choose_winner_player_one(monkeypatch):
    game = Game("pvp", ["john", "ben"])

    game.get_player(0)._hand._letters = [
        HAND_EMPTY_LETTER_SYMBOL for _ in range(HAND_SIZE)
    ]
    game.get_player(1)._hand._letters = [
        HAND_EMPTY_LETTER_SYMBOL for _ in range(HAND_SIZE)
    ]
    game.get_player(0).set_words(["jabłko", "kot", "samochód", "dom"])
    game.get_player(1).set_words(["telewizor", "rower", "kwiat"])
    if_draw, winner, loser, winner_points, loser_points = game.choose_winner()
    assert if_draw is False
    assert winner == "john"
    assert loser == "ben"
    assert winner_points == 40
    assert loser_points == 23


def test_choose_winner_player_two(monkeypatch):
    game = Game("pvp", ["john", "ben"])

    game.get_player(0)._hand._letters = [
        HAND_EMPTY_LETTER_SYMBOL for _ in range(HAND_SIZE)
    ]
    game.get_player(1)._hand._letters = [
        HAND_EMPTY_LETTER_SYMBOL for _ in range(HAND_SIZE)
    ]
    game.get_player(1).set_words(["jabłko", "kot", "samochód", "dom"])
    game.get_player(0).set_words(["telewizor", "rower", "kwiat"])
    if_draw, winner, loser, winner_points, loser_points = game.choose_winner()
    assert if_draw is False
    assert winner == "ben"
    assert loser == "john"
    assert winner_points == 40
    assert loser_points == 23


def test_choose_winner_draw(monkeypatch):
    game = Game("pvp", ["john", "ben"])
    if_draw, first_player_points = game.choose_winner()
    assert if_draw is True
    assert first_player_points == 0


def test_game_ending_single(capsys):
    game = Game("single", ["john"])
    game.game_ending()
    captured = capsys.readouterr()
    outputs = captured.out.strip().split("\n")
    assert "Congrats john!" in outputs[0]
    assert outputs[1] == "Your score is: 0"


def test_game_ending_pvp_winner(capsys):
    game = Game("pvp", ["john", "ben"])

    game.get_player(0)._hand._letters = [
        HAND_EMPTY_LETTER_SYMBOL for _ in range(HAND_SIZE)
    ]
    game.get_player(1)._hand._letters = [
        HAND_EMPTY_LETTER_SYMBOL for _ in range(HAND_SIZE)
    ]
    game.get_player(0).set_words(["jabłko", "kot", "samochód", "dom"])
    game.get_player(1).set_words(["telewizor", "rower", "kwiat"])
    game.game_ending()
    captured = capsys.readouterr()
    all_outputs = captured.out.split("\n")
    winner_msg = all_outputs[0]
    winner_score_msg = all_outputs[1]
    loser_msg = all_outputs[2]
    loser_score_msg = all_outputs[3]
    assert "john is the winner!" in winner_msg
    assert winner_score_msg == "john's score is: 40"
    assert "ben lost this time" in loser_msg
    assert loser_score_msg == "ben's score is: 23"


def test_game_ending_pvp_draw(capsys):
    game = Game("pvp", ["john", "ben"])

    game.get_player(0)._hand._letters = [
        HAND_EMPTY_LETTER_SYMBOL for _ in range(HAND_SIZE)
    ]
    game.get_player(1)._hand._letters = [
        HAND_EMPTY_LETTER_SYMBOL for _ in range(HAND_SIZE)
    ]
    game.game_ending()
    captured = capsys.readouterr()
    output = captured.out.strip()
    assert output == "It's a draw! You both scored 0"
