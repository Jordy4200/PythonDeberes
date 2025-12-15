# ==========================================
# Programación OO: Promedio de Clima
# ==========================================

class ClimaSemanal:
    # Constructor: Inicializa los atributos del objeto
    def __init__(self):
        # Este atributo es privado (encapsulamiento), solo la clase lo maneja directamente
        self.__temperaturas = []

    # Metodo para ingresar los datos diarios
    def ingresar_datos_diarios(self):
        print("--- Ingreso de Temperaturas (POO) ---")
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.__temperaturas.append(temp)

    # Metodo para calcular el promedio semanal
    def calcular_promedio(self):
        if not self.__temperaturas: # Verificamos si la lista no está vacía
            return 0
        suma = sum(self.__temperaturas)
        return suma / len(self.__temperaturas)

# Bloque principal
# Creamos el objeto (instancia) de la clase
clima_semana = ClimaSemanal()

# Usamos los métodos del objeto para realizar las tareas
clima_semana.ingresar_datos_diarios()
promedio_poo = clima_semana.calcular_promedio()

print(f"\nEl promedio semanal de temperatura (POO) es: {promedio_poo:.2f}°C")