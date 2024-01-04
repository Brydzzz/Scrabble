from player import Player
from hand import Hand
from bag import Bag


def test_create_player():
    bag = Bag()
    hand = Hand(bag)
    player = Player(hand, "John")
    assert player.name == "John"
    assert player.words == []
    assert player.points == 0
    assert player.hand == hand


def test_set_words():
    bag = Bag()
    hand = Hand(bag)
    player = Player(hand, "John")
    assert player.words == []
    player.set_words(["hello", "world"])
    assert player.words == ["hello", "world"]


def test_add_words():
    bag = Bag()
    hand = Hand(bag)
    player = Player(hand, "John", ["hello", "world"])
    assert player.words == ["hello", "world"]
    player.add_words(["from"])
    assert player.words == ["hello", "world", "from"]


def test_calculate_points():
    bag = Bag()
    hand = Hand(bag)
    hand._letters = ["A", "A", "A", "A", "A", "A", "A"]
    player = Player(hand, "John", ["hęllo", "world"])
    assert player.words == ["hęllo", "world"]
    player.calculate_points()
    assert player.points == 13
