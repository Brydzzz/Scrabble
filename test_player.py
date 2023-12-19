from player import Player


def test_create_player():
    player = Player("John")
    assert player.name == "John"
    assert player.words == []
    assert player.points == 0


def test_set_words():
    player = Player("John")
    assert player.words == []
    player.set_words(["hello", "world"])
    assert player.words == ["hello", "world"]


def test_add_word():
    player = Player("John", ["hello", "world"])
    assert player.words == ["hello", "world"]
    player.add_word("from")
    assert player.words == ["hello", "world", "from"]


def test_calculate_points():
    player = Player("John", ["hęllo", "world"])
    assert player.words == ["hęllo", "world"]
    player.calculate_points()
    assert player.points == 20
