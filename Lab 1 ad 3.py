a = float(input("Wprowadź pierwszą cyfrę: "))
b = float(input("Wprowadź drugą cyfrę: "))
x = input("Co chcesz zrobić? + | - | * | / | a**b ? ")
działania = {"+": a+b, "-": a-b, "*": a*b, "/": a/b, "a**b": a**b}
print("Wynik działania to " + str(działania[x]))