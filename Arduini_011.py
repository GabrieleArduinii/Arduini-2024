
num_fotocopie = int(input("Inserisci il numero di fotocopie da effettuare: "))
n_cliente = input("Inserisci il nome del cliente: ")
rilegatura = input("La fotocopia è da rilegare? (sì/no): ")
ris=0
if  rilegatura == "si" : 
    rilegature_text= "compresa la rilegatura"
    ris=1.80
else: 
    rilegatura_text = " "

if 1 <= num_fotocopie <= 19:
    costo_unitario = 0.10
elif 20 <= num_fotocopie <= 100:
    costo_unitario = 0.08
else:
    num_fotocopie>100
    costo_unitario = 0.05
    

costo_totale = num_fotocopie * costo_unitario+ris


print(f"Gentile Sig.{n_cliente }il suo preventivo è di{costo_totale }euro {rilegatura_text} .")


