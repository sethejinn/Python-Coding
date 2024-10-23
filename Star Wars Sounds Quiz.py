import random
import unidecode  # Para manejar la eliminación de acentos

opciones = {
    "fauna": {
        "wampa": "rarrrrrrr",
        "tauntaun": "hooowah",
        "ewok": "yub nub",
        "porg": "grititos agudos",
        "rancor": "gruñido bajo",
        "bantha": "rugido gutural",
        "nexu": "rugido felino",
        "dewback": "graznido reptiliano",
        "kowakian monkey-lizard": "risas y chillidos",
        "gundark": "gruñido fiero",
        "sarlacc": "rugido profundo",
        "mynock": "chillido agudo",
        "acklay": "gruñido amenazante",
        "reek": "bufido potente",
        "boga": "rugido reptiliano",
        "varactyl": "grito estridente",
    },
    "personaje": {
        "darth vader": "Yo soy tu padre",
        "yoda": "Hazlo o no lo hagas, pero no lo intentes",
        "han solo": "Que la Fuerza te acompañe",
        "obi-wan kenobi": "La Fuerza estará contigo, siempre",
        "leia organa": "Ayúdame, Obi-Wan Kenobi, eres mi única esperanza",
        "palpatine": "¡Tú no sabes el poder del Lado Oscuro!",
        "luke skywalker": "La Fuerza es poderosa en mi familia",
        "chewbacca": "Gruñido característico",
        "c-3po": "¡Oh, mis circuitos! ¡Estoy seguro de que es un error, señor!",
        "lando calrissian": "¡A por ello!",
        "anakin skywalker": "Tengo mal presentimiento sobre esto",
        "qui-gon jinn": "Tu enfoque determinará tu realidad",
        "padmé amidala": "Soy más fuerte de lo que crees",
        "jyn erso": "Rebellions are built on hope",
        "kylo ren": "Let the past die. Kill it, if you have to.",
        "finn": "Droid, please!",
    },
    "planeta": {
        "tatooine": "Desértico y desolado, conocido por sus dobles soles",
        "endor": "Boscoso y hogar de los Ewoks, ubicado en el Borde Exterior",
        "coruscant": "Ciudad planeta cubierto por vastos rascacielos y sede del Senado Galáctico",
        "naboo": "Planeta exuberante con paisajes hermosos y lagos",
        "kashyyyk": "Selvático y hogar de los Wookiees, ubicado en el Sector Mytaranor",
        "mustafar": "Volcánico y conocido por ser el sitio del duelo entre Obi-Wan y Anakin",
        "dagobah": "Pantanoso y cubierto de densa vegetación, escondite de Yoda",
        "geonosis": "Árido y rocoso, conocido por ser el sitio de la primera batalla de las Guerras Clon",
        "jakku": "Desértico y lleno de restos de naves espaciales, hogar de Rey",
        "ahch-to": "Océanos y islas rocosas, sitio de exilio de Luke Skywalker",
        "scarif": "Planeta tropical, sede de la base secreta del Imperio Galáctico",
        "hosnian prime": "Ciudad planeta y sede del gobierno de la Nueva República antes de ser destruido por Starkiller Base",
        "crait": "Mineral y salinas blancas, sitio de la batalla entre la Resistencia y la Primera Orden",
        "kamino": "Océanos y ciudades flotantes, hogar de los clonadores y el ejército clon",
        "exegol": "Planeta oculto de Sith en el Sector Unknown",
        "mon calamari": "Océanos profundos, hogar de los Mon Calamari y los Quarren",
        "bespin": "Gas gigante con ciudades flotantes y minas de Tibanna",
    }
}

def obtener_respuesta_valida(respuesta):
    """Función para normalizar la respuesta del usuario"""
    return unidecode.unidecode(respuesta.lower().replace("-", "").strip())

def mostrar_menu():
    """Función para mostrar el menú inicial"""
    print("Bienvenido al juego de Star Wars!")
    print("Elige una categoría para adivinar:")
    print("1. Sonido de una criatura")
    print("2. Frase épica de un personaje")
    print("3. Descripción de un planeta")
    print("4. Salir")

def jugar_star_wars_game():
    while True:
        mostrar_menu()
        
        opcion = input("Ingresa el número de la categoría o '4' para salir: ").strip().lower()
        
        if opcion == "4" or opcion == "salir":
            print("Gracias por jugar!")
            break
        
        if opcion not in ["1", "2", "3"]:
            print("Opción no válida. Por favor, elige una opción del 1 al 3 o '4' para salir.")
            continue
        
        opcion = int(opcion)
        
        categoria, preguntas = list(opciones.items())[opcion - 1]
        pregunta, respuesta = random.choice(list(preguntas.items()))
        
        print(f"Adivina {categoria}:")
        print(pregunta)
        
        intentos = 3
        while intentos > 0:
            respuesta_usuario = input("Tu respuesta: ").strip()
            
            if obtener_respuesta_valida(respuesta_usuario) == obtener_respuesta_valida(pregunta):
                print("¡Correcto!")
                break
            else:
                intentos -= 1
                if intentos > 0:
                    print(f"Incorrecto. Te quedan {intentos} intentos.")
        
        if intentos == 0:
            print(f"¡Lo siento! La respuesta correcta era: {respuesta}")
        
        print()  # Espacio para separar las preguntas

jugar_star_wars_game()
