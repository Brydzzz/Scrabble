from bag import Bag


def test_create_bag():
    bag = Bag()
    assert bag.inside == {
        "A": 9,
        "Ą": 1,
        "B": 2,
        "C": 3,
        "Ć": 1,
        "D": 3,
        "E": 7,
        "Ę": 1,
        "F": 1,
        "G": 2,
        "H": 2,
        "I": 8,
        "J": 2,
        "K": 3,
        "L": 3,
        "Ł": 2,
        "M": 3,
        "N": 5,
        "Ń": 1,
        "O": 6,
        "Ó": 1,
        "P": 3,
        "R": 4,
        "S": 4,
        "Ś": 1,
        "T": 3,
        "U": 2,
        "W": 4,
        "Y": 4,
        "Z": 5,
        "Ź": 1,
        "Ż": 1,
        "?": 2,
    }


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
    assert drawn_letter == "_"
