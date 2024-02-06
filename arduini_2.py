voti = {}
voti["micheal"] = 6,50
voti["marco"] = 7,50
voti["paolo"] = 8,50
voti["alessio"] = 5,50


for i in  voti.items():
  print(i)


voti["diego"] = 4,50
for i in voti.items():
   print(i)



controlla  = str(input("quale studente controllare"))


if controlla in voti:
   print(voti[controll])


else: 
    
    print("studente non trovato")