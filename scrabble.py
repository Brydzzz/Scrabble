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
        # print(hand)

    def play_letter(self):
        given_number = int(input("Number of letter you want to play: "))
        print("Where you want to place your letter")
        given_row = int(input("Number of row: "))
        given_col = int(input("Number of col: "))
        letter = self.hand.get_letter(given_number)
        self.hand.remove_letter(given_number)
        self.board.update_board(letter, given_row, given_col)
        self.print_game()


if __name__ == "__main__":
    game = Game()
    game.print_game()
    game.play_letter()

# print(bag.get_left())
# for i in range(0, 20):
#     print(f"Try {i} result: {bag.draw_letter()}")
# print("\n")
# bag.print_bag()
# print(bag.get_left())
# print("\n\n")
# bag2 = Bag()
# print(bag2.get_left())
