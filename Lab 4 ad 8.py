def potega(a, n):
    """Funkcja oblicza n-ty stopień potęgi liczby a."""
    if n == 0:
        return 1
    else:
        return a * potega(a, n-1)

print("Wynik n'tego stopnia potęgi ", potega(int(input("Wprowadź liczbę potęgowaną: ")), int(input("Wprowadź ile razy ma być potęgowana: "))))