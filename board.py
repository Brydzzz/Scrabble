import numpy as np
from collections import Counter
from copy import deepcopy


class Board:
    def __init__(self):
        self._cells = np.full((16, 16), "___", dtype=np.dtype("U3"))
        numbers = np.arange(1, 16)
        self._cells[0, 0] = "000"
        self._cells[0, 1:] = np.char.zfill(numbers.astype(str), 3)
        self._cells[1:, 0] = np.char.zfill(numbers.astype(str), 3)
        self._words = []
        self._blanks = []

    @property
    def cells(self):
        return self._cells

    @property
    def words(self):
        return self._words

    @property
    def blanks(self):
        return self._blanks

    def board_to_previous_state(self, previous_cells):
        """
        Changes board cells to given previous_cells
        """
        self._cells = previous_cells

    def print_board(self):
        """
        Prints board
        """
        np.set_printoptions(linewidth=100)
        print(self.cells)

    def update_board(self, new_letter, row, col):
        self._cells[row, col] = f" {new_letter} "

    def add_blank_info(self, row: int, col: int, letter_value: str):
        """
        Adds tuple with information about blank to blanks attribute
        """
        self._blanks.append((row, col, letter_value))

    def blanks_info(self):
        """
        Returns information about blanks on board
        """
        if self.blanks:
            blank_descriptions = [
                f"Blank in {blank[0]} row and {blank[1]} column is {blank[2]}"
                for blank in self.blanks
            ]

            blank_descriptions = "\n".join(blank_descriptions)
        else:
            blank_descriptions = "There are no blanks on board"
        return f"Blanks Info:\n{blank_descriptions}\n"

    def blanks_to_previous_state(self, previous_blanks):
        """
        Changes blanks to given previous_blanks
        """
        self._blanks = previous_blanks

    def access_cell(self, row: int, col: int):
        """
        Returns the value of cell for given row and col
        """
        return self.cells[row, col]

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

    def find_possible_new_words(self, played_cells):
        """
        Finds possible new words created by player
        Checks only rows and cols where player played letters
        If blank in row replaces it with its letter value
        """
        row_list = [cell[0] for cell in played_cells]
        col_list = [cell[1] for cell in played_cells]
        rows_no_duplicates = list(set(row_list))
        cols_no_duplicates = list(set(col_list))
        words = []
        for row in rows_no_duplicates:
            row_array = deepcopy(self.cells[row, 1:])
            for blank in self.blanks:
                if row == blank[0]:
                    row_array[blank[1] - 1] = blank[2]
            row_words = self.get_word_list_from_dimension(row_array)
            words.extend(row_words)
        for col in cols_no_duplicates:
            col_array = deepcopy(self.cells[1:, col])
            for blank in self.blanks:
                if col == blank[1]:
                    col_array[blank[0] - 1] = blank[2]
            col_words = self.get_word_list_from_dimension(col_array)
            words.extend(col_words)
        filtered_words = [word for word in words if len(word) != 1]
        return filtered_words

    def get_player_words(self):
        """
        Returns a list of words that were created by player
        """
        player_words = []
        words_before_move = Counter(self.words)
        words_after_move = Counter(self.find_all_words())
        for word, count in words_after_move.items():
            if count != words_before_move.get(word):
                player_words.append(word)
        return player_words

    def update_words(self):
        """
        Change words to a list of words found on board
        """
        self._words = self.find_all_words()
