import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print("¡Bienvenido al juego de Adivina el Número!")
    print("He pensado en un número entre 1 y 100. ¿Puedes adivinar cuál es?")
    while True:
        try:
            intento = int(input("Introduce tu número: "))
            intentos += 1
            if intento < numero_secreto:
                print("Demasiado bajo. Inténtalo de nuevo.")
            elif intento > numero_secreto:
                print("Demasiado alto. Inténtalo de nuevo.")
            else:
                print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")
if __name__ == "__main__":
    adivina_el_numero()
