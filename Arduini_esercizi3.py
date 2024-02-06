def is_bisestile(anno):
    if (Anno % 4 == 0 and Anno % 100 != 0) or (Anno % 400 == 0):
        return True
    else:
        return False

Giorno = int(input("Giorno: "))
Mese = int(input("Mese: "))
Anno = int(input("Anno: "))



if Mese < 1 or Mese > 12:
    print("Data non valida")
    
else:
  
    if Mese == 1 or Mese == 3 or Mese == 5 or Mese == 7 or Mese == 8 or Mese == 10 or Mese == 12:
        Massimo_Giorni = 31
    elif Mese == 4 or Mese == 6 or Mese == 9 or Mese == 11:
        Massimo_Giorni = 30
    else:  
        if is_bisestile(Anno):
            Massimo_Giorni = 29
        else:
            Massimo_Giorni = 28

    if Giorno < 1 or Giorno > Massimo_Giorni:
        print("Data non valida")
    else:
        print("Data valida")
        
        


Giorno: 31
Mese: 4
Anno: 2021


Giorno: 29
Mese: 2
Anno: 2020