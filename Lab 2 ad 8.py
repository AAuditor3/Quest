n = int(input("Podaj liczbę naturalną n: "))
a = float(input("Podaj pierwszy wyraz ciągu (a): "))
r = float(input("Podaj różnicę ciągu (r): "))

print(f"Następujące {n} elementy ciągu arytmetycznego:")
for i in range(n):
    element = a + i * r
    print(element, end=", ")
