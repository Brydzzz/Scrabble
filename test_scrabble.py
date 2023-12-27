from scrabble import Game


def test_check_one_word_rule_same_row():
    game = Game()
    game.player._played_cells = [(3, 4), (3, 5), (3, 6)]
    assert game.check_one_word_rule() is True


def test_check_one_word_rule_same_col():
    game = Game()
    game.player._played_cells = [(4, 3), (5, 3), (6, 3)]
    assert game.check_one_word_rule() is True


def test_check_one_word_rule_cols_not_correct():
    game = Game()
    game.player._played_cells = [(3, 4), (3, 5), (3, 6), (3, 11)]
    assert game.check_one_word_rule() is False


def test_check_one_word_rule_rows_not_correct():
    game = Game()
    game.player._played_cells = [(4, 3), (5, 3), (6, 3), (11, 3)]
    assert game.check_one_word_rule() is False
