num1 = int(input("dammi il primo numero: "))
num2 = int(input("dammi il secondo numero: "))
num3 = int(input("dammi il terzo numero: "))

if num1 >= num2 and num1 >= num3:
    print("Il num maggiore è:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Il num maggiore è:", num2)
else:
    print("Il num maggiore è:", num3)