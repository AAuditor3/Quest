x = 1
print("Równanie kwadratowe: ax^2+bx+c")
a = float(input("Wprowadź a "))
b = float(input("Wprowadź b "))
c = float(input("Wprowadź c "))

kwad = a * (x**2) + b * x + c == 0
delta = b**2 - 4 * a * c
pierwDelta = delta**(1/2)
x0 = -1 * b / 2 * a
x1 = -1 * b - (pierwDelta)/2 * a
x2 = -1 * b + (pierwDelta)/2 * a

if delta < 0:
    print(f"Delta wynosi {delta} i jest mniejsza od 0")
    print("Nie ma rozwiązań")
elif delta == 0:
    print(f"Delta wynosi {delta} i jest równa 0")
    print (f"Wynik to x={x0}")
elif delta > 0:
    print(f"Delta wynosi {delta} i jest większa od 0")
    print (f"Wynik to x1={x1} oraz x2={x2}")