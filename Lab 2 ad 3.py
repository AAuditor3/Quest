while True:
    try:
        number = int(input("Podaj liczbę całkowitą (liczba ujemna zakończy pętlę): "))

        if number < 0:
            print("Wprowadzono liczbę ujemną. Koniec programu.")
            break
        else:
            print(f"Wprowadzono: {number}")

    except ValueError:
        print("Nieprawidłowe dane. Podaj liczbę całkowitą.")