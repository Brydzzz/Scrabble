from board import Board
from bag import Bag
from hand import Hand


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
        print(f"\n Your letters: {self.hand} \n")

    def place_letter(self):
        """
        Gets input from player and places letter on board.
        Then prints updated board
        """
        given_number = int(input("Enter letter number: "))
        print("Where do you want to place your letter?")
        given_row = int(input("Row number: "))
        given_col = int(input("Column number: "))
        letter = self.hand.get_letter(given_number)
        self.hand.remove_letter(given_number)
        self.board.update_board(letter, given_row, given_col)
        self.print_game()

    def letter_round(self):
        """
        When player chooses place letter option in play_round() this executes.
        """
        while True:
            self.place_letter()
            print("Place another letter [A] or end round [E]\n")
            option = input("Enter your choice here: ")
            if option.lower() == "e":
                break
            elif option.lower() == "a":
                pass

    def redraw_letters_round(self):
        """
        Executes when player chooses draw new letters option in play_round()
        """
        number_of_letters = int(
            input("Enter how many letter you want to redraw: ")
        )
        choosen_letter_indexs = []
        for _ in range(number_of_letters):
            letter_index = int(
                input("Enter number of letter you want to redraw: ")
            )
            fixed_letter_index = letter_index - 1
            choosen_letter_indexs.append(fixed_letter_index)
        for index in choosen_letter_indexs:
            new_letter = self.bag.draw_letter()
            self._hand.replace_letter(new_letter, index)

    def play_round(self, round):
        """
        method responsible for player's journey
        """
        print(f"\nROUND: {round}")
        self.print_game()
        print("What you want to do?")
        print("[1] Place letters")
        print("[2] Draw new letters")
        print("[3] Exit game")
        action = int(input("Enter number here: "))
        if action == 1:
            self.letter_round()
            self.hand.draw_to_seven_letters(self._bag)
        elif action == 2:
            self.redraw_letters_round()
        else:
            exit()


if __name__ == "__main__":
    game = Game()
    round = 1
    while True:
        game.play_round(round)
        round += 1
