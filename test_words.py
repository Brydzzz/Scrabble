from words import check_the_words


def test_check_the_words_true():
    words = [
        "szmaragd",
        "archipelag",
        "filharmonia",
        "pergola",
        "magnolia",
        "kontrabas",
        "kaskadowy",
        "efemeryczny",
        "liryczny",
        "hipopotam",
        "katakumby",
        "szopka",
        "oratorium",
        "katakumby",
        "szopka",
        "oratorium",
        "ambrozja",
        "fantazyjny",
        "konglomerat",
        "symulacja",
        "egzotyczny",
        "plenarny",
        "katedra",
        "kapilara",
        "efektowny",
        "eksplozja",
        "kombinacja",
        "maksymalny",
        "perspektywa",
        "kwintesencja",
    ]
    assert check_the_words(words) is True


def test_check_the_words_false():
    words = [
        "zmargads",
        "arhipelag",
        "firhalmonia",
        "porgela",
        "mognola",
        "kontrabas",
        "kaskodawy",
        "efemerycnzy",
        "liryczny",
        "hipopotam",
        "katakumby",
        "sopzka",
    ]
    assert check_the_words(words) is False
