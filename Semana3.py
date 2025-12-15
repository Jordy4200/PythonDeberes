# ==========================================
# Programación Tradicional: Promedio de Clima
# ==========================================

# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    print("--- Ingreso de Temperaturas Semanales ---")
    # Pedimos la temperatura de los 7 días de la semana
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio_semanal(lista_temperaturas):
    suma = sum(lista_temperaturas)
    promedio = suma / len(lista_temperaturas)
    return promedio

# Bloque principal del programa
# Aquí organizamos la lógica llamando a las funciones paso a paso
print("Inicio del programa tradicional")
datos_semana = ingresar_temperaturas() # Paso 1: Obtener datos
promedio = calcular_promedio_semanal(datos_semana) # Paso 2: Calcular

print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")