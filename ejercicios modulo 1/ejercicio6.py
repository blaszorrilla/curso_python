numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

if numero1 > numero2:
    print(f"{numero1} es el numero mayor")
elif numero2>numero1:
    print(f"{numero2} es el numero mayor")
else:
    print("Los dos numeros son iguales")
    