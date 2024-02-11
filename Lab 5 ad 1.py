import random

# Losowanie szczęśliwego numerka dla grupy
szczesliwy_numer = random.randint(1, 31)
print("Szczęśliwy numer dla Twojej grupy to: ", szczesliwy_numer)

roczniki = [1990, 1985, 2000, 1998, 1995, 1980]

# Losowanie szczęśliwego rocznika
szczesliwy_rocznik = random.choice(roczniki)
print("Szczęśliwy rocznik to: ", szczesliwy_rocznik)

# Generowanie listy liczb od 1 do 49
liczby = list(range(1, 50))

# Losowanie 6 kul z listy liczb
wylosowane = random.sample(liczby, 6)
print("Wylosowane liczby to: ", wylosowane)