# Scrabble

## Autor

Brygida Silawko

## Uruchamianie gry
Aby uruchomić grę należy uruchomić moduł [scrabble.py](scrabble.py)

Do poprawnego działania potrzebne są biblioteki z [requirements.txt](requirements.txt)

## Zadany projekt
Przygotuj program który pozwoli grać w grę scrabble.

Gra polega na układaniu słów z wylosowanych klocków z literkami i dokładaniu ich do planszy tak żeby zdobyć jak najwięcej punktów. Słowa dokładać można tylko w jednym kierunku (pion lub poziom), a po dołożeniu nowego słowa wszystkie zbitki liter na planszy musza mieć sens (Zarówno w pionie jak i w poziomie).

W wersji piprowej proponuję uproszczenie gry do maksymalnie 5-literowych słów (w wersji z botem, żeby ułatwić przeszukiwanie słownika) i zrezygnowanie z pól z dodatkowymi premiami. Do rozwiązania zadania (stworzenia bota) należy wykorzystać słownik np: https://sjp.pl/slownik/growy/

Dokładne reguły, punktacja i liczba płytek z daną literą są dostępne na stronie: http://www.pfs.org.pl/reguly.php

## Podział programu

### Klasy:
- [Bag](bag.py) - reprezentuje worek z literkami
- [Board](board.py) - reprezentuje planszę
- [Hand](hand.py) - reprezentuje rękę gracza
- [Player](player.py) - reprezentuje gracza
- [Game](scrabble.py) - reprezentuje grę Scrabble

## Część refleksyjna

### Podsumowanie wykonanej pracy
Stworzenie gry Scrabble, która:
- działa w terminalu
- posiada dwa tryby gry: singleplayer i player vs player
- korzysta z oficjalnej listy słów dozwolonych w Scrabblach

### Rzeczy, których nie udało się osiągnąć
 - Wpisywanie słów inaczej niż literka po literce (np. podanie słowa, koordynatów pierwszej z literki i kierunku układania). Powód: brak czasu na przerobienie metod walidacji pod takie wpisywanie
 - Zamienić testów z [manual_scrabble_tests.py](manual_scrabble_tests.py) na testy automatyczne. Powód: nie udało mi się z mockować inputów gracza

### Co się zmieniło w stosunku do planowanego rozwiązania
Planowane rozwiązanie miało zawierać tryb gry z botem, ale po konsultacji z prowadzącym zamiast tej funkcjonalność miałam zrobić tryb dla dwóch graczy.