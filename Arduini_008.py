
n = int(input("metti il numero di pasticcini: "))

    scatole_5 = n // 5

    rim = n % 5

    scatole_3 = rim // 3

    rim = rim % 3

    scatole_1 = rim

    
print("Scatole da 5 pezzi:" + str (scatole_5))
print("Scatole da 3 pezzi:" + str (scatole_3))
print("Scatole da 1 pezzo:" + str (scatole_1))