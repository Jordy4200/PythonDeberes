# --- 1. CLASE PRODUCTO ---
# Esta clase es el "molde" para crear cada producto individual.
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters: Nos permiten "leer" o sacar la información del producto
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters: Nos permiten "modificar" la información del producto
    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio


# --- 2. CLASE INVENTARIO ---
# Esta clase maneja la lista donde guardaremos todos los productos.
class Inventario:
    def __init__(self):
        self.productos = []  # Creamos una lista vacía para guardar los productos

    def añadir_producto(self, producto):
        # Primero comprobamos si el ID ya existe en nuestra lista
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return  # Salimos de la función sin añadir nada

        # Si el ID es nuevo, añadimos el producto al final de la lista
        self.productos.append(producto)
        print("¡Producto añadido con éxito!")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)  # Borramos el producto de la lista
                print("¡Producto eliminado con éxito!")
                return
        print("Error: No se encontró ningún producto con ese ID.")

    def actualizar_producto(self, id_producto, nueva_cantidad, nuevo_precio):
        for p in self.productos:
            if p.get_id() == id_producto:
                # Si el usuario escribió una nueva cantidad, la actualizamos
                if nueva_cantidad != "":
                    p.set_cantidad(int(nueva_cantidad))
                # Si el usuario escribió un nuevo precio, lo actualizamos
                if nuevo_precio != "":
                    p.set_precio(float(nuevo_precio))

                print("¡Producto actualizado con éxito!")
                return
        print("Error: No se encontró ningún producto con ese ID.")

    def buscar_producto(self, nombre):
        encontrados = False
        for p in self.productos:
            # Comparamos los nombres en minúsculas para que sea más fácil buscar
            if nombre.lower() in p.get_nombre().lower():
                print(
                    f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio()}")
                encontrados = True

        if not encontrados:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if len(self.productos) == 0:
            print("El inventario está vacío.")
        else:
            print("\n--- Inventario Actual ---")
            for p in self.productos:
                print(
                    f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio()}")


# --- 3. MENÚ INTERACTIVO ---
# Esta función es la que interactúa con el usuario en la consola de PyCharm.
def menu_principal():
    mi_inventario = Inventario()  # Creamos nuestro inventario vacío

    while True:
        print("\n--- MENÚ DE GESTIÓN DE INVENTARIO ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Elige una opción (1-6): ")

        if opcion == '1':
            id_prod = input("Ingresa el ID del producto: ")
            nombre = input("Ingresa el nombre: ")
            cantidad = int(input("Ingresa la cantidad: "))
            precio = float(input("Ingresa el precio: "))

            nuevo_producto = Producto(id_prod, nombre, cantidad, precio)
            mi_inventario.añadir_producto(nuevo_producto)

        elif opcion == '2':
            id_prod = input("Ingresa el ID del producto a eliminar: ")
            mi_inventario.eliminar_producto(id_prod)

        elif opcion == '3':
            id_prod = input("Ingresa el ID del producto a actualizar: ")
            # Pedimos los datos como texto. Si el usuario presiona Enter sin escribir nada, queda como ""
            nueva_cantidad = input("Ingresa la nueva cantidad (presiona Enter para no cambiarla): ")
            nuevo_precio = input("Ingresa el nuevo precio (presiona Enter para no cambiarlo): ")

            mi_inventario.actualizar_producto(id_prod, nueva_cantidad, nuevo_precio)

        elif opcion == '4':
            nombre = input("Ingresa el nombre del producto a buscar: ")
            mi_inventario.buscar_producto(nombre)

        elif opcion == '5':
            mi_inventario.mostrar_inventario()

        elif opcion == '6':
            print("¡Saliendo del sistema! Hasta luego.")
            break  # Esto termina el ciclo "while" y cierra el programa

        else:
            print("Opción no válida. Por favor, elige un número del 1 al 6.")


# --- 4. PUNTO DE ARRANQUE ---
# Esto le dice a Python que si ejecutamos este archivo directamente, inicie el menú.
if __name__ == "__main__":
    menu_principal()