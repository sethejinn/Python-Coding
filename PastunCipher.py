def cifrar_texto(texto):
    resultado = ""
    alfabeto_espanol = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_pashto = "وزيدوارښيګکڅجچپتسدفبغعظړږ"
    
    for caracter in texto:
        if caracter.isalpha():
            indice = alfabeto_espanol.find(caracter.lower())
            if indice != -1:
                if caracter.islower():
                    resultado += alfabeto_pashto[(indice + 3) % len(alfabeto_pashto)]
                else:
                    resultado += alfabeto_pashto[(indice + 3) % len(alfabeto_pashto)].upper()
            else:
                resultado += caracter
        else:
            resultado += caracter
    
    return resultado

def descifrar_texto(texto):
    resultado = ""
    alfabeto_espanol = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_pashto = "وزيدوارښيګکڅجچپتسدفبغعظړږ"
    
    for caracter in texto:
        if caracter.isalpha():
            indice = alfabeto_pashto.find(caracter.lower())
            if indice != -1:
                if caracter.islower():
                    resultado += alfabeto_espanol[(indice - 3) % len(alfabeto_pashto)]
                else:
                    resultado += alfabeto_espanol[(indice - 3) % len(alfabeto_pashto)].upper()
            else:
                resultado += caracter
        else:
            resultado += caracter
    
    return resultado

def menu():

    print("¡Bienvenida al Cifrastun de MG!")

    while True:
        print("\nMenu:")
        print("1. Cifrar un texto")
        print("2. Descifrar un texto")
        print("3. Salir")
        opcion = input("Introduce tu opción: ")

        if opcion == '1':
            texto = input("Introduce el texto a cifrar: ")
            texto_cifrado = cifrar_texto(texto)
            print("Texto cifrado:", texto_cifrado)

        elif opcion == '2':
            texto = input("Introduce el texto a descifrar: ")
            texto_descifrado = descifrar_texto(texto)
            print("Texto descifrado:", texto_descifrado)

        elif opcion == '3':
            print("Gracias por utilizarme. ¡Nos vemos luego!")
            break

        else:
            print("Opción inválida.")

menu()
