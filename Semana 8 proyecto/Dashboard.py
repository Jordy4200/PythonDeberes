import os
import subprocess

# He añadido mis comentarios explicando los cambios que realicé para adaptar este dashboard a mis necesidades.

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        # CAMBIO REALIZADO POR MÍ: Agregué el parámetro encoding='utf-8'
        # Hice esto porque al leer mis archivos con tildes o ñ en Windows, me salían caracteres raros o errores.
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None


def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")


def mostrar_menu():
    # ADAPTACIÓN PERSONALIZADA:
    # Modifiqué la lógica para definir la ruta base.
    # Usé 'os.path.dirname' dos veces para subir un nivel en el directorio.
    # Mi objetivo es que el dashboard pueda ver toda mi carpeta "PythonTarea" y no solo la carpeta donde está este archivo.
    ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    print(f"\n--- Dashboard: {ruta_base} ---")

    while True:
        # Lógica dinámica:
        # En lugar de escribir manualmente las unidades ('1': 'Unidad 1'), programé este ciclo.
        # Ahora el código lee automáticamente las carpetas que yo cree (Semana 5, Semana 6, etc.).
        opciones = {}
        contador = 1

        with os.scandir(ruta_base) as entradas:
            for entrada in entradas:
                # Filtro para ignorar archivos ocultos (los que empiezan con punto) y asegurar que sean carpetas.
                if entrada.is_dir() and not entrada.name.startswith('.'):
                    opciones[str(contador)] = entrada.name
                    contador += 1

        print("\nMenu Principal - Selecciona una carpeta de trabajo")
        for key, nombre in opciones.items():
            print(f"{key} - {nombre}")
        print("0 - Salir")

        eleccion = input("Elige una opción: ")

        if eleccion == '0':
            print("Saliendo del programa.")
            break
        elif eleccion in opciones:
            ruta_seleccionada = os.path.join(ruta_base, opciones[eleccion])
            mostrar_sub_menu(ruta_seleccionada)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


def mostrar_sub_menu(ruta_unidad):
    # Detecto si hay subcarpetas dentro de la unidad seleccionada.
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir() and not f.name.startswith('.')]

    # MEJORA DE NAVEGACIÓN:
    # Agregué esta condición: si la carpeta NO tiene subcarpetas (como mi carpeta "Semana 5"),
    # el programa salta directamente a mostrar los scripts. Así ahorro un paso innecesario en el menú.
    if not sub_carpetas:
        mostrar_scripts(ruta_unidad)
        return

    while True:
        print(f"\nSubmenú ({os.path.basename(ruta_unidad)}) - Selecciona una subcarpeta")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion = input("Elige una opción: ")

        if eleccion == '0':
            break
        else:
            try:
                indice = int(eleccion) - 1
                if 0 <= indice < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[indice]))
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Opción no válida.")


def mostrar_scripts(ruta_carpeta):
    # Filtro para mostrar únicamente archivos .py
    scripts = [f.name for f in os.scandir(ruta_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print(f"\nScripts en ({os.path.basename(ruta_carpeta)})")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar")

        eleccion = input("Elige un script o '0' para regresar: ")

        if eleccion == '0':
            break
        else:
            try:
                indice = int(eleccion) - 1
                if 0 <= indice < len(scripts):
                    ruta_script = os.path.join(ruta_carpeta, scripts[indice])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Opción no válida.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()