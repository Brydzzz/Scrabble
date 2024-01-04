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

    def __init__(self, game_mode: str, players_names: list[str]):
        self._game_mode = game_mode
        self._board = Board()
        self._bag = Bag()
        hand = Hand(self.bag)
        if game_mode == "pvp":
            second_hand = Hand(self.bag)
            self._players = [
                Player(hand, players_names[0]),
                Player(second_hand, players_names[1]),
            ]
        else:
            self._players = [Player(hand, players_names[0])]

    @property
    def board(self):
        return self._board

    @property
    def bag(self):
        return self._bag

    @property
    def game_mode(self):
        return self._game_mode

    @property
    def players(self):
        return self._players

    def get_player(self, index):
        return self._players[index]

    def check_if_players_hands_empty(self):
        for player in self.players:
            if set(player.hand.letters) == {HAND_EMPTY_LETTER_SYMBOL}:
                return True
        return False

    def print_game(self, player_index):
        """
        prints board and player's hand
        """
        print("\n Board: \n")
        self.board.print_board()
        print(f"{self.get_player(player_index).name.upper()}'s TURN")
        hand_info_message = (
            f"\nYour letters: {self.get_player(player_index).hand}"
        )
        print(hand_info_message)
        letter_number_guide = " | ".join(HAND_LETTER_NUMBERS)
        offset = len(hand_info_message) - 1
        print(f"| {letter_number_guide} |".rjust(offset) + "\n")
        print(self.board.blanks_info())

    def validate_place_letter_inputs(
        self, given_number, given_row, given_col, player_index
    ):
        """
        Validates player inputs from place_letter() function.
        Returns error message to display and if all requirements are met
        """
        is_field_empty = self.board.check_if_cell_empty(given_row, given_col)
        is_letter_not_empty = (
            self.get_player(player_index).hand.get_letter(given_number)
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

    def check_one_word_rule(self, board_before_moves, player_index):
        """
        Returns True if player didn't break add letter to only one word rule
        else returns False
        """
        played_cells = self.get_player(player_index).played_cells
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

    def place_letter(self, player_index):
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
            given_number, given_row, given_col, player_index
        )
        if inputs_correct:
            letter = self.get_player(player_index).hand.get_letter(
                given_number
            )
            if letter == "?":
                blank_value = Prompt.ask(
                    "What letter should blank be?",
                    choices=BLANK_POSSIBLE_VALUES,
                )
                self.board.add_blank_info(given_row, given_col, blank_value)
            self.get_player(player_index).hand.remove_letter(given_number)
            self.board.update_board(letter, given_row, given_col)
            self.get_player(player_index).add_played_cell(
                (given_row, given_col)
            )
            self.print_game(player_index)
        else:
            rprint("[bold red]\nERROR[/bold red]")
            print(player_message)
            print("\nTry again, but with correct input\n")
            self.place_letter(player_index)

    def game_to_previous_state(
        self,
        hand_before_moves,
        board_before_moves,
        blanks_before_moves,
        player_index,
    ):
        """
        Changes hand, board and blanks to previous state
        """
        self.get_player(player_index).hand.hand_to_previous_state(
            hand_before_moves
        )
        self.board.board_to_previous_state(board_before_moves)
        self.board.blanks_to_previous_state(blanks_before_moves)

    def place_letter_round(self, player_index):
        """
        When player chooses place letter option in play_round() this executes.
        """
        hand_before_moves = deepcopy(
            self.get_player(player_index).hand.letters
        )
        board_before_moves = deepcopy(self.board.cells)
        blanks_before_moves = deepcopy(self.board.blanks)
        while True:
            if set(self.get_player(player_index).hand.letters) == {
                HAND_EMPTY_LETTER_SYMBOL
            }:
                print("NO LETTERS LEFT - END OF THE ROUND")
                break
            self.place_letter(player_index)
            print("Place another letter [1] or end round [2]\n")
            option = IntPrompt.ask(
                "Enter your choice here", choices=["1", "2"]
            )
            if option == 2:
                break
        new_words = self.board.find_possible_new_words(
            self.get_player(player_index).played_cells
        )
        one_word_rule = self.check_one_word_rule(
            board_before_moves, player_index
        )
        print("Checking the words...")
        all_words_correct = check_the_words(new_words)
        if not one_word_rule:
            print("You added letters to more than one word")
            self.game_to_previous_state(
                hand_before_moves,
                board_before_moves,
                blanks_before_moves,
                player_index,
            )
        elif not all_words_correct or not new_words:
            print("Your letters don't form allowed words")
            rprint("You lose your move in this round :cry:")
            self.game_to_previous_state(
                hand_before_moves,
                board_before_moves,
                blanks_before_moves,
                player_index,
            )
        else:
            print("Everything all right!!!")
            player_words = self.board.get_player_words()
            self.get_player(player_index).add_words(player_words)
            self.board.update_words()
        self.get_player(player_index).reset_played_cells()

    def exchange_letters_round(self, player_index):
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
            exchanged_letter = self.get_player(player_index).hand.get_letter(
                letter_number
            )
            try:
                new_letter = self.bag.exchange_letter(exchanged_letter)
                self._players[player_index]._hand.replace_letter(
                    new_letter, letter_number - 1
                )
            except KeyError:
                print(f"Cannot exchange letter with number {letter_number}")
                pass

    def choose_winner(self):
        self.get_player(0).calculate_points()
        self.get_player(1).calculate_points()
        first_player_points = self.get_player(0).points
        second_player_points = self.get_player(1).points
        if first_player_points > second_player_points:
            winner = self.get_player(0).name
            loser = self.get_player(1).name
            winner_points = first_player_points
            loser_points = second_player_points
        elif first_player_points < second_player_points:
            winner = self.get_player(1).name
            loser = self.get_player(0).name
            winner_points = second_player_points
            loser_points = first_player_points
        else:
            return "draw", first_player_points
        return winner, loser, winner_points, loser_points

    def game_ending(self):
        """
        displays end game message and quits game
        """
        if self.game_mode == "pvp":
            result = self.choose_winner()
            if result[0] == "draw":
                points = result[1]
                print(f"It's a draw! You both scored {points}")
            else:
                winner, loser, winner_points, loser_points = result
                print(f"{winner} is the winner! They scored {winner_points}")
                print(f"{loser} lost this time :( They scored {loser_points}")
        else:
            self.get_player(0).calculate_points()
            points = self.get_player(0).points
            print(
                f"Congrats {self.get_player(0).name}! Your score is: {points}"
            )
        exit()

    def play_round(self, round, player_index):
        """
        method responsible for player's journey
        """
        print(f"\nROUND: {round}")
        self.print_game(player_index)
        print("What do you want to do?")
        print("[1] Place letters")
        print("[2] Exchange letters")
        print("[3] End game")
        action = IntPrompt.ask("Enter number here", choices=["1", "2", "3"])
        if action == 1:
            self.place_letter_round(player_index)
            self.get_player(player_index).hand.draw_to_seven_letters(self._bag)
        elif action == 2:
            if self.bag.get_left() == 0:
                print("CANNOT EXCHANGE LETTERS - BAG IS EMPTY")
            else:
                self.exchange_letters_round(player_index)
        else:
            self.game_ending()

    def play_game(self):
        round = 1
        while True:
            if (
                self.bag.get_left() == 0
                and self.check_if_players_hands_empty()
            ):
                print("END OF THE GAME")
                self.game_ending()
            if self.game_mode == "single":
                self.play_round(round, 0)
            else:
                self.play_round(round, 0)
                self.play_round(round, 1)
            round += 1


if __name__ == "__main__":
    game_mode = Prompt.ask(
        "Choose game mode: singleplayer, player vs player (pvp)",
        choices=["single", "pvp"],
    )
    if game_mode == "single":
        player_name = input("Enter your name: ")
        game = Game(game_mode, player_name)
    else:
        first_player_name = input("First player, enter your name: ")
        second_player_name = input("Second player, enter your name: ")
        players_names = [first_player_name, second_player_name]
        game = Game(game_mode, players_names)
    game.play_game()
