from board import Board


def test_check_if_letter_around_typical():
    board = Board()
    board.update_board(" A ", 8, 8)
    board.update_board(" B ", 8, 9)
    board.update_board(" C ", 8, 10)
    board.update_board(" D ", 9, 8)
    result_1 = board.check_if_letter_around(9, 7)
    result_2 = board.check_if_letter_around(9, 10)
    assert result_1 is True
    assert result_2 is True


def test_check_if_letter_around_corners_true():
    board = Board()
    board.update_board(" A ", 1, 2)
    board.update_board(" B ", 15, 14)
    board.update_board(" C ", 14, 1)
    board.update_board(" D ", 1, 14)
    top_left = board.check_if_letter_around(1, 1)
    top_right = board.check_if_letter_around(1, 15)
    down_left = board.check_if_letter_around(15, 1)
    down_right = board.check_if_letter_around(15, 15)
    assert top_left is True
    assert top_right is True
    assert down_left is True
    assert down_right is True


def test_check_if_letter_around_corners_false():
    board = Board()
    top_left = board.check_if_letter_around(1, 1)
    top_right = board.check_if_letter_around(1, 15)
    down_left = board.check_if_letter_around(15, 1)
    down_right = board.check_if_letter_around(15, 15)
    assert top_left is False
    assert top_right is False
    assert down_left is False
    assert down_right is False


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
    words = board.find_all_words()
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
    words = board.find_all_words()
    assert words == ["ALA", "MA", "DOM"]


def test_find_words():
    board = Board()
    board.update_board(" A ", 8, 8)
    board.update_board(" L ", 9, 8)
    board.update_board(" A ", 10, 8)
    board.update_board(" M ", 10, 7)
    board.update_board(" K ", 8, 5)
    board.update_board(" O ", 8, 6)
    board.update_board(" T ", 8, 7)
    words = board.find_all_words()
    assert sorted(words) == sorted(["ALA", "MA", "KOTA"])


def test_find_possible_new_words():
    board = Board()
    board.update_board(" A ", 8, 8)
    board.update_board(" L ", 9, 8)
    board.update_board(" A ", 10, 8)
    board.update_board(" M ", 10, 7)
    board.update_board(" K ", 8, 5)
    board.update_board(" O ", 8, 6)
    board.update_board(" T ", 8, 7)
    played_cells = [(8, 5), (8, 6), (8, 7)]
    words = board.find_possible_new_words(played_cells)
    assert words == ["KOTA"]
