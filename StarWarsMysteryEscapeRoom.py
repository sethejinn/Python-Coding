import time
import random

class EscapeRoom:
    def __init__(self):
        self.solved_room_1 = False
        self.solved_room_2 = False
        self.solved_room_3 = False
        self.solved_room_4 = False
        self.solved_room_5 = False
        self.sith_detected = False
        self.jedi_suspects = ["Master Zora", "Knight Arlos", "Padawan Reyla", "Master Valen"]
        self.jedi_ally = "Master Zora"
        self.player_name = ""
        self.has_discovered_who = False
        self.final_choices = []
        self.discovery = False
        self.eclipse_active = False
        self.sith_infiltrator = None
        self.mission_status = "active"

    def start(self):
        print("¡Bienvenido a 'El Eclipse del Jedi'!")
        self.player_name = input("Por favor, introduce tu nombre, comandante: ")
        print(f"\nBienvenido, {self.player_name}. Prepárate para tu misión secreta en la estación de Atorix.")
        time.sleep(2)
        print("Un eclipse ha bloqueado la Fuerza en la estación. Deberás resolver este misterio sin los poderes Jedi.")
        time.sleep(1)
        print("¡La misión ha comenzado!")
        self.room_1()

    def room_1(self):
        print("\n--- Sala 1: La Cárcel de Seguridad ---")
        print("Te despiertas en una celda oscura, con los ojos nublados por la luz parpadeante.")
        print("Una voz desconocida te habla por el intercomunicador: 'El asesino está entre nosotros. "
              "La estación se destruirá pronto. Si quieres sobrevivir, resuelve los acertijos y descubre la verdad.'")
        print("En el panel de seguridad hay cuatro símbolos: Luz, Oscuridad, Sabiduría, Caos.")
        print("El código para salir depende de encontrar el patrón correcto.")
        
        # Pista del asesinato
        print("\nEncuentras el cadáver de un guardia. Hay algo escrito en su brazo con sangre: 'La luz revela la verdad'.")
        print("Tienes que encontrar el patrón correcto en el panel.")
        
        while not self.solved_room_1:
            user_input = input("Introduce el código de 4 símbolos (Luz, Oscuridad, Sabiduría, Caos): ").lower()
            if user_input == "luz, sabiduría, caos, oscuridad":
                print("¡Código correcto! La puerta de la celda se desbloquea.")
                self.solved_room_1 = True
                time.sleep(1)
                self.room_2()
            else:
                print("Código incorrecto. Intenta nuevamente o escribe 'pista' para recibir ayuda.")
                if user_input.lower() == "pista":
                    print("Pista: El patrón está basado en la naturaleza del asesinato. La luz y la sabiduría revelan la verdad.")

    def room_2(self):
        print("\n--- Sala 2: El Laboratorio de Investigaciones ---")
        print("Has llegado a un laboratorio lleno de equipos y computadoras. Un mensaje parpadea en una de las pantallas: "
              "'El Maestro Jedi Kyros fue asesinado por alguien cercano. La verdad está en el archivo de seguridad.'")
        print("Sin embargo, la puerta al archivo de seguridad está bloqueada por un acertijo.")
        
        # El acertijo en el laboratorio
        print("\nEn la pantalla, aparece una lista de opciones para desbloquear el archivo:")
        print("1. Fuerza de voluntad")
        print("2. Sabiduría Jedi")
        print("3. Traición Sith")
        print("4. Honra Republicana")

        while not self.solved_room_2:
            print("\n¿Qué opción elegirás? Introduce el número de la opción.")
            user_input = input("Opción (1-4): ")
            if user_input == "3":
                print("¡Correcto! El asesino era un Sith infiltrado.")
                self.solved_room_2 = True
                self.sith_detected = True
                self.final_choices.append("El Sith infiltrado")
                self.sith_infiltrator = random.choice(self.jedi_suspects)
                time.sleep(1)
                self.room_3()
            elif user_input == "2":
                print("Sabiduría Jedi... No es la respuesta correcta. Intenta nuevamente.")
            elif user_input == "1":
                print("Fuerza de voluntad... No es la respuesta correcta. Intenta nuevamente.")
            elif user_input == "4":
                print("Honra Republicana... No es la respuesta correcta. Intenta nuevamente.")
            else:
                print("Opción no válida. Elige una opción entre 1 y 4.")

    def room_3(self):
        print("\n--- Sala 3: El Corazón Oscuro ---")
        print("Has llegado al núcleo de la estación. El sistema de autodestrucción está activo, y el temporizador marca 10 minutos.")
        print("Una pantalla muestra la pregunta final: '¿Cómo desactivarás el sistema de autodestrucción?'")
        
        print("\nLas opciones disponibles son:")
        print("1. Utilizar la Fuerza para detenerlo")
        print("2. Desactivar manualmente el sistema desde la consola principal")
        print("3. Destruir la fuente de energía del núcleo")
        print("4. Investigar la conexión Sith")

        while not self.solved_room_3:
            user_input = input("Elige una opción (1-4): ")
            if user_input == "2":
                print("¡Correcto! Has desactivado el sistema de autodestrucción y detenido el desastre.")
                self.solved_room_3 = True
                time.sleep(1)
                self.room_4()
            elif user_input == "1":
                print("La Fuerza no puede detener el sistema de autodestrucción en este caso. Intenta otra opción.")
            elif user_input == "3":
                print("Destruir la fuente de energía del núcleo solo empeoraría las cosas. Intenta otra opción.")
            elif user_input == "4":
                print("Investigando la conexión Sith... ¡Has descubierto que el Sith infiltrado estaba en la misma red de seguridad!")
                self.solved_room_3 = True
                time.sleep(1)
                self.room_4()

    def room_4(self):
        print("\n--- Sala 4: El Confrontamiento Final ---")
        print("Has llegado a la sala donde el Sith se esconde. Con el sistema de autodestrucción desactivado, debes enfrentarte a él.")
        
        # Acertijo sobre quién es el asesino
        print("\nEl Sith se encuentra con una máscara. Solo uno de los cuatro Jedi puede ser el culpable: ")
        for i, jedi in enumerate(self.jedi_suspects):
            print(f"{i+1}. {jedi}")
        
        print("\n¿A quién vas a confrontar?")
        while not self.solved_room_4:
            user_input = input("Introduce el número del Jedi que crees que es el asesino: ")
            if user_input == "1":
                print("¡Incorrecto! No es el Maestro Zora. Era un aliado de los Sith. Vuelves a la sala.")
                time.sleep(2)
                self.room_4()
            elif user_input == "2":
                print("¡Correcto! El Knight Arlos era un Sith infiltrado todo el tiempo.")
                self.solved_room_4 = True
                self.final_choices.append("Knight Arlos")
                time.sleep(2)
                self.room_5()
            elif user_input == "3":
                print("¡Incorrecto! La Padawan Reyla también estaba manipulada por los Sith. Vuelves a la sala.")
                time.sleep(2)
                self.room_4()
            elif user_input == "4":
                print("¡Incorrecto! El Maestro Valen fue otro de los que traicionó la República.")
                time.sleep(2)
                self.room_4()

    def room_5(self):
        print("\n--- Sala 5: La Última Decisión ---")
        print("¡Has llegado al final! El Sith Knight Arlos revela su verdadera identidad. Te da una última oportunidad.")
        print("Te ofrece una elección: unirte a los Sith y destruir la República o resistir y salvarla.")
        
        print("\nTus opciones son:")
        print("1. Unirte a los Sith y destruir la República.")
        print("2. Rechazar la oferta y destruir al Sith, defendiendo la República.")
        
        while not self.discovery:
            user_input = input("Elige una opción (1-2): ")
            if user_input == "1":
                print(f"\nHas elegido unirte a los Sith, {self.player_name}. La República caerá bajo el caos de la oscuridad.")
                self.discovery = True
                self.final_choices.append("Sith")
                self.game_over()
            elif user_input == "2":
                print(f"\n¡Has decidido salvar la República, {self.player_name}! El Sith Knight Arlos es derrotado.")
                self.discovery = True
                self.final_choices.append("Republicano")
                self.victory()

    def game_over(self):
        print("\nFin del juego. El caos y la oscuridad han tomado la galaxia. El Sith ha ganado.")

    def victory(self):
        print("\nFin del juego. La República ha prevalecido. La estación Atorix queda libre de la influencia Sith.")

# Inicio del juego
game = EscapeRoom()
game.start()
