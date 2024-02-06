
input_voti = input("dammi  i 5 voti: ")

voti = input_voti.split()

voti_validi = 0


voti_sufficienti = 0


for voto in voti:
    voto = int(voto)  
    
    if voto >= 1 and voto <= 10:
        voti_validi += 1
        if voto >= 6:
            voti_sufficienti += 1

print("Voti validi:", voti_validi)
print("Voti sufficienti:", voti_sufficienti)