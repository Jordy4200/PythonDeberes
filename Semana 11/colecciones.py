import json  # Importamos json para poder guardar y leer datos de un archivo de texto fácilmente
import os


# 1. CLASE PRODUCTO
class Producto:
    # El metodo __init__ es el constructor que inicializa los atributos del producto
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos para "obtener" (Getters) los valores
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos para "establecer" o actualizar (Setters) los valores
    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # Metodo extra para convertir el objeto a un diccionario simple.
    # Esto nos facilitará muchísimo guardar la información en un archivo.
    def to_dict(self):
        return {
            "id": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }


# 2. CLASE INVENTARIO
class Inventario:
    def __init__(self):
        # Usamos un DICCIONARIO para almacenar los productos.
        # La clave (key) será el ID del producto, y el valor será el objeto Producto.
        self.productos = {}
        self.archivo_datos = "inventario_datos.json"  # Nombre del archivo donde guardaremostodo

    def añadir_producto(self, producto):
        # Verificamos que el ID no exista ya en las claves del diccionario
        if producto.get_id() in self.productos:
            print("Error: Ya existe un producto con ese ID.")
        else:
            # Añadimos el producto al diccionario
            self.productos[producto.get_id()] = producto
            print("Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            # 'del' elimina el par clave-valor del diccionario
            del self.productos[id_producto]
            print("Producto eliminado con éxito.")
        else:
            print("Error: No se encontró un producto con ese ID.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]  # Obtenemos el objeto

            # Actualizamos solo si el usuario ingresó un valor nuevo
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)

            print("Producto actualizado con éxito.")
        else:
            print("Error: No se encontró el producto.")

    def buscar_producto_por_nombre(self, nombre_buscar):
        # Usamos una LISTA para guardar las coincidencias, por si hay varios productos con nombres parecidos
        resultados = []
        # Iteramos sobre los valores del diccionario (que son los objetos Producto)
        for producto in self.productos.values():
            if nombre_buscar.lower() in producto.get_nombre().lower():
                resultados.append(producto)

        if len(resultados) > 0:
            print(f"\n--- Resultados de búsqueda para '{nombre_buscar}' ---")
            for p in resultados:
                print(
                    f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio()}")
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if len(self.productos) == 0:
            print("El inventario está vacío.")
        else:
            print("\n--- Inventario Completo ---")
            for p in self.productos.values():
                print(
                    f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio()}")

    # --- Métodos de Archivos ---
    def guardar_en_archivo(self):
        # Convertimos nuestro diccionario de objetos a un formato simple que json pueda entender
        diccionario_para_guardar = {}
        for id_prod, producto in self.productos.items():
            diccionario_para_guardar[id_prod] = producto.to_dict()

        # Abrimos el archivo en modo escritura ('w' de write)
        with open(self.archivo_datos, 'w') as archivo:
            json.dump(diccionario_para_guardar, archivo, indent=4)
        print("Datos guardados en el archivo correctamente.")

    def cargar_desde_archivo(self):
        # Primero comprobamos si el archivo existe para no causar un error
        if os.path.exists(self.archivo_datos):
            # Abrimos el archivo en modo lectura ('r' de read)
            with open(self.archivo_datos, 'r') as archivo:
                datos_cargados = json.load(archivo)

                # Vaciamos el inventario actual
                self.productos = {}

                # Reconstruimos los objetos Producto a partir del archivo
                for id_prod, datos in datos_cargados.items():
                    nuevo_producto = Producto(datos["id"], datos["nombre"], datos["cantidad"], datos["precio"])
                    self.productos[id_prod] = nuevo_producto
            print("Datos cargados desde el archivo correctamente.")


# 3. INTERFAZ DE USUARIO (MENÚ)
def menu_principal():
    mi_inventario = Inventario()
    # Cargamos los datos guardados previamente al iniciar el programa
    mi_inventario.cargar_desde_archivo()

    while True:
        print("\n" + "=" * 30)
        print(" SISTEMA DE INVENTARIO AVANZADO ")
        print("=" * 30)
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar y Salir")

        opcion = input("Elige una opción (1-6): ")

        if opcion == '1':
            id_prod = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre: ")
            try:
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio: "))
                nuevo_prod = Producto(id_prod, nombre, cantidad, precio)
                mi_inventario.añadir_producto(nuevo_prod)
            except ValueError:
                print("Error: La cantidad debe ser un número entero y el precio un número decimal.")

        elif opcion == '2':
            id_prod = input("Ingrese el ID del producto a eliminar: ")
            mi_inventario.eliminar_producto(id_prod)

        elif opcion == '3':
            id_prod = input("Ingrese el ID del producto a actualizar: ")
            print("Deja el espacio en blanco si no deseas actualizar ese campo.")

            str_cantidad = input("Nueva cantidad: ")
            str_precio = input("Nuevo precio: ")

            # Comprobamos si el usuario escribió algo o lo dejó en blanco
            nueva_cantidad = int(str_cantidad) if str_cantidad != "" else None
            nuevo_precio = float(str_precio) if str_precio != "" else None

            mi_inventario.actualizar_producto(id_prod, nueva_cantidad, nuevo_precio)

        elif opcion == '4':
            nombre = input("Ingrese el nombre a buscar: ")
            mi_inventario.buscar_producto_por_nombre(nombre)

        elif opcion == '5':
            mi_inventario.mostrar_todos()

        elif opcion == '6':
            # Guardamos antes de cerrar el programa
            mi_inventario.guardar_en_archivo()
            print("Saliendo del sistema... ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Este bloque asegura que el menú solo se ejecute si corremos este archivo directamente
if __name__ == "__main__":
    menu_principal()