import random

a = random.randint(3, 7)
b = random.randint(3, 7)

X = set(random.randint(0, 10) for _ in range(a))
Y = set(random.randint(0, 10) for _ in range(b))

# a
czy_zawiera_5_X = 5 in X
print(f"a. Zbiór X zawiera liczbę 5: {czy_zawiera_5_X}")

# b
czy_podzbiorem = X.issubset(Y)
print(f"b. Zbiór X jest podzbiorem zbioru Y: {czy_podzbiorem}")

# c
czy_podzbiorem_Y = Y.issubset(X)
print(f"c. Zbiór Y jest podzbiorem zbioru X: {czy_podzbiorem_Y}")

# d
czy_nadzbiorem_X = X.issuperset(Y)
print(f"d. Zbiór X jest nadzbiorem zbioru Y: {czy_nadzbiorem_X}")

# e
czy_nadzbiorem_Y = Y.issuperset(X)
print(f"e. Zbiór Y jest nadzbiorem zbioru X: {czy_nadzbiorem_Y}")

# f
suma_zbiorow = X.union(Y)
print(f"f. Suma zbiorów X i Y: {suma_zbiorow}")

# g
roznica_X_Y = X.difference(Y)
print(f"g. Różnica zbiorów X i Y: {roznica_X_Y}")

# h
roznica_Y_X = Y.difference(X)
print(f"h. Różnica zbiorów Y i X: {roznica_Y_X}")

# i
iloczyn_X_Y = X.intersection(Y)
print(f"i. Iloczyn zbiorów X i Y: {iloczyn_X_Y}")

# j
roznica_symetryczna = X.symmetric_difference(Y)
print(f"j. Różnica symetryczna zbiorów X i Y: {roznica_symetryczna}")

# k
najwyzszy_element = max(X.union(Y))
print(f"k. Najwyższy element w obu zbiorach: {najwyzszy_element}")

# l
pierwszy_element_X = X.pop()
Y.add(pierwszy_element_X)
print(f"l. Usunięto ze zbioru X pierwszy element i dołączono go do zbioru Y.")

# m
Y.update(X)
print(f"m. Przekopiowano wszystkie elementy zbioru X do zbioru Y.")

# n
X.clear()
Y.clear()
print("n. Wyczyszczono oba zbiory.")
