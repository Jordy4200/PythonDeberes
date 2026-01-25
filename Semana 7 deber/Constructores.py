class CazaDragones:
    """
    Clase que representa a un cazador como Ragna o Crimson.
    """

    # 1. EL CONSTRUCTOR (__init__)
    # Este metodo es el "nacimiento" del objeto.
    # Se ejecuta AUTOMÁTICAMENTE cuando creas una instancia de la clase.
    def __init__(self, nombre, magia):
        self.nombre = nombre
        self.magia = magia
        print(f"✨ [INICIO] ¡{self.nombre} ha entrado al campo de batalla!")
        print(f"   -> Cargando poder: {self.magia}...")

    # Un metodo normal para que el personaje haga algo
    def usar_tecnica_definitiva(self):
        print(f"⚔️  ¡{self.nombre} lanza un ataque brutal con {self.magia}!")
        print("   -> ¡Un dragón ha sido eliminado!")

    # 2. EL DESTRUCTOR (__del__)
    # Este metodo es el "final" del objeto.
    # Se ejecuta cuando borras el objeto o cuando el programa termina y
    # Python necesita limpiar la memoria (sacar la basura).
    def __del__(self):
        print(f"💀 [FIN] {self.nombre} se ha quedado sin energía o la misión terminó.")
        print("   -> Limpiando rastros y liberando memoria...")

# --- ZONA DE PRUEBAS ---

if __name__ == "__main__":
    print("--- Comienza la historia ---")

    # Aquí llamamos al CONSTRUCTOR (__init__) automáticamente
    ragna = CazaDragones("Ragna", "Artes de Plata (Silverine)")

    # Usamos al objeto
    ragna.usar_tecnica_definitiva()

    print("--- Ragna está descansando un momento... ---")

    # Aquí forzamos el DESTRUCTOR (__del__) para el ejemplo.
    # Si no pones esta línea, el destructor se ejecutará solo al final del script.
    del ragna

    print("--- Fin de la historia ---")