def pole_trapezu(a, b, h):
    """Funkcja oblicza pole trapezu o zadanych wymiarach: a, b, h."""
    return 0.5 * (a + b) * h

print("Pole trapezu to", pole_trapezu(int(input("Wprowadź długość boku a: ")), int(input("Wprowadź długość boku b: ")), int(input("Wprowadź długość boku c: "))))