import numpy as np


class Board:
    SIZE = 15
    CENTER = 8

    def __init__(self):
        self._cells = np.full((16, 16), "___", dtype=np.dtype("U3"))
        numbers = np.arange(1, 16)
        self._cells[0, 0] = "000"
        self._cells[0, 1:] = np.char.zfill(numbers.astype(str), 3)
        self._cells[1:, 0] = np.char.zfill(numbers.astype(str), 3)

    @property
    def cells(self):
        return self._cells

    def board_to_previous_state(self, previous_cells):
        """
        Changes board cells to given previous_cells
        """
        self._cells = previous_cells

    def print_board(self):
        np.set_printoptions(linewidth=100)
        print(self.cells)

    def access_cell(self, row: int, col: int):
        return self.cells[row, col]

    def update_board(self, new_letter, row, col):
        self._cells[row, col] = f" {new_letter} "

    def check_if_cell_empty(self, row: int, col: int):
        """
        Check if given cell is empty (contains "___")
        """
        return self.access_cell(row, col) == "___"

    def check_if_letter_around(self, row: int, col: int):
        """
        Check if there is at least one letter around cell
        If given cell is next to number guide, treats
        number guide values as "___" to avoid false results
        """
        left = self.access_cell(row, col - 1) if col - 1 != 0 else "___"
        up = self.access_cell(row - 1, col) if row - 1 != 0 else "___"
        right = self.access_cell(row, col + 1) if col + 1 != 16 else "___"
        down = self.access_cell(row + 1, col) if row + 1 != 16 else "___"
        cells = (left, right, up, down)
        return any(cell != "___" for cell in cells)

    def get_word_list_from_dimension(self, dimension_array):
        """
        Get a list of word from row or column
        """
        joined_dimension_array = "".join(dimension_array)
        no_spaces_between_letters = joined_dimension_array.replace(" ", "")
        words_with_empty_str = no_spaces_between_letters.replace("_", " ")
        dimension_words = words_with_empty_str.split()
        return dimension_words

    def find_all_words(self):
        """
        Returns a list of all words on board
        """
        words = []
        for row in self.cells[1:, 1:]:
            row_words = self.get_word_list_from_dimension(row)
            words.extend(row_words)
        for col in self.cells[1:, 1:].T:
            col_words = self.get_word_list_from_dimension(col)
            words.extend(col_words)
        filtered_words = [word for word in words if len(word) != 1]
        return filtered_words

    def find_new_words(self, played_cells):
        row_list = [cell[0] for cell in played_cells]
        col_list = [cell[1] for cell in played_cells]
        rows_no_duplicates = list(set(row_list))
        cols_no_duplicates = list(set(col_list))
        words = []
        for row in rows_no_duplicates:
            row_array = self.cells[row, 1:]
            row_words = self.get_word_list_from_dimension(row_array)
            words.extend(row_words)
        for col in cols_no_duplicates:
            col_array = self.cells[1:, col]
            col_words = self.get_word_list_from_dimension(col_array)
            words.extend(col_words)
        filtered_words = [word for word in words if len(word) != 1]
        return filtered_words
