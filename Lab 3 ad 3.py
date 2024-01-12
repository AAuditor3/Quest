# a
tekst_b = "Python jest super"
indeksy_a = tekst_b[0], tekst_b[-1]
print("Zerowy i ostatni znak:", indeksy_a)

# b
indeksy_b = tekst_b[::2]
print("Co drugi znak, zaczynając od zerowego:", indeksy_b)

# c
indeksy_c = tekst_b[1::3]
print("Co trzeci znak, zaczynając od pierwszego:", indeksy_c)

# d
indeksy_d = tekst_b[9:]
print("Od dziesiątego do ostatniego znaku:", indeksy_d)

# e
indeksy_e = tekst_b[::-1]
print("Od końca do początku:", indeksy_e)