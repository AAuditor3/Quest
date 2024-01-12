import math
def pole_trojkata(a, b, c):
    """Funkcja oblicza pole trójkąta o bokach a, b, c."""
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    else:
        print("Błędne dane. Trójkąt o podanych bokach nie istnieje.")

print("Pole trójkąta wynosi: ", pole_trojkata(int(input("Wprowadź długość boku a: ")), int(input("Wprowadź długość boku b: ")), int(input("Wprowadź długość boku c: "))))