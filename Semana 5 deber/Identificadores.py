"""
==========================================
PROGRAMA: CALCULADORA DE ÁREA Y REGISTRO
DESCRIPCIÓN:
Este programa hace esto:
1. Calcula el área de un círculo usando su radio
2. Muestra información básica de un estudiante
==========================================
"""

# PARTE 1: CALCULAR ÁREA DE UN CÍRCULO

# Definimos una función para calcular el área
def calcular_area_circulo(radio):
    """
    Esta función calcula el área de un círculo.
    Fórmula: área = π * radio²
    """
    # Definimos PI como constante (tipo float)
    PI = 3.14159

    # Calculamos el área (radio al cuadrado multiplicado por PI)
    area = PI * (radio ** 2)  # radio ** 2 significa radio al cuadrado

    # Retornamos el resultado
    return area


# PARTE 2: INFORMACIÓN DEL ESTUDIANTE


def mostrar_info_estudiante():
    """
    Esta función muestra información de un estudiante.
    Usamos diferentes tipos de datos:
    - string para texto
    - integer para números enteros
    - float para números con decimales
    - boolean para verdadero/falso
    """
    # Tipos de datos diferentes:

    # STRING: para texto (entre comillas)
    nombre_estudiante = "Juan Pérez"
    nombre_curso = "Programación Orientada a Objetos"

    # INTEGER: número entero (sin decimales)
    edad_estudiante = 20
    codigo_estudiante = 2023001

    # FLOAT: número con decimales
    promedio_calificaciones = 8.75
    altura_estudiante = 1.75  # en metros

    # BOOLEAN: verdadero o falso
    esta_inscrito = True
    ha_aprobado = False

    # Mostramos toda la información
    print("\n=== INFORMACIÓN DEL ESTUDIANTE ===")
    print(f"Nombre: {nombre_estudiante}")
    print(f"Edad: {edad_estudiante} años")
    print(f"Código: {codigo_estudiante}")
    print(f"Curso: {nombre_curso}")
    print(f"Promedio: {promedio_calificaciones}")
    print(f"Altura: {altura_estudiante} metros")
    print(f"¿Está inscrito?: {esta_inscrito}")
    print(f"¿Ha aprobado?: {ha_aprobado}")


# PARTE 3: EJECUCIÓN PRINCIPAL

def main():
    # Esta funcion ejecuta toda el  deber

    print("¡BIENVENIDO AL PROGRAMA!")
    print("=" * 40)

    # Ejemplo 1: Calcular área de un círculo
    print("\n--- CÁLCULO DEL ÁREA DE UN CÍRCULO ---")

    # Definimos el radio (tipo float)
    radio_circulo = 5.0  # en centímetros

    # Llamamos a la función para calcular el área
    area_resultado = calcular_area_circulo(radio_circulo)

    # Mostramos el resultado
    print(f"Radio del círculo: {radio_circulo} cm")
    print(f"Área calculada: {area_resultado:.2f} cm²")  # :.2f muestra 2 decimales

    # Ejemplo 2: Calcular con otro radio
    otro_radio = 7.5
    otra_area = calcular_area_circulo(otro_radio)
    print(f"\nPara un radio de {otro_radio} cm, el área es: {otra_area:.2f} cm²")

    # Ejemplo 3: Mostrar información del estudiante
    mostrar_info_estudiante()

    # PARTE 4: USO DE DIFERENTES IDENTIFICADORES

    # Más ejemplos de identificadores descriptivos

    # Para números
    cantidad_estudiantes = 25
    precio_producto = 49.99
    temperatura_ambiente = 22.5

    # Para texto
    nombre_profesor = "María González"
    nombre_universidad = "Universidad Amazónica"

    # Para booleanos
    es_dia_laboral = True
    tiene_conexion_internet = True

    # Mostramos algunos de estos valores
    print("\n=== DATOS ADICIONALES ===")
    print(f"Cantidad de estudiantes: {cantidad_estudiantes}")
    print(f"Precio del producto: ${precio_producto}")
    print(f"Nombre del profesor: {nombre_profesor}")
    print(f"¿Es día laboral?: {es_dia_laboral}")

    print("\n" + "=" * 40)
    print("¡PROGRAMA FINALIZADO EXITOSAMENTE!")
    print("=" * 40)

# INICIAR EL PROGRAMA

# Esta línea hace que el programa comience ejecutando la función main
if __name__ == "__main__":
    main()