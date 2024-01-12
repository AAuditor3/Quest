rachunki_pradu = {'styczeń': 150, 'luty': 180, 'marzec': 120, 'kwiecień': 200}
wartosci = list(rachunki_pradu.values())

# a
maksimum = max(wartosci)
minimum = min(wartosci)
suma = sum(wartosci)
srednia = suma / len(wartosci)
print(f"Maksimum: {maksimum}, Minimum: {minimum}, Suma: {suma}, Średnia: {srednia}")

# b
ostatni_miesiac = 'kwiecień'
if rachunki_pradu[ostatni_miesiac] > srednia:
    print("Zacznij oszczędzać")
else:
    print("Jesteś bezpieczny")