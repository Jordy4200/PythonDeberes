
# ==================== 1. ABSTRACCIÓN ====================
# Clase base con solo lo esencial
class Personaje:
    def __init__(self, nombre, poder):
        self._nombre = nombre  # _nombre es "privado"
        self._poder = poder

    def mostrar(self):
        return f"Personaje: {self._nombre}"

    # ==================== 2. ENCAPSULAMIENTO ====================
    # Protegemos el acceso a los datos
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo):
        if len(nuevo) > 2:
            self._nombre = nuevo


# ==================== 3. HERENCIA ====================
# Creamos una clase que hereda
class Avenger(Personaje):
    def __init__(self, nombre, poder, equipo):
        super().__init__(nombre, poder)
        self.equipo = equipo  # Nuevo atributo

    # ==================== 4. POLIMORFISMO ====================
    def mostrar(self):
        return f" {self._nombre} - Poder: {self._poder} - Equipo: {self.equipo}"


# ==================== SALIDA ====================
print("=" * 40)
print("   SISTEMA SIMPLE DE AVENGERS")
print("=" * 40)

# Crear objetos
heroe1 = Avenger("Iron Man", "Armadura", "Avengers")
heroe2 = Avenger("Thor", "Martillo", "Avengers")

# Mostrar información (POLIMORFISMO)
print(heroe1.mostrar())
print(heroe2.mostrar())

# Usar ENCAPSULAMIENTO
print(f"\nNombre actual: {heroe1.get_nombre()}")
heroe1.set_nombre("Tony Stark")
print(f"Nuevo nombre: {heroe1.get_nombre()}")

print("\n" + "=" * 40)
print("   ¡EJEMPLO TERMINADO!")
print("=" * 40)