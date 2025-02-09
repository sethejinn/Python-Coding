import random
import time

class Granja:
    def __init__(self):
        self.dinero = 1000
        self.cultivos = {}
        self.animales = {}
        self.clima = "Soleado"
        self.eventos = ["Tormenta", "Sequía", "Día de Mercado", "Visita Sorpresa", "Festival de la Cosecha", "Brote de Enfermedad", "Invasión de Plagas"]
        self.nivel = 1
        self.experiencia = 0
        self.inventario = {"leche": 0, "huevos": 0, "lana": 0, "frutas": 0}
        self.edificaciones = {"silo": False, "granero": False, "establo": False}
    
    def mostrar_estado(self):
        print(f"\nDinero: ${self.dinero}")
        print(f"Nivel: {self.nivel} | Experiencia: {self.experiencia}")
        print(f"Cultivos: {self.cultivos}")
        print(f"Animales: {self.animales}")
        print(f"Inventario: {self.inventario}")
        print(f"Edificaciones: {self.edificaciones}")
        print(f"Clima actual: {self.clima}")
    
    def cambiar_clima(self):
        self.clima = random.choice(["Soleado", "Lluvioso", "Nublado", "Tormentoso", "Nevado"])
        print(f"El clima ha cambiado a: {self.clima}")
    
    def plantar_cultivo(self, tipo, cantidad):
        costo = cantidad * 10
        if self.dinero >= costo:
            self.dinero -= costo
            self.cultivos[tipo] = self.cultivos.get(tipo, 0) + cantidad
            print(f"Has plantado {cantidad} {tipo}(s).")
            self.ganar_experiencia(5 * cantidad)
        else:
            print("No tienes suficiente dinero para plantar eso.")
    
    def cosechar(self):
        ganancia = sum(cantidad * 15 for cantidad in self.cultivos.values())
        self.dinero += ganancia
        self.inventario["frutas"] += sum(self.cultivos.values())
        self.cultivos.clear()
        print(f"Has cosechado y ganado ${ganancia}.")
        self.ganar_experiencia(20)
    
    def comprar_animal(self, tipo, cantidad):
        costo = cantidad * 50
        if self.dinero >= costo:
            self.dinero -= costo
            self.animales[tipo] = self.animales.get(tipo, 0) + cantidad
            print(f"Has comprado {cantidad} {tipo}(s).")
            self.ganar_experiencia(10 * cantidad)
        else:
            print("No tienes suficiente dinero.")
    
    def recolectar_productos(self):
        if "vaca" in self.animales:
            self.inventario["leche"] += self.animales["vaca"]
        if "gallina" in self.animales:
            self.inventario["huevos"] += self.animales["gallina"]
        if "oveja" in self.animales:
            self.inventario["lana"] += self.animales["oveja"]
        print("Has recolectado productos de tus animales.")
        self.ganar_experiencia(15)
    
    def vender_producto(self, producto, cantidad):
        if self.inventario.get(producto, 0) >= cantidad:
            precio = random.randint(10, 30)
            ganancia = cantidad * precio
            self.dinero += ganancia
            self.inventario[producto] -= cantidad
            print(f"Has vendido {cantidad} {producto}(s) por ${ganancia}.")
            self.ganar_experiencia(10)
        else:
            print("No tienes suficientes productos para vender.")
    
    def evento_aleatorio(self):
        evento = random.choice(self.eventos)
        if evento == "Tormenta":
            print("Una tormenta ha dañado tus cultivos. Pierdes la mitad de ellos.")
            for cultivo in self.cultivos:
                self.cultivos[cultivo] //= 2
        elif evento == "Sequía":
            print("La sequía ha afectado a tus animales. Algunos están enfermos.")
            for animal in self.animales:
                self.animales[animal] -= max(1, self.animales[animal] // 4)
        elif evento == "Día de Mercado":
            print("Hoy es día de mercado. Puedes vender productos a mejor precio.")
            self.dinero += 300
        elif evento == "Visita Sorpresa":
            print("Un visitante te ha regalado 200 monedas.")
            self.dinero += 200
        elif evento == "Festival de la Cosecha":
            print("Tu cosecha ha crecido más rápido y duplicas la producción.")
            for cultivo in self.cultivos:
                self.cultivos[cultivo] *= 2
        elif evento == "Brote de Enfermedad":
            print("Una enfermedad ha afectado a tus animales. Pierdes algunos de ellos.")
            for animal in self.animales:
                self.animales[animal] = max(0, self.animales[animal] - 1)
        elif evento == "Invasión de Plagas":
            print("Plagas han destruido algunos cultivos.")
            for cultivo in self.cultivos:
                self.cultivos[cultivo] = max(0, self.cultivos[cultivo] - 2)
        print(f"Evento del día: {evento}")
    
    def ganar_experiencia(self, cantidad):
        self.experiencia += cantidad
        if self.experiencia >= self.nivel * 100:
            self.nivel += 1
            self.experiencia = 0
            print(f"¡Has subido al nivel {self.nivel}!")
    
    def jugar_turno(self):
        self.mostrar_estado()
        self.cambiar_clima()
        self.evento_aleatorio()
        print("\nOpciones: 1) Plantar 2) Cosechar 3) Comprar animal 4) Vender producto 5) Recolectar productos 6) Pasar turno")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            tipo = input("¿Qué deseas plantar? ")
            cantidad = int(input("¿Cuántos? "))
            self.plantar_cultivo(tipo, cantidad)
        elif opcion == "2":
            self.cosechar()
        elif opcion == "3":
            tipo = input("¿Qué animal deseas comprar? ")
            cantidad = int(input("¿Cuántos? "))
            self.comprar_animal(tipo, cantidad)
        elif opcion == "4":
            producto = input("¿Qué producto deseas vender? ")
            cantidad = int(input("¿Cuántos? "))
            self.vender_producto(producto, cantidad)
        elif opcion == "5":
            self.recolectar_productos()
        print("Fin del turno...")
        time.sleep(2)

if __name__ == "__main__":
    granja = Granja()
    while True:
        granja.jugar_turno()
