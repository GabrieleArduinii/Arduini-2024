num1 = input("Inserisci il primo numero: ")
num2 = input("Inserisci il secondo numero: ")

num1 = int(num1)
num2 = int(num2)

if num1 % 2 == 0 and num2 % 2 == 0:
print("Entrambi i numeri sono pari")
elif num1 % 2 == 0 and num2 % 2 != 0:
print("Il primo numero è pari e il secondo numero è dispari")
elif num1 % 2 != 0 and num2 % 2 == 0:
print("Il primo numero è dispari e il secondo numero è pari")
else:
print("Entrambi i numeri sono dispari")