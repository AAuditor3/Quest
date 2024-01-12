def bmi_status(waga, wzrost):
    """Funkcja oblicza wskaźnik BMI i informuje użytkownika o jego zakresie."""
    bmi = waga / (wzrost / 100)**2
    print("BMI:", bmi)
    if bmi < 18.5:
        print("Niedowaga")
    elif 18.5 <= bmi < 24.9:
        print("Waga prawidłowa")
    elif 25 <= bmi < 29.9:
        print("Nadwaga")
    else:
        print("Otyłość")

print("Obliczanie Twojego BMI:")
bmi_status(int(input("Wprowadź wagę w kilogramach ")), int(input("Wprowadź swój wzrost w centymetrach ")))