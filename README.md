# ex-panda
Wersja beta 0.2
Developed by Email Zelman

## Konfiguracja

- Plik abbrv_list.txt powinien być sformatowany w następujący sposób (klucz i wartość w jednej linii, w pojedynczych apostrofach, oddzielone 
spacją):
'skrt' 'nowy text ktory pojawi sie w miejscu skrt'


Jeśli chcemy dodać znak nowej linii, w danym miejscu należy umieścić \n, przykład:

    'txt' 'bla bla bla\nnowa linia\nbla bla bla'

Co da nam wynik:
    
    bla bla bla
    nowa linia
    bla bla bla


WAŻNE!!! Jeśli chcemy używać apostrofów w części nowego tekstu, należy je wy-escapeować znakiem \

Przykład:
   
    '_hi' 'Hello, this is techstop\'s Emil speaking'

Wynik:

    Hello, this is techstop's Emil speaking

Nie używajcie apostrofów w sekcji tesktu podmienianego bo wszystko sie zdupczy i program się nie uruchomi.

    'a'b' 'nowy text' <--- Źle

Polskie znaki na ten moment nie są wspierane, tylko `ASCII`
