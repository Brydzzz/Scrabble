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
