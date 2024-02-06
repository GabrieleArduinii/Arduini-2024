
anno = int(input("Inserisci un anno: "))

if anno > 0 and anno < 2100:
if anno % 400 == 0 or (anno % 4 == 0 and anno % 100 != 0):
print("L'anno", anno, "è bisestile.")
else:
print("L'anno", anno, "non è bisestile.")
else:
print("L'anno inserito non è valido.