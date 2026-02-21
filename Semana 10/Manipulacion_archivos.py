import os


# --- CLASE PRODUCTO ---
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = str(id_producto)
        self.nombre = nombre
        self.cantidad = int(cantidad)
        self.precio = float(precio)

    # Este metodo define cómo se muestra el producto en texto
    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"


# --- CLASE INVENTARIO ---
class Inventario:
    def __init__(self):
        # Usamos un diccionario para guardar los productos, la clave será el ID
        self.productos = {}
        self.archivo = "inventario.txt"
        # Al iniciar, cargamos automáticamente los datos del archivo
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Lee el archivo .txt y carga los productos al diccionario."""
        try:
            # Abrimos en modo lectura ('r') usando with
            with open(self.archivo, 'r') as f:
                for linea in f:  # Leemos línea por línea [cite: 55]
                    # Limpiamos saltos de línea y separamos por comas
                    datos = linea.strip().split(',')
                    if len(datos) == 4:
                        id_prod, nombre, cant, precio = datos
                        # Creamos el objeto producto y lo añadimos al diccionario
                        producto = Producto(id_prod, nombre, cant, precio)
                        self.productos[id_prod] = producto
            print("✅ Inventario cargado exitosamente desde el archivo.")

        except FileNotFoundError:  # Se ejecuta si el archivo no existe [cite: 102]
            print(" Archivo de inventario no encontrado. Se creará uno nuevo automáticamente.")
            # Si no existe, lo creamos abriéndolo en modo escritura y cerrándolo
            with open(self.archivo, 'w') as f:
                pass
        except PermissionError:
            print(" Error: No tienes permisos para leer el archivo 'inventario.txt'.")
        except Exception as e:  # Captura cualquier otra excepción no prevista [cite: 117, 118]
            print(f" Error inesperado al cargar el archivo: {e}")

    def guardar_en_archivo(self):
        """Guarda todos los productos del diccionario en el archivo .txt."""
        try:
            # Abrimos en modo escritura ('w') para sobrescribir con los datos actualizados [cite: 43, 64]
            with open(self.archivo, 'w') as f:
                for p in self.productos.values():
                    # Escribimos cada producto separado por comas
                    f.write(f"{p.id_producto},{p.nombre},{p.cantidad},{p.precio}\n")
            print("✅ Cambios guardados en el archivo exitosamente.")

        except PermissionError:
            print(" Error: No tienes permisos para escribir en el archivo 'inventario.txt'.")
        except Exception as e:
            print(f" Error inesperado al guardar el archivo: {e}")

    def añadir_producto(self, producto):
        if producto.id_producto in self.productos:
            print("⚠️ Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.id_producto] = producto
            print(" Producto añadido al inventario.")
            self.guardar_en_archivo()  # Guardamos en el archivo tras la modificación

    def actualizar_producto(self, id_producto, nueva_cantidad, nuevo_precio):
        if id_producto in self.productos:
            self.productos[id_producto].cantidad = nueva_cantidad
            self.productos[id_producto].precio = nuevo_precio
            print(" Producto actualizado.")
            self.guardar_en_archivo()  # Guardamos en el archivo tras la modificación
        else:
            print("⚠️ Error: Producto no encontrado.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(" Producto eliminado.")
            self.guardar_en_archivo()  # Guardamos en el archivo tras la modificación
        else:
            print("⚠Error: Producto no encontrado.")

    def mostrar_inventario(self):
        if not self.productos:
            print(" El inventario está vacío.")
        else:
            print("\n--- Lista de Productos ---")
            for p in self.productos.values():
                print(p)
            print("--------------------------")


# --- INTERFAZ DE USUARIO (CONSOLA) ---
def menu():
    inventario = Inventario()

    while True:
        print("\n=== SISTEMA DE GESTIÓN DE INVENTARIOS ===")
        print("1. Añadir nuevo producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_p = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre: ")
            try:
                cant = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio: "))
                nuevo_producto = Producto(id_p, nombre, cant, precio)
                inventario.añadir_producto(nuevo_producto)
            except ValueError:  # Manejamos el error si el usuario no introduce números [cite: 99]
                print(" Error: La cantidad y el precio deben ser números.")

        elif opcion == '2':
            id_p = input("Ingrese el ID del producto a actualizar: ")
            try:
                cant = int(input("Ingrese la nueva cantidad: "))
                precio = float(input("Ingrese el nuevo precio: "))
                inventario.actualizar_producto(id_p, cant, precio)
            except ValueError:
                print(" Error: La cantidad y el precio deben ser números.")

        elif opcion == '3':
            id_p = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_p)

        elif opcion == '4':
            inventario.mostrar_inventario()

        elif opcion == '5':
            print("Saliendo del sistema... ¡Hasta luego!")
            break

        else:
            print("⚠️ Opción no válida. Por favor, intente de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu()