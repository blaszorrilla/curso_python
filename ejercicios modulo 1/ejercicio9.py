frase = input("Ingrese una frase: ")
vocales = ""
vocales_lista = ['a','e','i','o','u','A','E','I','O','U']
for caracter in frase:
    if caracter in vocales_lista:
        vocales += caracter +str(" ")
if len(vocales) > 0:
    print("Las vocales que aparecen en la frase son: ",vocales)
else:
    print("No se encontraron vocales en la frase")