from bag import Bag
from constants import LETTERS_BAG_COUNT, HAND_EMPTY_LETTER_SYMBOL


def test_create_bag():
    bag = Bag()
    assert bag.inside == LETTERS_BAG_COUNT


def test_draw_letter_typical(monkeypatch):
    bag = Bag()
    a_count = bag.inside["A"]

    def draw_a(w):
        return "A"

    monkeypatch.setattr("random.choice", draw_a)
    drawn_letter = bag.draw_letter()
    assert bag.inside["A"] == a_count - 1
    assert drawn_letter == "A"


def test_draw_letter_no_letters(monkeypatch):
    bag = Bag()
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

    def draw_a(w):
        return "A"

    monkeypatch.setattr("random.choice", draw_a)
    drawn_letter = bag.draw_letter()
    assert bag.inside["A"] == 0
    assert drawn_letter == HAND_EMPTY_LETTER_SYMBOL


def test_draw_letter_drawn_letter_not_available(monkeypatch):
    bag = Bag()
    bag._inside["A"] = 0
    b_count = bag.inside["B"]
    mock_choice = iter(["A", "B"])
    monkeypatch.setattr("random.choice", lambda _: next(mock_choice))
    drawn_letter = bag.draw_letter()
    assert bag.inside["A"] == 0
    assert bag.inside["B"] == b_count - 1
    assert drawn_letter == "B"
