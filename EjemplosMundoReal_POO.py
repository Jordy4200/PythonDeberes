# ==========================================
# TAREA: Ejemplo Real de POO
# CASO: Una Mascota (Perro) que juega y duerme
# ==========================================

class Perro:
    # Este es el "molde". Se ejecuta automático al crear el perro.
    def __init__(self, nombre, raza):
        self.nombre = nombre   # Le ponemos nombre
        self.raza = raza       # Definimos su raza
        self.energia = 100     # Empieza con la energía al máximo

    # Una acción simple: el perro ladra
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau Guau!")

    # Otra acción: jugar. Esto gasta energía.
    def jugar(self):
        if self.energia >= 20:
            self.energia = self.energia - 20
            print(f"{self.nombre} corrió por el parque. Energía restante: {self.energia}")
        else:
            # Si tiene poca energía, no juega
            print(f"{self.nombre} está muy cansado para jugar. ¡Mandalo a dormir!")

    # Acción para recuperar energía
    def dormir(self):
        print(f"{self.nombre} se echó una siesta...")
        self.energia = 100 # Vuelve a estar a tope
        print("¡Baterías recargadas al 100%!")


# --- ZONA DE PRUEBAS ---

# 1. Creamos el perro (Instancia)
mi_perro = Perro("Mia", "Labrador")

# 2. Interactuamos con él
mi_perro.ladrar()

# 3. Lo ponemos a jugar varias veces para cansarlo
mi_perro.jugar()
mi_perro.jugar()
mi_perro.jugar() # Aquí ya debería tener poca energía

# 4. Intentamos jugar cansado y luego lo dormimos
mi_perro.jugar() # Probablemente te diga que está cansado
mi_perro.dormir()