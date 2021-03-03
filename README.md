Domowa biblioteka filmów.

Wyświetlanie domowej biblioteki filmów nigdy nie było takie brzydkie! Dodawaj, modyfikuj i wyświetlaj swoje ulubione filmy!

Strona startowa "./collections/" wyświetla listę filmów zawartych w pliku "collection.json"
Pod listą filmów znajduje się forumlarz do dodawania nowych pozycji.
W formularzu, TYTUŁ jest pozycją obowiązkową.
Każdy tytuł filmu prowadzi do widoku pozwalającego na modyfikacje zawartych tam treści(opis, status obejrzenia, rok produkcji).

Druga część programu to API:

Dostępne pod adresem "./api/v1/collections/" oraz dla poszczególnych pozycji "/api/v1/collections/numer_pozycji".

- Zwracane dane są w formacie json
- Wyświetlenie całej biblioteki oraz poszczególnych filmów (GET)
- Dodawanie nowych pozycji (POST)
- Usuwaniu elementów biblioteki (DELETE)
- Modyfikacji istniejących filmów (PUT)

Szablony:
"collections.html" - "Strona główna" - Wyświetla biblioteke oraz forumlarz .
"single.html" - Widok dla poszczególnego elementu.

Forms:
"forms.py" - Formularz napisany za pomocą modułu WTForms do dodawania nowych filmów.

Models:
"models.py" - Tworzy instancje klasy Movie(). Działania na liście słowników(kolekcji filmów).
