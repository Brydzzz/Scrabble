from hand import Hand
from bag import Bag
from constants import HAND_SIZE, HAND_EMPTY_LETTER_SYMBOL
from copy import deepcopy


def test_create_hand():
    bag = Bag()
    hand = Hand(bag)
    assert len(hand.letters) == HAND_SIZE


def test_str_hand(monkeypatch):
    def fake_generate_hand(w):
        return ["A", "B", "C", "D", "E", "F", "G"]

    monkeypatch.setattr("bag.Bag.generate_hand", fake_generate_hand)
    bag = Bag()
    hand = Hand(bag)
    assert str(hand) == "| A | B | C | D | E | F | G |"


def test_get_letter(monkeypatch):
    def fake_generate_hand(w):
        return ["A", "B", "C", "D", "E", "F", "G"]

    monkeypatch.setattr("bag.Bag.generate_hand", fake_generate_hand)
    bag = Bag()
    hand = Hand(bag)
    assert hand.get_letter(1) == "A"


def test_remove_letter(monkeypatch):
    def fake_generate_hand(w):
        return ["A", "B", "C", "D", "E", "F", "G"]

    monkeypatch.setattr("bag.Bag.generate_hand", fake_generate_hand)
    bag = Bag()
    hand = Hand(bag)
    assert hand.get_letter(1) == "A"
    hand.remove_letter(1)
    assert hand.get_letter(1) == HAND_EMPTY_LETTER_SYMBOL


def test_replace_letter():
    bag = Bag()
    hand = Hand(bag)

    hand.replace_letter("W", 3)
    assert hand.letters[3] == "W"


def test_hand_to_previous_state(monkeypatch):
    def fake_generate_hand(w):
        return ["A", "B", "C", "D", "E", "F", "G"]

    monkeypatch.setattr("bag.Bag.generate_hand", fake_generate_hand)
    bag = Bag()
    hand = Hand(bag)
    assert hand.letters == ["A", "B", "C", "D", "E", "F", "G"]
    previous_letters = deepcopy(hand.letters)
    hand.replace_letter("K", 0)
    assert hand.letters == ["K", "B", "C", "D", "E", "F", "G"]
    hand.hand_to_previous_state(previous_letters)
    assert hand.letters == ["A", "B", "C", "D", "E", "F", "G"]


def test_draw_to_seven_letters(monkeypatch):
    def fake_generate_hand(w):
        return ["A", "B", "C", "D", "E", "F", "G"]

    drawn_letters = iter(["K", "O", "T"])
    monkeypatch.setattr("bag.Bag.generate_hand", fake_generate_hand)
    monkeypatch.setattr("bag.Bag.draw_letter", lambda _: next(drawn_letters))
    bag = Bag()
    hand = Hand(bag)
    assert hand.letters == ["A", "B", "C", "D", "E", "F", "G"]
    hand.replace_letter(HAND_EMPTY_LETTER_SYMBOL, 0)
    hand.replace_letter(HAND_EMPTY_LETTER_SYMBOL, 1)
    hand.replace_letter(HAND_EMPTY_LETTER_SYMBOL, 2)
    assert hand.letters == [
        HAND_EMPTY_LETTER_SYMBOL,
        HAND_EMPTY_LETTER_SYMBOL,
        HAND_EMPTY_LETTER_SYMBOL,
        "D",
        "E",
        "F",
        "G",
    ]
    hand.draw_to_seven_letters(bag)
    assert hand.letters == ["K", "O", "T", "D", "E", "F", "G"]


def test_draw_to_seven_letters_empty_bag(monkeypatch):
    def fake_generate_hand(w):
        return ["A", "B", "C", "D", "E", "F", "G"]

    monkeypatch.setattr("bag.Bag.generate_hand", fake_generate_hand)
    bag = Bag()
    hand = Hand(bag)
    assert hand.letters == ["A", "B", "C", "D", "E", "F", "G"]
    hand.replace_letter(HAND_EMPTY_LETTER_SYMBOL, 0)
    hand.replace_letter(HAND_EMPTY_LETTER_SYMBOL, 1)
    hand.replace_letter(HAND_EMPTY_LETTER_SYMBOL, 2)
    assert hand.letters == [
        HAND_EMPTY_LETTER_SYMBOL,
        HAND_EMPTY_LETTER_SYMBOL,
        HAND_EMPTY_LETTER_SYMBOL,
        "D",
        "E",
        "F",
        "G",
    ]
    bag._inside = {
        "A": 0,
        "Ą": 0,
        "B": 0,
        "C": 0,
        "Ć": 0,
        "D": 0,
        "E": 0,
        "Ę": 0,
        "F": 0,
        "G": 0,
        "H": 0,
        "I": 0,
        "J": 0,
        "K": 0,
        "L": 0,
        "Ł": 0,
        "M": 0,
        "N": 0,
        "Ń": 0,
        "O": 0,
        "Ó": 0,
        "P": 0,
        "R": 0,
        "S": 0,
        "Ś": 0,
        "T": 0,
        "U": 0,
        "W": 0,
        "Y": 0,
        "Z": 0,
        "Ź": 0,
        "Ż": 0,
        "?": 0,
    }
    hand.draw_to_seven_letters(bag)
    assert hand.letters == [
        HAND_EMPTY_LETTER_SYMBOL,
        HAND_EMPTY_LETTER_SYMBOL,
        HAND_EMPTY_LETTER_SYMBOL,
        "D",
        "E",
        "F",
        "G",
    ]
