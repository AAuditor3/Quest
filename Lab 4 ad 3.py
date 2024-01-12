def informacje_o_osobie(imie, wiek=20):
    """Funkcja wypisuje na ekranie imię i wiek danej osoby."""
    print(f"Imię: {imie}, Wiek: {wiek}")
print(informacje_o_osobie.__doc__)
informacje_o_osobie(input("Wprowadź imie: "), int(input("Wprowadź wiek osoby: ")))