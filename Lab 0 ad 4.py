import random

road = float(input("Podaj przebytą drogę w kilometrach "))
avrConsumption = float(input("Podaj średnie spalanie samochodu w litrach na 100km "))
consumption = road * avrConsumption/100
fuelCost = 6.5 * consumption
print(f"Przewidywane zużycie paliwa na trasie {road}km wynosi {consumption}l a koszt takiej wyprawy to {fuelCost}zł")

los = random.randint(1, 100000)
losConsumption = los *avrConsumption/100
losFuel = 6.5 * losConsumption
print(f"Przewidywane zużycie paliwa na losowej trasie {los}km wynosi {losConsumption}l a koszt takiej wyprawy to {losFuel}zł")