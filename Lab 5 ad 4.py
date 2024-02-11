from datetime import datetime

# Przyjmujemy daty ostatnich laboratoriów i datę kolokwium
data_laboratoriow = datetime(2024, 1, 15)
data_kolokwium = datetime(2024, 2, 15)

# Obliczamy różnicę czasu
czas_do_kolokwium = data_kolokwium - datetime.now()
dni_od_laboratoriow = datetime.now() - data_laboratoriow

# Wyświetlamy wyniki
print(f"Do kolokwium pozostało {czas_do_kolokwium.days} dni.")
print(f"Od ostatnich laboratoriów minęło {dni_od_laboratoriow.days} dni.")
