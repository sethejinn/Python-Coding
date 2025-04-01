CREATE DATABASE IF NOT EXISTS sistema_inventario;

USE sistema_inventario;

CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    cantidad INT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    categoria VARCHAR(50) NOT NULL
);
CREATE DATABASE IF NOT EXISTS sistema_inventario;

USE sistema_inventario;

CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    cantidad INT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    categoria VARCHAR(50) NOT NULL
);

import mysql.connector
from mysql.connector import Error

class Producto:
    def __init__(self, nombre, cantidad, precio, categoria):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.categoria = categoria

    def __str__(self):
        return f"Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}, Categoría: {self.categoria}"

class GestionInventario:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                database='sistema_inventario',
                user='root',
                password=''  # Coloca tu contraseña si es necesario
            )
            
            if self.conexion.is_connected():
                print("Conexión exitosa a la base de datos")
                
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
    
    def __del__(self):
        if hasattr(self, 'conexion') and self.conexion.is_connected():
            self.conexion.close()
            print("Conexión a MySQL cerrada")
    
    def agregar_producto(self, producto):
        try:
            cursor = self.conexion.cursor()
            
            # Verificar si el producto ya existe
            cursor.execute("SELECT nombre FROM productos WHERE nombre = %s", (producto.nombre,))
            if cursor.fetchone():
                print(f"Error: Ya existe un producto con el nombre '{producto.nombre}'")
                return False
            
            # Insertar el nuevo producto
            query = "INSERT INTO productos (nombre, cantidad, precio, categoria) VALUES (%s, %s, %s, %s)"
            valores = (producto.nombre, producto.cantidad, producto.precio, producto.categoria)
            cursor.execute(query, valores)
            self.conexion.commit()
            print("Producto agregado exitosamente!")
            return True
            
        except Error as e:
            print(f"Error al agregar producto: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
    
    def mostrar_productos(self):
        try:
            cursor = self.conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM productos")
            productos = cursor.fetchall()
            
            if not productos:
                print("No hay productos en el inventario.")
                return
            
            print("\n--- LISTA DE PRODUCTOS ---")
            for producto in productos:
                print(f"ID: {producto['id']}")
                print(f"Nombre: {producto['nombre']}")
                print(f"Cantidad: {producto['cantidad']}")
                print(f"Precio: ${producto['precio']:.2f}")
                print(f"Categoría: {producto['categoria']}")
                print("-----------------------------")
                
        except Error as e:
            print(f"Error al mostrar productos: {e}")
        finally:
            if cursor:
                cursor.close()
    
    def buscar_producto(self, nombre):
        try:
            cursor = self.conexion.cursor(dictionary=True)
            query = "SELECT * FROM productos WHERE nombre = %s"
            cursor.execute(query, (nombre,))
            producto = cursor.fetchone()
            
            if producto:
                print("\n--- PRODUCTO ENCONTRADO ---")
                print(f"ID: {producto['id']}")
                print(f"Nombre: {producto['nombre']}")
                print(f"Cantidad: {producto['cantidad']}")
                print(f"Precio: ${producto['precio']:.2f}")
                print(f"Categoría: {producto['categoria']}")
                return True
            else:
                print(f"No se encontró un producto con el nombre '{nombre}'")
                return False
                
        except Error as e:
            print(f"Error al buscar producto: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
    
    def actualizar_producto(self, nombre, nueva_cantidad=None, nuevo_precio=None, nueva_categoria=None):
        try:
            cursor = self.conexion.cursor()
            
            # Verificar si el producto existe
            cursor.execute("SELECT id FROM productos WHERE nombre = %s", (nombre,))
            producto_id = cursor.fetchone()
            
            if not producto_id:
                print(f"No se encontró un producto con el nombre '{nombre}'")
                return False
            
            # Construir la consulta de actualización
            updates = []
            valores = []
            
            if nueva_cantidad is not None:
                updates.append("cantidad = %s")
                valores.append(nueva_cantidad)
            
            if nuevo_precio is not None:
                updates.append("precio = %s")
                valores.append(nuevo_precio)
            
            if nueva_categoria is not None:
                updates.append("categoria = %s")
                valores.append(nueva_categoria)
            
            if not updates:
                print("No se proporcionaron datos para actualizar")
                return False
            
            query = f"UPDATE productos SET {', '.join(updates)} WHERE nombre = %s"
            valores.append(nombre)
            
            cursor.execute(query, valores)
            self.conexion.commit()
            
            if cursor.rowcount > 0:
                print("Producto actualizado exitosamente!")
                return True
            else:
                print("No se realizaron cambios en el producto")
                return False
                
        except Error as e:
            print(f"Error al actualizar producto: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
    
    def eliminar_producto(self, nombre):
        try:
            cursor = self.conexion.cursor()
            
            # Verificar si el producto existe
            cursor.execute("SELECT id FROM productos WHERE nombre = %s", (nombre,))
            producto_id = cursor.fetchone()
            
            if not producto_id:
                print(f"No se encontró un producto con el nombre '{nombre}'")
                return False
            
            # Eliminar el producto
            cursor.execute("DELETE FROM productos WHERE nombre = %s", (nombre,))
            self.conexion.commit()
            
            if cursor.rowcount > 0:
                print("Producto eliminado exitosamente!")
                return True
            else:
                print("No se pudo eliminar el producto")
                return False
                
        except Error as e:
            print(f"Error al eliminar producto: {e}")
            return False
        finally:
            if cursor:
                cursor.close()

def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN DE INVENTARIO ---")
    print("1. Agregar un producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar un producto")
    print("4. Actualizar un producto")
    print("5. Eliminar un producto")
    print("6. Salir")
    return input("Seleccione una opción (1-6): ")

def main():
    gestion = GestionInventario()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            print("\n--- AGREGAR PRODUCTO ---")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            categoria = input("Categoría: ")
            
            producto = Producto(nombre, cantidad, precio, categoria)
            gestion.agregar_producto(producto)
        
        elif opcion == '2':
            print("\n--- MOSTRAR PRODUCTOS ---")
            gestion.mostrar_productos()
        
        elif opcion == '3':
            print("\n--- BUSCAR PRODUCTO ---")
            nombre = input("Nombre del producto a buscar: ")
            gestion.buscar_producto(nombre)
        
        elif opcion == '4':
            print("\n--- ACTUALIZAR PRODUCTO ---")
            nombre = input("Nombre del producto a actualizar: ")
            
            print("Deje en blanco los campos que no desea actualizar")
            cantidad = input("Nueva cantidad: ")
            precio = input("Nuevo precio: ")
            categoria = input("Nueva categoría: ")
            
            # Convertir valores vacíos a None
            nueva_cantidad = int(cantidad) if cantidad else None
            nuevo_precio = float(precio) if precio else None
            nueva_categoria = categoria if categoria else None
            
            gestion.actualizar_producto(nombre, nueva_cantidad, nuevo_precio, nueva_categoria)
        
        elif opcion == '5':
            print("\n--- ELIMINAR PRODUCTO ---")
            nombre = input("Nombre del producto a eliminar: ")
            gestion.eliminar_producto(nombre)
        
        elif opcion == '6':
            print("Saliendo del sistema...")
            break
        
        else:
            print("Por favor, seleccione del 1 al 6.")

if __name__ == "__main__":
    main()
