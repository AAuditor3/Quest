while True:
    try:
        number = int(input("Podaj liczbę całkowitą (liczba ujemna zakończy pętlę): "))

        if number < 0:
            print("Wprowadzono liczbę ujemną. Koniec programu.")
            break  # Wyjście z pętli
        else:
            print(f"Wprowadzono: {number}")

    except ValueError:
        print("Nieprawidłowe dane. Podaj liczbę całkowitą.")