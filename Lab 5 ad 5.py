import keyword

slowa = ["for", "print", "break", "done", "bad"]

for slowo in slowa:
    if slowo in keyword.kwlist:
        print(f"{slowo} jest słowem kluczowym w Pythonie.")
    else:
        print(f"{slowo} nie jest słowem kluczowym w Pythonie.")
