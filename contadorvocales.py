cadena = "Hola Mundo"
contador = 0

for caracter in cadena:
    if caracter.lower() in {'a', 'e', 'i', 'o', 'u'}:
        contador += 1

print(contador)
