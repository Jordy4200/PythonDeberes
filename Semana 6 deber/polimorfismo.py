# --- 1. CLASE PADRE (HERENCIA) ---
# Creamos una plantilla general para cualquier Eva.
class EvaGeneral:
    def __init__(self, piloto):
        self.piloto = piloto
        # --- 2. ENCAPSULACIÓN (DATO SECRETO) ---
        # Ponemos dos guiones bajos '__' antes del nombre.
        # Esto hace que la energía sea privada y nadie la cambie desde fuera por error.
        self.__energia = 100

    # Metodo para ver la energía (ya que está oculta)
    def ver_energia(self):
        return self.__energia

    # --- 3. POLIMORFISMO (La base) ---
    # Definimos una acción 'atacar' que cada Eva hará a su manera.
    def atacar(self):
        return "El Eva se prepara para atacar..."

# --- CLASES HIJAS (HERENCIA) ---
# El Eva 01 "hereda"  de EvaGeneral (tiene piloto y energía automática).

class Eva01(EvaGeneral):
    # Polimorfismo: Cambiamos cómo ataca el Eva 01
    def atacar(self):
        return f"{self.piloto} (Eva 01) usa: ¡Cuchillo Progresivo!"

class Eva02(EvaGeneral):
    # Polimorfismo: Cambiamos cómo ataca el Eva 02
    def atacar(self):
        return f"{self.piloto} (Eva 02) usa: ¡Rifle de Positrones!"

# --- PROBANDO EL PROGRAMA (OBJETOS) ---

# Creamos los objetos
shinji = Eva01("Shinji")
asuka = Eva02("Asuka")

print("--- INICIO DE COMBATE ---")

# Probamos el Polimorfismo (misma orden 'atacar', diferente resultado)
print(shinji.atacar())
print(asuka.atacar())

print("--- REPORTE DE ESTADO ---")
# Probamos la Encapsulación (leemos el dato secreto)
print(f"Energía de Shinji: {shinji.ver_energia()}%")