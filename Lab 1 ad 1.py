yo = int(input("Ile masz lat? "))


if yo < 0:
    print("Niepoprawny wiek")

elif yo < 4:
    print("Wchodzisz za darmo")

elif 4 <= yo <= 18:
    print("Bilet 10 zł")

else:
    print("Bilet 20 zł")