import re
import os

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"

class GestionContactos:
    def __init__(self, archivo_contactos='contactos.txt'):
        self.archivo_contactos = archivo_contactos
        self.contactos = []
        self.cargar_contactos()
    
    def validar_email(self, email):
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, email) is not None
    
    def agregar_contacto(self, contacto):
        try:
            if not contacto.nombre or not contacto.telefono or not contacto.email:
                raise ValueError("Todos los campos son obligatorios")
            
            if not self.validar_email(contacto.email):
                raise ValueError("Formato de email inválido")
            
            self.contactos.append(contacto)
            self.guardar_contactos()
            print("Contacto agregado exitosamente.")
        except ValueError as e:
            print(f"Error al agregar contacto: {e}")
    
    def mostrar_contactos(self):
        if not self.contactos:
            print("No hay contactos en la lista.")
            return
        
        print("\n--- LISTA DE CONTACTOS ---")
        for i, contacto in enumerate(self.contactos, 1):
            print(f"{i}. {contacto}")
        print("--------------------------\n")
    
    def buscar_contacto(self, nombre):
        contactos_encontrados = [
            contacto for contacto in self.contactos 
            if nombre.lower() in contacto.nombre.lower()
        ]
        
        if not contactos_encontrados:
            print(f"No se encontraron contactos con el nombre '{nombre}'.")
            return
        
        print("\n--- CONTACTOS ENCONTRADOS ---")
        for i, contacto in enumerate(contactos_encontrados, 1):
            print(f"{i}. {contacto}")
        print("-----------------------------\n")
    
    def eliminar_contacto(self, nombre):
        contactos_a_eliminar = [
            contacto for contacto in self.contactos 
            if nombre.lower() == contacto.nombre.lower()
        ]
        
        if not contactos_a_eliminar:
            print(f"No se encontró un contacto con el nombre '{nombre}'.")
            return
        
        if len(contactos_a_eliminar) > 1:
            print("Múltiples contactos encontrados con ese nombre:")
            self.buscar_contacto(nombre)
            try:
                indice = int(input("Ingrese el número del contacto que desea eliminar: ")) - 1
                if 0 <= indice < len(contactos_a_eliminar):
                    contacto = contactos_a_eliminar[indice]
                else:
                    print("Número de contacto inválido.")
                    return
            except ValueError:
                print("Entrada inválida. Debe ingresar un número.")
                return
        else:
            contacto = contactos_a_eliminar[0]
        
        self.contactos.remove(contacto)
        self.guardar_contactos()
        print(f"Contacto '{contacto.nombre}' eliminado exitosamente.")
    
    def guardar_contactos(self):
        try:
            with open(self.archivo_contactos, 'w') as archivo:
                for contacto in self.contactos:
                    archivo.write(f"{contacto.nombre},{contacto.telefono},{contacto.email}\n")
        except IOError as e:
            print(f"Error al guardar contactos: {e}")
    
    def cargar_contactos(self):
        try:
            if not os.path.exists(self.archivo_contactos):
                return
            
            with open(self.archivo_contactos, 'r') as archivo:
                lineas = archivo.readlines()
                for linea in lineas:
                    datos = linea.strip().split(',')
                    if len(datos) == 3:
                        nombre, telefono, email = datos
                        self.contactos.append(Contacto(nombre, telefono, email))
        except IOError as e:
            print(f"Error al cargar contactos: {e}")

def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN DE CONTACTOS ---")
    print("1. Agregar contacto")
    print("2. Mostrar todos los contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    print("----------------------------------------")

def main():
    sistema = GestionContactos()
    
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
        
        if opcion == 1:
            print("\n--- AGREGAR CONTACTO ---")
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            
            nuevo_contacto = Contacto(nombre, telefono, email)
            sistema.agregar_contacto(nuevo_contacto)
        
        elif opcion == 2:
            sistema.mostrar_contactos()
        
        elif opcion == 3:
            print("\n--- BUSCAR CONTACTO ---")
            nombre = input("Ingrese el nombre a buscar: ")
            sistema.buscar_contacto(nombre)
        
        elif opcion == 4:
            print("\n--- ELIMINAR CONTACTO ---")
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            sistema.eliminar_contacto(nombre)
        
        elif opcion == 5:
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    main()
