from math import sqrt
def entrata():
    a = int(input("inserisci un numero:"))
    b = int(input("inserisci un numero:"))
    c = int(input("inserisci un numero:"))
    return a,b,c
def elaborazione(a,b,c):
    soluzione1=0
    soluzione2=0
    delta=b*b-4*a*c
    if delta<0:
        print("delta è negativa ,l'equazione è impossibile")
    if delta==0:
        soluzione1=b/2*a
    if delta>0:
        soluzione1= b +sqrt(delta)/2*a
        soluzione2= b +sqrt(delta)/2*a
    return soluzione1,soluzione2
def uscita(soluzione1,soluzione2):
    print(soluzione1)
    print(soluzione2)


a,b,c=entrata()  
soluzione1,soluzione2=elaborazione(a,b,c) 
uscita(soluzione1,soluzione2)