from hand import Hand
from bag import Bag


def test_replace_letters():
    bag = Bag()
    hand = Hand(bag)

    hand.replace_letter("W", 3)
    assert hand.letters[3] == "W"
