import tkinter as tk
from tkinter import messagebox


# ==========================================
# LÓGICA DE LA APLICACIÓN (Manejo de Eventos)
# ==========================================

def agregar_dato():
    """Obtiene el texto del campo de entrada y lo añade a la lista."""
    dato = entrada_texto.get()  # Obtenemos lo que el usuario escribió

    if dato.strip():  # Verificamos que no esté vacío o solo tenga espacios
        lista_datos.insert(tk.END, dato)  # Insertamos al final de la lista
        entrada_texto.delete(0, tk.END)  # Limpiamos el campo de texto
    else:
        # Mostramos una alerta si el usuario intenta agregar algo vacío
        messagebox.showwarning("Advertencia", "Por favor, ingresa un dato válido.")


def limpiar_datos():
    """Borra todos los elementos de la lista y limpia el campo de texto."""
    lista_datos.delete(0, tk.END)  # Borra desde el índice 0 hasta el final
    entrada_texto.delete(0, tk.END)


# ==========================================
# DISEÑO DE LA INTERFAZ GRÁFICA  SIMPLE (GUI)
# ==========================================

# 1. Creación de la ventana principal
ventana = tk.Tk()
ventana.title("GUI  DE PRUEBA - Gestor de Datos")  # Título descriptivo
ventana.geometry("400x350")  # Tamaño inicial de la ventana
ventana.config(padx=20, pady=20)  # Márgenes internos

# 2. Componentes (Widgets)

# Etiqueta de instrucción
etiqueta_instruccion = tk.Label(ventana, text="Ingresa un nuevo dato:", font=("Arial", 10))
etiqueta_instruccion.pack(anchor="w", pady=(0, 5))

# Campo de texto para que el usuario escriba
entrada_texto = tk.Entry(ventana, width=40)
entrada_texto.pack(pady=5)

# Botón para agregar (Conecta con la función agregar_dato)
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato, bg="lightblue")
boton_agregar.pack(pady=5)

# Etiqueta para la lista
etiqueta_lista = tk.Label(ventana, text="Datos registrados:", font=("Arial", 10))
etiqueta_lista.pack(anchor="w", pady=(15, 5))

# Lista (Listbox) para mostrar los datos ingresados
lista_datos = tk.Listbox(ventana, width=50, height=8)
lista_datos.pack(pady=5)

# Botón para limpiartodo (Conecta con la función limpiar_datos)
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos, bg="lightcoral")
boton_limpiar.pack(pady=10)

# ==========================================
# BUCLE PRINCIPAL DE EJECUCIÓN
# ==========================================
# Mantiene la ventana abierta y esperando los eventos del usuario
ventana.mainloop()