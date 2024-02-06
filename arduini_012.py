n = int(input("dammi il numero di valori da sommare: "))
somma = 0

for i in range(n):
    valore = int(input("dammi un valore: "))
    somma += valore

print("La somma dei valori è:", somma)