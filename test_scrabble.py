from scrabble import Game


def test_check_one_word_rule_same_row():
    game = Game()
    board_before_moves = game.board.cells
    game.player._played_cells = [(3, 4), (3, 5), (3, 6)]
    assert game.check_one_word_rule(board_before_moves) is True


def test_check_one_word_rule_same_col():
    game = Game()
    board_before_moves = game.board.cells
    game.player._played_cells = [(4, 3), (5, 3), (6, 3)]
    assert game.check_one_word_rule(board_before_moves) is True


def test_check_one_word_rule_possible_cells_rows_descending_order():
    game = Game()
    board_before_moves = game.board.cells
    game.player._played_cells = [(7, 8), (6, 8)]
    assert game.check_one_word_rule(board_before_moves) is True


def test_check_one_word_rule_possible_cells_cols_descending_order():
    game = Game()
    board_before_moves = game.board.cells
    game.player._played_cells = [(8, 7), (8, 6)]
    assert game.check_one_word_rule(board_before_moves) is True


def test_check_one_word_rule_cols_not_correct():
    game = Game()
    board_before_moves = game.board.cells
    game.player._played_cells = [(3, 4), (3, 5), (3, 6), (3, 11)]
    assert game.check_one_word_rule(board_before_moves) is False


def test_check_one_word_rule_rows_not_correct():
    game = Game()
    board_before_moves = game.board.cells
    game.player._played_cells = [(4, 3), (5, 3), (6, 3), (11, 3)]
    assert game.check_one_word_rule(board_before_moves) is False


def test_check_one_word_added_to_end_and_start_col():
    game = Game()
    game.board.update_board(" X ", 7, 3)
    board_before_moves = game.board.cells
    game.player._played_cells = [(4, 3), (5, 3), (6, 3), (8, 3)]
    assert game.check_one_word_rule(board_before_moves) is True


def test_check_one_word_added_to_end_and_start_row():
    game = Game()
    game.board.update_board(" X ", 3, 7)
    game.board.update_board(" X ", 3, 8)
    board_before_moves = game.board.cells
    game.player._played_cells = [(3, 4), (3, 5), (3, 6), (3, 9)]
    assert game.check_one_word_rule(board_before_moves) is True


def test_check_one_word_adde_to_two_words_row():
    game = Game()
    game.board.update_board(" X ", 3, 7)
    game.board.update_board(" X ", 3, 10)
    board_before_moves = game.board.cells
    game.player._played_cells = [(3, 4), (3, 5), (3, 6), (3, 8), (3, 11)]
    assert game.check_one_word_rule(board_before_moves) is False


def test_check_one_word_adde_to_two_words_col():
    game = Game()
    game.board.update_board(" X ", 7, 3)
    game.board.update_board(" X ", 10, 3)
    board_before_moves = game.board.cells
    game.player._played_cells = [(4, 3), (5, 3), (6, 3), (8, 3), (11, 3)]
    assert game.check_one_word_rule(board_before_moves) is False