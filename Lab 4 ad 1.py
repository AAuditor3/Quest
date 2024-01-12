import math
def pole_kola(r):
    """Funkcja oblicza pole koła o zadanym promieniu."""
    return math.pi * r**2
r = int(input("Wprowadź długość promienia: "))
print(f"Pole koła przy długości promienia {r} to:" , pole_kola(r))