import time

def start_game():
    print("""
    WARFRAME: EL DESPERTAR DEL TENNO
    ---------------------------------
    Eres un Tenno, un antiguo guerrero de la Era Orokin.
    Despiertas de tu criosueño en un sistema dominado por facciones corruptas y guerreros mecánicos.
    """)
    time.sleep(2)
    despertar()
def despertar():
    print("""
    Abres los ojos en una cápsula de estasis. La alarma suena y escuchas una voz femenina:
    "Tenno, despierta. Nos necesitan. El enemigo está cerca."
    Te rodean soldados Grineer, brutales guerreros clonados.
    """)
    time.sleep(2)
    print("1) Luchar contra los Grineer y abrirse paso a la salida.")
    print("2) Intentar comunicarte con la voz misteriosa y entender la situación.")    
    choice = input("¿Qué decides? (1/2): ")
    if choice == "1":
        print("Desenvainas tu espada y te lanzas a la batalla. Los Grineer caen a tu paso.")
        encuentro_lotus()
    elif choice == "2":
        print("Decides escuchar a la voz. Ella te llama 'Tenno' y promete ayudarte.")
        encuentro_lotus()
    else:
        print("Opción no válida. Intenta de nuevo.")
        despertar()
def encuentro_lotus():
    print("""
    Una figura holográfica aparece: es Lotus, tu mentora.
    "Debes huir, Tenno. El sistema está en guerra y te necesitan."
    Te da acceso a un Warframe: Excalibur, Mag o Volt.
    """)
    time.sleep(2)
    print("1) Elegir Excalibur, el equilibrio entre poder y agilidad.")
    print("2) Elegir Mag, maestra del magnetismo y el control.")
    print("3) Elegir Volt, con velocidad y descargas eléctricas.")
    
    choice = input("¿Qué Warframe eliges? (1/2/3): ")
    if choice in ["1", "2", "3"]:
        print("Te vinculas con tu Warframe y sientes su poder.")
        primer_mision()
    else:
        print("Opción no válida. Intenta de nuevo.")
        encuentro_lotus()
def primer_mision():
    print("""
    Lotus te envía a tu primera misión: sabotear una base Grineer para debilitar su control.
    Llegas a la instalación en tu nave Orbiter, con una misión clara.
    """)
    time.sleep(2)
    print("1) Infiltrarte sigilosamente y eliminar enemigos sin ser visto.")
    print("2) Atacar de frente y arrasar con todo a tu paso.")
    
    choice = input("¿Cómo abordas la misión? (1/2): ")
    if choice == "1":
        print("Te mueves entre las sombras, eliminando enemigos sin activar alarmas.")
        enfrentar_capitano()
    elif choice == "2":
        print("Desatas el caos y haces saltar la alarma. Más enemigos llegan.")
        enfrentar_capitano()
    else:
        print("Opción no válida. Intenta de nuevo.")
        primer_mision()
def enfrentar_capitano():
    print("""
    En lo profundo de la base, un Capitano Grineer te espera.
    "Tenno... Finalmente nos encontramos. No escaparás vivo."
    Es un enemigo formidable, debes decidir tu estrategia.
    """)
    time.sleep(2)
    print("1) Usar tus habilidades de Warframe y atacarlo con todo.")
    print("2) Analizar su patrón de ataque y esperar el momento perfecto.")
    
    choice = input("¿Cómo enfrentas al Capitano? (1/2): ")
    if choice == "1":
        print("Usas tu poder y lo derrotas con una exhibición de habilidades Tenno.")
        escape_base()
    elif choice == "2":
        print("Esperas pacientemente, estudias sus movimientos y encuentras una apertura para vencerlo.")
        escape_base()
    else:
        print("Opción no válida. Intenta de nuevo.")
        enfrentar_capitano()
def escape_base():
    print("""
    La base comienza a autodestruirse. Lotus te guía hacia una salida de emergencia.    
    "Tenno, apresúrate. No podemos perderte ahora."
    """)
    time.sleep(2)
    print("1) Correr directamente hacia la nave y escapar rápidamente.")
    print("2) Buscar información en los sistemas enemigos antes de huir.")
    
    choice = input("¿Qué decides hacer? (1/2): ")
    if choice == "1":
        print("Llegas a la nave y escapas justo antes de la explosión.")
        final()
    elif choice == "2":
        print("Hackeas los sistemas y descubres información sobre un arma secreta Grineer antes de escapar.")
        final()
    else:
        print("Opción no válida. Intenta de nuevo.")
        escape_base()
def final():
    print("""
    Regresas a la nave y Lotus te felicita. Pero la guerra apenas comienza...
    Tu verdadero destino como Tenno aún está por revelarse.
    """)
    time.sleep(2)
    print("CONTINUARÁ...")

if __name__ == "__main__":
    start_game()
