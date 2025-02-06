import random

palos = ['Oros', 'Copas', 'Espadas', 'Bastos']
numeros = ['1', '2', '3', '4', '5', '6', '7', 'Sota', 'Caballo', 'Rey']

mazo = [f'{numero} de {palo}' for palo in palos for numero in numeros]

random.shuffle(mazo)

def iniciar_juego():
    print("\nBienvenido/a al juego de la Sota!!")
    print("¡Suerte!\n")
    
    intentos = 0
    puntuacion = 0
    limite_intentos = 5  # Limite de intentos

    return intentos, puntuacion, limite_intentos

def sacar_carta():
    carta = mazo.pop()  # Sacamos una carta del mazo
    print(f'Has sacado la carta: {carta}')
    return carta

def es_sota(carta):
    if 'Sota' in carta:
        return True
    return False

def mostrar_estado(intentos, puntuacion, limite_intentos):
    print(f"\nIntentos restantes: {limite_intentos - intentos}")
    print(f"Puntuación actual: {puntuacion}")
    print(f"Cartas restantes en el mazo: {len(mazo)}\n")

def juego():
    global mazo  # Para que no se reinicie el mazo al llamar la función varias veces

    intentos, puntuacion, limite_intentos = iniciar_juego()

    while len(mazo) > 0 and intentos < limite_intentos:
        mostrar_estado(intentos, puntuacion, limite_intentos)
        
        input("Presiona Enter para sacar una carta...")
        
        carta = sacar_carta()
        intentos += 1

        if es_sota(carta):
            puntuacion += 10  # Aumentamos la puntuación si sacamos una Sota
            print("¡Felicidades! Has sacado una Sota. +10 puntos.\n")
        else:
            print("No has sacado la Sota. Sigue intentando.\n")
        
        if intentos >= limite_intentos:
            print("\nHas alcanzado el límite de intentos.")
            break

    print("\nFin del juego.")
    print(f"Tu puntuación final es: {puntuacion} puntos.")
    if puntuacion >= 10:
        print("¡Enhorabuena! ¡Has jugado bien!")
    else:
        print("Sigue practicando, ¡la próxima vez será mejor!")

def reiniciar_juego():
    global mazo
    mazo = [f'{numero} de {palo}' for palo in palos for numero in numeros]  # Reiniciamos el mazo
    random.shuffle(mazo)  # Barajamos de nuevo

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Iniciar el juego")
        print("2. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            juego()
            reiniciar_juego()  # Reiniciamos el mazo para la siguiente ronda
        elif opcion == '2':
            print("¡Gracias por jugar! ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción correcta.")

if __name__ == "__main__":
    menu()
