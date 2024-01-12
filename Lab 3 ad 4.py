# a
imie = input("Podaj imię: ")
print("Witaj", imie)

# b
wiek = input("Podaj wiek: ")
print("Twój wiek to:", wiek)

# c
imie_nazwisko = input("Podaj imię i nazwisko (oddzielone spacją): ")
inicjaly = imie_nazwisko[0].upper() + imie_nazwisko.split()[1][0].upper()
print("Inicjały:", inicjaly)

# d
lanuch_pięć_razy = input("Podaj łańcuch: ") * 5
print("Łańcuch pięć razy:", lanuch_pięć_razy)

# e
pierwszy_lanuch = input("Podaj pierwszy łańcuch: ")
drugi_lanuch = input("Podaj drugi łańcuch: ")
trzeci_lanuch = pierwszy_lanuch + drugi_lanuch
print("Połączone łańcuchy:", trzeci_lanuch)

# f
pierwsza_polowa = pierwszy_lanuch[:len(pierwszy_lanuch)//2]
druga_polowa = drugi_lanuch[len(drugi_lanuch)//2:]
trzecia_czesc = pierwsza_polowa + druga_polowa
print("Pierwsza połowa pierwszego i druga połowa drugiego:", trzecia_czesc)