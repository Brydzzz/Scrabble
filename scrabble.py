from board import Board
from bag import Bag
from hand import Hand


class Game:
    def __init__(self):
        self.board = Board()
        self.bag = Bag()
        self.hand = Hand(self.bag)

    def start_game(self):
        print("Board: \n")
        self.board.print_board()
        print(f"\n Your letters: {self.hand}")
        # print(hand)

    def place_letter(self):
        given_number = input("Give the number of letter you want to place: ")
        letter = self.hand.get_letter(int(given_number))
        self.hand.remove_letter(int(given_number))
        self.board.update_board(letter, 1, 2)
        print("Board: \n")
        self.board.print_board()
        print(f"\n Your letters: {self.hand}")


if __name__ == "__main__":
    game = Game()
    game.start_game()
    game.place_letter()

# print(bag.get_left())
# for i in range(0, 20):
#     print(f"Try {i} result: {bag.draw_letter()}")
# print("\n")
# bag.print_bag()
# print(bag.get_left())
# print("\n\n")
# bag2 = Bag()
# print(bag2.get_left())
