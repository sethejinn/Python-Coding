import re

def obtener_actividad(dia, hora):
    if dia in ["Lunes", "Martes", "Miércoles", "Jueves"]:
        if hora >= "00:00" and hora < "06:00":
            return "Durmiendo"
        elif hora >= "06:00" and hora < "07:30":
            return "Desayunando"
        elif hora >= "07:30" and hora < "08:00":
            return "En transporte hacia el trabajo"
        elif hora >= "08:00" and hora < "15:00":
            return "Trabajando"
        elif hora >= "15:00" and hora < "18:00":
            if dia in ["Martes", "Jueves"]:
                return "Estudiando"
            else:
                return "Descansando"
        elif hora >= "18:30" and hora < "20:00":
            return "Tiempo de libre organización"
        else:
            return "Descansando"
    elif dia == "Viernes":
        if hora == "16:00":
            return "Durmiendo siesta"
        elif hora >= "00:00" and hora < "06:00":
            return "Durmiendo"
        else:
            return "Descansando"
    else:
        if hora >= "00:00" and hora < "06:00":
            return "Durmiendo"
        else:
            return "Descansando"

def obtener_hora():
    while True:
        hora = input("¿Qué hora es?: ")
        if re.match(r'^\d{1,2}(\.|:)\d{2}$', hora):
            return hora
        else:
            print("Formato de hora inválido. ")

def main():
    print("¡Bienvenido al Organizador!")
    while True:
        print("1. Introduce día y hora")
        print("2. Finalizar")
        opcion = input("¿Qué quieres hacer?: ")
        
        if opcion == "1":
            dia = input("¿Qué día de la semana es hoy?: ")
            hora = obtener_hora()

            actividad = obtener_actividad(dia.capitalize(), hora)

            print("Deberías estar:", actividad)
        elif opcion == "2":
            print("¡Nos vemos luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
