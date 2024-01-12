import random

n = int(input("Podaj liczbę ciągów: "))
x = int(input("Podaj długość ciągów: "))

lista_ciagow = [''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(x)) for _ in range(n)]
krotka_ciagow = tuple(lista_ciagow)

# a
ilosc_znakow = sum(len(ciag) for ciag in krotka_ciagow)
print(f"a. Ilość znaków w liście: {ilosc_znakow}")

# b
ilosc_liter_k = sum(ciag.count('k') for ciag in krotka_ciagow)
print(f"b. Ilość liter 'k' w liście: {ilosc_liter_k}")

# c
ilosc_ciągów_kt = sum(ciag.count('kt') for ciag in krotka_ciagow)
print(f"c. Ilość ciągów 'kt' w liście: {ilosc_ciągów_kt}")

# d
s = input("Podaj wartość s: ")
ilosc_ciagow_dluzszych_niz_s = sum(1 for ciag in krotka_ciagow if len(ciag) > len(s))
print(f"d. Ilość ciągów dłuższych niż {s}: {ilosc_ciagow_dluzszych_niz_s}")