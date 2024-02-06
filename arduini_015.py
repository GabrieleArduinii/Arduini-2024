#Arduini

media=0
x =  1
quantita_voti = 0
while x == 1:
    voto = int(input("Inserire voto: "))
    if voto <= 0:      
        x=0
    if voto > 10:
        print("Voto non valido")
    if voto <=10 and voto >=1:
        media=media+voto
        print("Aggiunto alla lista")
        quantita_voti += 1
    
media = media / quantita_voti

print("\nLa media è: ", media)
#-----------------------------------------------------------------------