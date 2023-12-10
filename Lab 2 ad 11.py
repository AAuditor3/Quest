tekst = "Python jest super"

zerowy_indeks = tekst[0]
print("Znak o zerowym indeksie:", zerowy_indeks)

ostatni_indeks = tekst[-1]
print("Ostatni znak:", ostatni_indeks)

co_drugi_zerowy = tekst[::2]
print("Co drugi znak, zaczynając od zerowego:", co_drugi_zerowy)

co_trzeci_pierwszy = tekst[1::3]
print("Co trzeci znak, zaczynając od pierwszego:", co_trzeci_pierwszy)

od_dziesatego_do_konca = tekst[9:]
print("Od dziesiątego do ostatniego znaku:", od_dziesatego_do_konca)

od_konca_do_poczatku = tekst[::-1]
print("Od końca do początku:", od_konca_do_poczatku)
