# Generador de Contraseñas Seguras

import random
import string

def gen_contrasena(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

print("¡Bienvenida al Generador de Contraseñas Seguras de MG!")

contrasena = gen_contrasena()
print("Aquí tienes tu contraseña, cuídala:", contrasena)
