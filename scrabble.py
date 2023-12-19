from board import Board
from bag import Bag
from hand import Hand
import numpy as np
from rich import print as rprint
from rich.prompt import IntPrompt, Prompt


class Game:
    def __init__(self):
        self._board = Board()
        self._bag = Bag()
        self._hand = Hand(self.bag)

    @property
    def board(self):
        return self._board

    @property
    def bag(self):
        return self._bag

    @property
    def hand(self):
        return self._hand

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
        print("[3] Exit game")
        action = IntPrompt.ask("Enter number here", choices=["1", "2", "3"])
        if action == 1:
            self.place_letter_round()
            self.hand.draw_to_seven_letters(self._bag)
        elif action == 2:
            self.exchange_letters_round()
        else:
            exit()


if __name__ == "__main__":
    game = Game()
    round = 1
    while True:
        game.play_round(round)
        round += 1
