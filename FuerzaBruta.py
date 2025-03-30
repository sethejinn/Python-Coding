import hashlib

def hashear_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()
def fuerza_bruta(hash_objetivo, diccionario):
    with open(diccionario, "r", encoding="utf-8") as f:
        for linea in f:
            palabra = linea.strip()
            if hashear_contraseña(palabra) == hash_objetivo:
                return palabra
    return None
if __name__ == "__main__":
    hash_victima = input("Introduce el hash SHA-256 de la contraseña: ")
    diccionario = input("Ruta del diccionario: ")
    resultado = fuerza_bruta(hash_victima, diccionario)
    if resultado:
        print(f"Contraseña encontrada: {resultado}")
    else:
        print("No se encontró la contraseña.")
