età = int(input("Inserisci la tua età: "))

if età >= 0 and età <= 12:
    print("Sei un bambino.")
elif età >= 13 and età <= 19:
    print("Sei un adolescente.")
elif età >= 20 and età <= 64:
    print("Sei un adulto.")
else:
    print("Sei un anziano.")