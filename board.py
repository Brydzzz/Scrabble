import numpy as np


class Board:
    SIZE = 15
    CENTER = 8

    def __init__(self):
        self.cells = np.full((16, 16), "___", dtype=np.dtype("U3"))
        numbers = np.arange(1, 16)
        self.cells[0, 0] = "000"
        self.cells[0, 1:] = np.char.zfill(numbers.astype(str), 3)
        self.cells[1:, 0] = np.char.zfill(numbers.astype(str), 3)

    def print_board(self):
        np.set_printoptions(linewidth=100)
        print(self.cells)

    def access_cell(self, row: int, col: int):
        return self.cells[row, col]

    def update_board(self, new_letter, row, col):
        self.cells[row, col] = f" {new_letter} "
