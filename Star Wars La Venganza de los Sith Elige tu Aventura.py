import time

def start_game():
    print("""
    STAR WARS: EPISODIO III - LA VENGANZA DE LOS SITH
    --------------------------------------------------
    Juegas como Anakin Skywalker, el Caballero Jedi más poderoso de la galaxia.
    Tus decisiones afectarán el desarrollo de los eventos, pero ten cuidado...
    La línea entre el Lado Luminoso y el Lado Oscuro es delgada.
    """)
    time.sleep(2)
    primera_decision()
def primera_decision():
    print("""
    La galaxia está en guerra. Los Separatistas han secuestrado al Canciller Palpatine,
    y tú y Obi-Wan Kenobi lideran un asalto para rescatarlo a bordo del Crucero de Grievous.
    """)
    time.sleep(2)
    print("1) Seguir el plan de Obi-Wan y mantener la calma.")
    print("2) Atacar impulsivamente a los droides y llegar al Canciller lo antes posible.")
    
    choice = input("¿Qué decides? (1/2): ")
    if choice == "1":
        print("Sabia decisión. Usas estrategia y avanzas con Obi-Wan de manera efectiva.")
        duelo_con_dooku()
    elif choice == "2":
        print("Tu impaciencia te hace cometer errores, pero logras abrirte paso.")
        duelo_con_dooku()
    else:
        print("Opción no válida. Intenta de nuevo.")
        primera_decision()
def duelo_con_dooku():
    print("""
    Llegas a la sala donde el Conde Dooku mantiene cautivo a Palpatine.
    Obi-Wan es derribado rápidamente, y ahora debes enfrentarte solo a Dooku.
    """)
    time.sleep(2)
    print("1) Atacar con furia, sin contenerte.")
    print("2) Mantener la calma y pelear con disciplina Jedi.")
    choice = input("¿Qué decides? (1/2): ")
    if choice == "1":
        print("Tu ira te da fuerza. Dooku es poderoso, pero lo superas y lo derrotas.")
        matar_dooku()
    elif choice == "2":
        print("Luchas con técnica y logras vencer a Dooku, pero tardas más tiempo.")
        matar_dooku()
    else:
        print("Opción no válida. Intenta de nuevo.")
        duelo_con_dooku()
def matar_dooku():
    print("""
    Derrotas a Dooku y lo desarmas. Palpatine te observa y te dice:
    "Mátalo, es demasiado peligroso para dejarlo vivir."
    """)
    time.sleep(2)
    print("1) Acabar con Dooku y obedecer a Palpatine.")
    print("2) Mostrar piedad y dejarlo con vida.")
    choice = input("¿Qué decides? (1/2): ")
    if choice == "1":
        print("Con un corte, acabas con Dooku. Palpatine sonríe, satisfecho.")
        pesadillas_padme()
    elif choice == "2":
        print("Decides dejarlo vivir, pero Palpatine no está contento con tu decisión.")
        pesadillas_padme()
    else:
        print("Opción no válida. Intenta de nuevo.")
        matar_dooku()
def pesadillas_padme():
    print("""
    Regresas a Coruscant y te reencuentras con Padmé. Te revela que está embarazada.
    Esa misma noche, tienes una pesadilla donde la ves muriendo en el parto.
    """)
    time.sleep(2)
    print("1) Hablar con Yoda sobre la visión.")
    print("2) Confiar en Palpatine y buscar su consejo.")
    choice = input("¿Qué decides? (1/2): ")
    if choice == "1":
        print("Yoda te advierte sobre el miedo a perder y el apego, pero no te da respuestas claras.")
        manipulado_por_palpatine()
    elif choice == "2":
        print("Palpatine te habla de un poder oculto para salvar a Padmé. Siembra dudas en tu mente.")
        manipulado_por_palpatine()
    else:
        print("Opción no válida. Intenta de nuevo.")
        pesadillas_padme()
def manipulado_por_palpatine():
    print("""
    Palpatine te revela que conoce los secretos del Lado Oscuro, e insinúa que puedes
    aprender a salvar a Padmé si confías en él.
    """)
    time.sleep(2)
    print("1) Rechazar su propuesta y confiar en los Jedi.")
    print("2) Seguir escuchando y considerar sus palabras.")
    choice = input("¿Qué decides? (1/2): ")
    if choice == "1":
        print("Intentas resistir, pero las dudas comienzan a carcomerte.")
        orden_66()
    elif choice == "2":
        print("Empiezas a aceptar la posibilidad de que los Jedi no sean tan confiables como creías.")
        orden_66()
    else:
        print("Opción no válida. Intenta de nuevo.")
        manipulado_por_palpatine()
def orden_66():
    print("""
    Palpatine se revela como Darth Sidious y los Jedi intentan arrestarlo.
    Mace Windu casi lo derrota, pero te pide ayuda.
    """)
    time.sleep(2)
    print("1) Ayudar a Mace Windu y traicionar a Palpatine.")
    print("2) Defender a Palpatine y acabar con Windu.")
    choice = input("¿Qué decides? (1/2): ")
    if choice == "1":
        print("Intentas hacer lo correcto, pero Palpatine te traiciona y mata a Windu de todos modos.")
        caida_al_lado_oscuro()
    elif choice == "2":
        print("Atacas a Windu y permites que Palpatine lo mate. Ahora eres Darth Vader.")
        caida_al_lado_oscuro()
    else:
        print("Opción no válida. Intenta de nuevo.")
        orden_66()
def caida_al_lado_oscuro():
    print("""
    Te arrodillas ante Palpatine. Ahora eres su aprendiz, Darth Vader.
    Tu primer acto es liderar el ataque al Templo Jedi...
    """)
    time.sleep(2)
    print("CONTINUARÁ...")
if __name__ == "__main__":
    start_game()
