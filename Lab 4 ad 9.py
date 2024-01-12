def fibonacci(n):
    """Funkcja oblicza n-ty wyraz ciągu Fibonacciego."""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("Wynik ciągu fibonacciego :", fibonacci(int(input("Wprowadź który wyraz ciągu fibonacciego ma być wyświetlony: "))))