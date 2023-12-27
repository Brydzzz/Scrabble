from board import Board
from bag import Bag
from hand import Hand
import numpy as np
from rich import print as rprint
from rich.prompt import IntPrompt, Prompt
from copy import deepcopy
from words import check_if_words_allowed
from player import Player


class Game:
    def __init__(self, player_name: str = None):
        self._board = Board()
        self._bag = Bag()
        self._hand = Hand(self.bag)
        self._player = Player(player_name)

    @property
    def board(self):
        return self._board

    @property
    def bag(self):
        return self._bag

    @property
    def hand(self):
        return self._hand

    @property
    def player(self):
        return self._player

    def print_game(self):
        """
        prints board and player's hand
        """
        print("\n Board: \n")
        self.board.print_board()
        print(f"\nYour letters: {self.hand}")
        letter_number_guide = "| 1 | 2 | 3 | 4 | 5 | 6 | 7 |"
        print(f"{letter_number_guide:>43}\n")

    def validate_place_letter_inputs(self, given_number, given_row, given_col):
        """
        Validates player inputs from place_letter() function.
        Returns error message to display and if all requirements are met
        """
        is_field_empty = self.board.check_if_cell_empty(given_row, given_col)
        is_letter_not_empty = self.hand.get_letter(given_number) != "_"
        is_adjacent_to_letter = self.board.check_if_letter_around(
            given_row, given_col
        ) or (given_row, given_col) == (8, 8)
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

    def check_one_word_rule(self):
        """
        Returns True if player didn't break add letter to only one word rule
        else returns False
        """
        played_cells = self.player.played_cells
        row_list = [cell[0] for cell in played_cells]
        col_list = [cell[1] for cell in played_cells]
        if len(set(row_list)) == 1:
            return sorted(col_list) == list(
                range(col_list[0], col_list[0] + len(col_list))
            )
        elif len(set(col_list)) == 1:
            return sorted(row_list) == list(
                range(row_list[0], row_list[0] + len(row_list))
            )
        else:
            return False

    def place_letter(self):
        """
        Gets input from player and places letter on board.
        Then prints updated board
        """
        given_number = IntPrompt.ask(
            "Enter letter number",
            choices=["1", "2", "3", "4", "5", "6", "7"],
        )
        possible_row_col = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
        ]
        if np.all(self.board._cells[1:, 1:] == "___"):
            print("First letter in the game will be placed at (8,8)")
            given_row = 8
            given_col = 8
        else:
            print("Where do you want to place your letter?")
            given_row = IntPrompt.ask("Row number", choices=possible_row_col)
            given_col = IntPrompt.ask(
                "Column number", choices=possible_row_col
            )
        inputs_correct, player_message = self.validate_place_letter_inputs(
            given_number, given_row, given_col
        )
        if inputs_correct:
            letter = self.hand.get_letter(given_number)
            if letter == "?":
                alphabet = list(self.bag.inside.keys())
                alphabet.remove("?")
                blank_value = Prompt.ask(
                    "What letter should blank be?",
                    choices=alphabet,
                )
                letter = blank_value
            self.hand.remove_letter(given_number)
            self.board.update_board(letter, given_row, given_col)
            self.player.add_played_cell((given_row, given_col))
            self.print_game()
        else:
            rprint("[bold red]\nERROR[/bold red]")
            print(player_message)
            print("\nTry again, but with correct input\n")
            self.place_letter()

    def place_letter_round(self):
        """
        When player chooses place letter option in play_round() this executes.
        """
        hand_before_moves = deepcopy(self.hand.letters)
        board_before_moves = deepcopy(self.board.cells)
        while True:
            if set(self.hand.letters) == {"_"}:
                print("NO LETTERS LEFT - END OF THE ROUND")
                break
            self.place_letter()
            print("Place another letter [1] or end round [2]\n")
            option = IntPrompt.ask(
                "Enter your choice here", choices=["1", "2"]
            )
            if option == 2:
                break
        words_on_board = self.board.find_all_words()
        one_word_rule = self.check_one_word_rule()
        print("Checking the words...")
        with open(
            "words_lenght_less_than_6.txt", "r", encoding="UTF-8"
        ) as file:
            all_words_correct = check_if_words_allowed(file, words_on_board)
        if not one_word_rule:
            print("You added letters to more than one word")
            self.hand.hand_to_previous_state(hand_before_moves)
            self.board.board_to_previous_state(board_before_moves)
        elif not all_words_correct or not words_on_board:
            print("Your letters don't form allowed words")
            rprint("You lose your move in this round :cry:")
            self.hand.hand_to_previous_state(hand_before_moves)
            self.board.board_to_previous_state(board_before_moves)
        else:
            print("Everything all right!!!")
            self.player.reset_played_cells()

    def exchange_letters_round(self):
        """
        Executes when player chooses exchange letters option in play_round()
        """
        correct_numbers = ["1", "2", "3", "4", "5", "6", "7"]
        number_of_letters = IntPrompt.ask(
            "Enter how many letter you want to exchange",
            choices=correct_numbers,
        )
        choosen_letter_numbers = [
            IntPrompt.ask(
                "Enter number of a letter you want to exchange",
                choices=correct_numbers,
            )
            for _ in range(number_of_letters)
        ]
        for letter_number in choosen_letter_numbers:
            exchanged_letter = self.hand.get_letter(letter_number)
            new_letter = self.bag.exchange_letter(exchanged_letter)
            self._hand.replace_letter(new_letter, letter_number - 1)

    def play_round(self, round):
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
            self.hand.draw_to_seven_letters(self._bag)
        elif action == 2:
            self.exchange_letters_round()
        else:
            exit()


if __name__ == "__main__":
    player_name = input("Enter your name: ")
    game = Game(player_name)
    round = 1
    while True:
        game.play_round(round)
        round += 1
