frase = input("Ingrese una frase: ")
contador_a = 0
for caracter in frase:
    caracter=caracter.lower()
    if caracter == 'a':
        contador_a += 1
print(f"La letra a aparece {contador_a} veces en la frase")
