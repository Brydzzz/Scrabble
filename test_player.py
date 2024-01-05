from player import Player
from hand import Hand
from bag import Bag
from constants import HAND_SIZE, HAND_EMPTY_LETTER_SYMBOL


def test_create_player():
    bag = Bag()
    hand = Hand(bag)
    player = Player(hand, "John")
    assert player.name == "John"
    assert player.words == []
    assert player.played_cells == []
    assert player.points == 0
    assert player.hand == hand


def test_set_words():
    bag = Bag()
    hand = Hand(bag)
    player = Player(hand, "John")
    assert player.words == []
    player.set_words(["hello", "world"])
    assert player.words == ["hello", "world"]


def test_add_played_cell():
    bag = Bag()
    hand = Hand(bag)
    player = Player(hand, "John")
    player.add_played_cell((4, 7))
    assert player.played_cells == [(4, 7)]


def test_reset_played_cells():
    bag = Bag()
    hand = Hand(bag)
    player = Player(hand, "John")
    player.add_played_cell((4, 7))
    assert player.played_cells == [(4, 7)]
    player.reset_played_cells()
    assert player.played_cells == []


def test_add_words():
    bag = Bag()
    hand = Hand(bag)
    player = Player(hand, "John", ["hello", "world"])
    assert player.words == ["hello", "world"]
    player.add_words(["from"])
    assert player.words == ["hello", "world", "from"]


def test_calculate_points_hand_not_empty():
    bag = Bag()
    hand = Hand(bag)
    hand._letters = ["A", "A", "A", "A", "A", "A", "A"]
    player = Player(hand, "John", ["hęllo", "world"])
    assert player.words == ["hęllo", "world"]
    player.calculate_points()
    assert player.points == 13


def test_calculate_points_hand_empty():
    bag = Bag()
    hand = Hand(bag)
    hand._letters = [HAND_EMPTY_LETTER_SYMBOL for _ in range(HAND_SIZE)]
    player = Player(hand, "John", ["hęllo", "world"])
    assert player.words == ["hęllo", "world"]
    player.calculate_points()
    assert player.points == 20
