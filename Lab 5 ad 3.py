import time

czas = int(input("Podaj czas w sekundach: "))

while czas > 0:
    print("Pozostało", czas, "sekund.")
    time.sleep(1)
    czas -= 1

print("Czas minął!")

