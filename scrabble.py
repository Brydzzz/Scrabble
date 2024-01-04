from board import Board
from bag import Bag
from hand import Hand
import numpy as np
from rich import print as rprint
from rich.prompt import IntPrompt, Prompt
from copy import deepcopy
from words import check_the_words
from player import Player
from constants import (
    HAND_EMPTY_LETTER_SYMBOL,
    BOARD_CENTER,
    NO_LETTER_SYMBOL,
    HAND_LETTER_NUMBERS,
    ROW_COL_NUMBERS,
    BLANK_POSSIBLE_VALUES,
)


class Game:
    """
    Attributes
    ----------
    board : Board
        game's board
    bag : Bag
        game's bag
    player: Player
        player that playes the game
    """

    def __init__(self, player_name: str = None):
        self._board = Board()
        self._bag = Bag()
        hand = Hand(self.bag)  # TODO: wylosowac dwie ręce jeśli potrzeba
        self._player = Player(
            hand, player_name
        )  # TODO: atrybut nazywa sie players i ma liste graczy
        # TODO: dodać paramter tryb gry, bo pomoze z tymi rekami

    @property
    def board(self):
        return self._board

    @property
    def bag(self):
        return self._bag

    @property
    def player(self):
        return self._player  # TODO daje liste graczy

    def print_game(self):  # TODO ma w parametrze ktory gracz
        """
        prints board and player's hand
        """
        print("\n Board: \n")
        self.board.print_board()
        hand_info_message = f"\nYour letters: {self.player.hand}"
        print(hand_info_message)
        letter_number_guide = " | ".join(HAND_LETTER_NUMBERS)
        offset = len(hand_info_message) - 1
        print(f"| {letter_number_guide} |".rjust(offset) + "\n")
        print(self.board.blanks_info())

    def validate_place_letter_inputs(
        self, given_number, given_row, given_col
    ):  # TODO ma w parametrze ktory gracz
        """
        Validates player inputs from place_letter() function.
        Returns error message to display and if all requirements are met
        """
        is_field_empty = self.board.check_if_cell_empty(given_row, given_col)
        is_letter_not_empty = (
            self.player.hand.get_letter(given_number)
            != HAND_EMPTY_LETTER_SYMBOL
        )
        is_adjacent_to_letter = (
            self.board.check_if_letter_around(given_row, given_col)
            or (given_row, given_col) == BOARD_CENTER
        )
        inputs_correct = (
            is_field_empty,
            is_letter_not_empty,
            is_adjacent_to_letter,
        )
        messages = []
        if not is_field_empty:
            messages.append("Choosen field is not empty")
        if not is_letter_not_empty:
            messages.append("Cannot play empty letter")
        if not is_adjacent_to_letter:
            messages.append(
                "Letter has to be adjacent to an already placed letter"
            )

        return all(inputs_correct), "\n".join(messages)

    def check_one_word_rule(
        self, board_before_moves
    ):  # TODO ma w parametrze ktory gracz
        """
        Returns True if player didn't break add letter to only one word rule
        else returns False
        """
        played_cells = self.player.played_cells
        row_list = [cell[0] for cell in played_cells]
        col_list = [cell[1] for cell in played_cells]
        if len(set(row_list)) == 1:
            row = row_list[0]
            for col_number in range(min(col_list), max(col_list) + 1):
                if (
                    col_number not in col_list
                    and board_before_moves[row][col_number] == NO_LETTER_SYMBOL
                ):
                    return False
            return True
        elif len(set(col_list)) == 1:
            col = col_list[0]
            for row_number in range(min(row_list), max(row_list) + 1):
                if (
                    row_number not in row_list
                    and board_before_moves[row_number][col] == NO_LETTER_SYMBOL
                ):
                    return False
            return True
        else:
            return False

    def place_letter(self):  # TODO ma w parametrze ktory gracz
        """
        Gets input from player and places letter on board.
        Then prints updated board
        """
        given_number = IntPrompt.ask(
            "Enter letter number",
            choices=HAND_LETTER_NUMBERS,
        )
        if np.all(self.board._cells[1:, 1:] == NO_LETTER_SYMBOL):
            print("First letter in the game will be placed at (8,8)")
            given_row, given_col = BOARD_CENTER
        else:
            print("Where do you want to place your letter?")
            given_row = IntPrompt.ask("Row number", choices=ROW_COL_NUMBERS)
            given_col = IntPrompt.ask("Column number", choices=ROW_COL_NUMBERS)
        inputs_correct, player_message = self.validate_place_letter_inputs(
            given_number, given_row, given_col
        )
        if inputs_correct:
            letter = self.player.hand.get_letter(given_number)
            if letter == "?":
                blank_value = Prompt.ask(
                    "What letter should blank be?",
                    choices=BLANK_POSSIBLE_VALUES,
                )
                self.board.add_blank_info(given_row, given_col, blank_value)
            self.player.hand.remove_letter(given_number)
            self.board.update_board(letter, given_row, given_col)
            self.player.add_played_cell((given_row, given_col))
            self.print_game()
        else:
            rprint("[bold red]\nERROR[/bold red]")
            print(player_message)
            print("\nTry again, but with correct input\n")
            self.place_letter()

    def game_to_previous_state(
        self, hand_before_moves, board_before_moves, blanks_before_moves
    ):  # TODO ma w parametrze ktory gracz
        """
        Changes hand, board and blanks to previous state
        """
        self.player.hand.hand_to_previous_state(hand_before_moves)
        self.board.board_to_previous_state(board_before_moves)
        self.board.blanks_to_previous_state(blanks_before_moves)

    def place_letter_round(self):  # TODO ma w parametrze ktory gracz
        """
        When player chooses place letter option in play_round() this executes.
        """
        hand_before_moves = deepcopy(self.player.hand.letters)
        board_before_moves = deepcopy(self.board.cells)
        blanks_before_moves = deepcopy(self.board.blanks)
        while True:
            if set(self.player.hand.letters) == {HAND_EMPTY_LETTER_SYMBOL}:
                print("NO LETTERS LEFT - END OF THE ROUND")
                break
            self.place_letter()
            print("Place another letter [1] or end round [2]\n")
            option = IntPrompt.ask(
                "Enter your choice here", choices=["1", "2"]
            )
            if option == 2:
                break
        new_words = self.board.find_possible_new_words(
            self.player.played_cells
        )
        one_word_rule = self.check_one_word_rule(board_before_moves)
        print("Checking the words...")
        all_words_correct = check_the_words(new_words)
        if not one_word_rule:
            print("You added letters to more than one word")
            self.game_to_previous_state(
                hand_before_moves, board_before_moves, blanks_before_moves
            )
        elif not all_words_correct or not new_words:
            print("Your letters don't form allowed words")
            rprint("You lose your move in this round :cry:")
            self.game_to_previous_state(
                hand_before_moves, board_before_moves, blanks_before_moves
            )
        else:
            print("Everything all right!!!")
            player_words = self.board.get_player_words()
            self.player.add_words(player_words)
            self.board.update_words()
        self.player.reset_played_cells()

    def exchange_letters_round(self):  # TODO ma w parametrze ktory gracz
        """
        Executes when player chooses exchange letters option in play_round()
        """
        number_of_letters = IntPrompt.ask(
            "Enter how many letter you want to exchange",
            choices=HAND_LETTER_NUMBERS,
        )
        choosen_letter_numbers = [
            IntPrompt.ask(
                "Enter number of a letter you want to exchange",
                choices=HAND_LETTER_NUMBERS,
            )
            for _ in range(number_of_letters)
        ]
        for letter_number in choosen_letter_numbers:
            exchanged_letter = self.player.hand.get_letter(letter_number)
            try:
                new_letter = self.bag.exchange_letter(exchanged_letter)
                self._player._hand.replace_letter(
                    new_letter, letter_number - 1
                )
            except KeyError:
                print(f"Cannot exchange letter with number {letter_number}")
                pass

    def game_ending(self):
        """
        displayes end game message and quits game
        """
        self.player.calculate_points()
        points = self.player.points
        # TODO: display end message for all players, maybe writes who wins
        print(f"Congrats {self.player.name}! Your score is: {points}")
        exit()

    def play_round(self, round):  # TODO ma w parametrze ktory gracz
        """
        method responsible for player's journey
        """
        print(f"\nROUND: {round}")
        self.print_game()
        print("What do you want to do?")
        print("[1] Place letters")
        print("[2] Exchange letters")
        print("[3] End game")
        action = IntPrompt.ask("Enter number here", choices=["1", "2", "3"])
        if action == 1:
            self.place_letter_round()
            self.player.hand.draw_to_seven_letters(self._bag)
        elif action == 2:
            if self.bag.get_left() == 0:
                print("CANNOT EXCHANGE LETTERS - BAG IS EMPTY")
            else:
                self.exchange_letters_round()
        else:
            self.game_ending()

    def play_game(self):
        round = 1
        while True:
            if (
                self.bag.get_left() == 0 and set(self.player.hand.letters)
            ) == {HAND_EMPTY_LETTER_SYMBOL}:
                print("END OF THE GAME")
                self.game_ending()
            self.play_round(round)
            # TODO kolejne wywołanie play_round w trybie pvp
            round += 1


if __name__ == "__main__":
    # TODO zapytanie o tryb gry, odpowiednio pytam sie o imie raz lub dwa razy
    player_name = input("Enter your name: ")
    game = Game(player_name)  # TODO do game mogę podać też game_mode
    game.play_game()