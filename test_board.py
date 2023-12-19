from board import Board


def test_check_if_letter_around():
    board = Board()
    board.update_board(" A ", 8, 8)
    board.update_board(" B ", 8, 9)
    board.update_board(" C ", 8, 10)
    board.update_board(" D ", 9, 8)
    result_1 = board.check_if_letter_around(9, 7)
    result_2 = board.check_if_letter_around(9, 10)
    assert result_1 is True
    assert result_2 is True


def test_find_words_in_rows():
    board = Board()
    board.update_board(" A ", 8, 8)
    board.update_board(" L ", 8, 9)
    board.update_board(" A ", 8, 10)
    board.update_board(" M ", 8, 12)
    board.update_board(" A ", 8, 13)
    board.update_board(" D ", 10, 8)
    board.update_board(" O ", 10, 9)
    board.update_board(" M ", 10, 10)
    words = board.find_words()
    assert words == ["ALA", "MA", "DOM"]


def test_find_words_in_cols():
    board = Board()
    board.update_board(" A ", 8, 8)
    board.update_board(" L ", 9, 8)
    board.update_board(" A ", 10, 8)
    board.update_board(" M ", 12, 8)
    board.update_board(" A ", 13, 8)
    board.update_board(" D ", 8, 10)
    board.update_board(" O ", 9, 10)
    board.update_board(" M ", 10, 10)
    words = board.find_words()
    assert words == ["ALA", "MA", "DOM"]
