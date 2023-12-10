liczba1 = int(input("Podaj pierwszą liczbę całkowitą: "))
liczba2 = int(input("Podaj drugą liczbę całkowitą: "))

print("\nLiczby parzyste od mniejszej do większej:")
if liczba1 <= liczba2:
    for i in range(liczba1, liczba2 + 1):
        if i % 2 != 0:
            continue
        print(i)
else:
    for i in range(liczba1, liczba2 - 1, -1):
        if i % 2 != 0:
            continue
        print(i)
