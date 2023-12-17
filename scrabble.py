from board import Board
from bag import Bag
from hand import Hand
import numpy as np


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
        is_given_number_correct = 1 <= given_number <= 7
        is_given_row_correct = 1 <= given_row <= 15
        is_given_col_correct = 1 <= given_col <= 15
        is_field_empty = True
        is_letter_not_empty = True
        if is_given_row_correct and is_given_col_correct:
            is_field_empty = self.board.check_if_cell_empty(
                given_row, given_col
            )
        if is_given_number_correct:
            is_letter_not_empty = self.hand.get_letter(given_number) != "_"
        inputs_correct = (
            is_given_number_correct,
            is_given_row_correct,
            is_given_col_correct,
            is_field_empty,
            is_letter_not_empty,
        )
        messages = []
        if not is_given_number_correct:
            messages.append("Letter number is incorrect")
        if not is_given_row_correct:
            messages.append("Row number is incorrect")
        if not is_given_col_correct:
            messages.append("Col number is incorrect")
        if not is_field_empty:
            messages.append("Choosen field is not empty or doesn't exist")
        if not is_letter_not_empty:
            messages.append("Cannot play empty letter")

        return all(inputs_correct), "\n".join(messages)

    def place_letter(self):
        """
        Gets input from player and places letter on board.
        Then prints updated board
        """
        while True:
            try:
                given_number = int(input("Enter letter number: "))
                print("Where do you want to place your letter?")
                given_row = int(input("Row number: "))
                given_col = int(input("Column number: "))
                break
            except ValueError:
                print("Input has to be an integer\n")
        inputs_correct, player_message = self.validate_place_letter_inputs(
            given_number, given_row, given_col
        )
        if inputs_correct:
            if np.all(self.board._cells[1:, 1:] == "___"):
                print("First letter in the game will be placed at (8,8)")
                given_row = 8
                given_col = 8
            letter = self.hand.get_letter(given_number)
            self.hand.remove_letter(given_number)
            self.board.update_board(letter, given_row, given_col)
            self.print_game()
        else:
            print("\nERROR")
            print(player_message)
            print("\nTry again but with correct input\n")
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
            option = input("Enter your choice here: ")
            if option == "2":
                break
            elif option == "1":
                pass

    def exchange_letters_round(self):
        """
        Executes when player chooses exchange letters option in play_round()
        """
        number_of_letters = int(
            input("Enter how many letter you want to exchange: ")
        )
        choosen_letter_numbers = [
            int(input("Enter number of letter you want to exchange: "))
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
        while True:
            try:
                action = int(input("Enter number here: "))
                break
            except ValueError:
                print("Input has to be an integer\n")
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
