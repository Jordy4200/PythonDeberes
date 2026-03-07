# ==========================================
# CLASES DEL SISTEMA
# ==========================================

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Usamos una TUPLA para atributos inmutables (no cambian)
        self.info_basica = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.info_basica[0]}' por {self.info_basica[1]} (Cat: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Usamos una LISTA para los libros prestados (cambia dinámicamente)
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        # DICCIONARIO para buscar libros rápido por ISBN
        self.libros_disponibles = {}
        # CONJUNTO para asegurar que los IDs de usuario sean únicos
        self.ids_usuarios = set()
        # DICCIONARIO para guardar a los usuarios por su ID
        self.usuarios_registrados = {}

    def añadir_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro
        print(f"\n✅ Libro '{libro.info_basica[0]}' añadido a la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print("\n🗑️ Libro eliminado exitosamente.")
        else:
            print("\n❌ Error: No se encontró un libro con ese ISBN.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.ids_usuarios.add(usuario.id_usuario)
            self.usuarios_registrados[usuario.id_usuario] = usuario
            print(f"\n✅ Usuario '{usuario.nombre}' registrado con éxito.")
        else:
            print("\n❌ Error: Ese ID de usuario ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.ids_usuarios:
            self.ids_usuarios.remove(id_usuario)
            del self.usuarios_registrados[id_usuario]
            print("\n🗑️ Usuario dado de baja exitosamente.")
        else:
            print("\n❌ Error: Usuario no encontrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados and isbn in self.libros_disponibles:
            usuario = self.usuarios_registrados[id_usuario]
            libro = self.libros_disponibles[isbn]

            usuario.libros_prestados.append(libro)
            del self.libros_disponibles[isbn]
            print(f"\n📚 Libro prestado a {usuario.nombre} exitosamente.")
        else:
            print("\n❌ Error: El usuario no existe o el libro no está disponible.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]

            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"\n🔄 Libro devuelto por {usuario.nombre} exitosamente.")
                    return
            print("\n❌ Error: El usuario no tiene prestado un libro con ese ISBN.")
        else:
            print("\n❌ Error: Usuario no encontrado.")

    def buscar_libros(self, termino):
        print(f"\n🔍 Resultados para '{termino}':")
        encontrados = False
        termino = termino.lower()

        for libro in self.libros_disponibles.values():
            if (termino in libro.info_basica[0].lower() or
                    termino in libro.info_basica[1].lower() or
                    termino in libro.categoria.lower()):
                print(f"  - {libro}")
                encontrados = True

        if not encontrados:
            print("  - No se encontraron libros.")

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            print(f"\n📖 Libros prestados a {usuario.nombre}:")
            if usuario.libros_prestados:
                for libro in usuario.libros_prestados:
                    print(f"  - {libro}")
            else:
                print("  - No tiene libros prestados.")
        else:
            print("\n❌ Error: Usuario no encontrado.")


# ==========================================
# MENÚ INTERACTIVO (Ingreso Manual)
# ==========================================

def iniciar_sistema():
    mi_biblio = Biblioteca()

    while True:
        print("\n" + "=" * 40)
        print("   SISTEMA DE BIBLIOTECA DIGITAL")
        print("=" * 40)
        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Listar libros prestados de un usuario")
        print("9. Salir del sistema")
        print("=" * 40)

        opcion = input("Elige una opción (1-9): ")

        if opcion == "1":
            titulo = input("Ingresa el título del libro: ")
            autor = input("Ingresa el autor: ")
            categoria = input("Ingresa la categoría: ")
            isbn = input("Ingresa el ISBN: ")
            nuevo_libro = Libro(titulo, autor, categoria, isbn)
            mi_biblio.añadir_libro(nuevo_libro)

        elif opcion == "2":
            isbn = input("Ingresa el ISBN del libro a quitar: ")
            mi_biblio.quitar_libro(isbn)

        elif opcion == "3":
            nombre = input("Ingresa el nombre del usuario: ")
            id_usu = input("Ingresa un ID único para el usuario: ")
            nuevo_usuario = Usuario(nombre, id_usu)
            mi_biblio.registrar_usuario(nuevo_usuario)

        elif opcion == "4":
            id_usu = input("Ingresa el ID del usuario a dar de baja: ")
            mi_biblio.dar_baja_usuario(id_usu)

        elif opcion == "5":
            id_usu = input("Ingresa el ID del usuario: ")
            isbn = input("Ingresa el ISBN del libro a prestar: ")
            mi_biblio.prestar_libro(id_usu, isbn)

        elif opcion == "6":
            id_usu = input("Ingresa el ID del usuario: ")
            isbn = input("Ingresa el ISBN del libro a devolver: ")
            mi_biblio.devolver_libro(id_usu, isbn)

        elif opcion == "7":
            termino = input("Ingresa el título, autor o categoría a buscar: ")
            mi_biblio.buscar_libros(termino)

        elif opcion == "8":
            id_usu = input("Ingresa el ID del usuario: ")
            mi_biblio.listar_libros_prestados(id_usu)

        elif opcion == "9":
            print("\nSaliendo del sistema... ¡Hasta luego!")
            break

        else:
            print("\n❌ Opción no válida. Por favor, ingresa un número del 1 al 9.")


# Arrancar el programa
if __name__ == "__main__":
    iniciar_sistema()