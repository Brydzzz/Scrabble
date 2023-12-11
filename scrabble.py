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
        print("\n Board: \n")
        self.board.print_board()
        print(f"\n Your letters: {self.hand} \n")

    def place_letter(self):
        given_number = int(input("Enter letter number: "))
        print("Where you want to place your letter?")
        given_row = int(input("Row number: "))
        given_col = int(input("Column number: "))
        letter = self.hand.get_letter(given_number)
        self.hand.remove_letter(given_number)
        self.board.update_board(letter, given_row, given_col)
        self.print_game()

    def letter_round(self):
        self.print_game()
        while True:
            self.place_letter()
            print("Place another letter [A] or end round [E]\n")
            option = input("Enter your choice here: ")
            if option.lower() == "e":
                break
            elif option.lower() == "a":
                pass

    def draw_letters_round(self):
        pass

    def play_round(self):
        self.print_game()
        print("What you want to do?")
        print("[1] Place letters")
        print("[2] Draw new letters")
        action = int(input("Enter number here: "))
        if action == 1:
            self.letter_round()
        else:
            self.draw_letters_round()


if __name__ == "__main__":
    game = Game()
    while True:
        game.play_round()
