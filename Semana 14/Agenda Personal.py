import tkinter as tk
from tkinter import ttk, messagebox
# Importamos tkcalendar para el DatePicker.
from tkcalendar import DateEntry


# --- DECLARACIÓN DE FUNCIONES ---

def agregar_evento():
    # Obtenemos el texto que el usuario escribió en las cajas
    fecha = entrada_fecha.get()
    hora = entrada_hora.get()
    descripcion = entrada_descripcion.get()

    # Validamos que no dejen nada en blanco
    if fecha == "" or hora == "" or descripcion == "":
        messagebox.showwarning("Advertencia", "Por favor, llena todos los campos.")
    else:
        # Insertamos los datos en nuestra tabla (TreeView)
        tabla.insert("", tk.END, values=(fecha, hora, descripcion))

        # Limpiamos las cajas de texto de hora y descripción para agregar uno nuevo
        entrada_hora.delete(0, tk.END)
        entrada_descripcion.delete(0, tk.END)


def eliminar_evento():
    # Vemos qué fila de la tabla seleccionó el usuario
    seleccion = tabla.selection()

    # Si no seleccionó nada, le avisamos
    if not seleccion:
        messagebox.showwarning("Advertencia", "Selecciona un evento de la lista para eliminar.")
        return

    # Mostramos el diálogo de confirmación (como pedía la tarea)
    respuesta = messagebox.askyesno("Confirmar", "¿Seguro que quieres eliminar este evento?")

    # Si dice que sí, borramos la fila seleccionada
    if respuesta:
        for elemento in seleccion:
            tabla.delete(elemento)


# --- DECLARACIÓN DE LA VENTANA PRINCIPAL ---
root = tk.Tk()
root.title("Mi Agenda Personal")
root.geometry("600x500")

# --- CONTENEDORES (Paneles/Frames para organizartodo) ---

# Frame para agrupar los textos y las cajas de entrada
frame_entrada = tk.Frame(root, pady=10)
frame_entrada.pack()

# Frame para agrupar los botones
frame_botones = tk.Frame(root, pady=10)
frame_botones.pack()

# Frame para mostrar la tabla de eventos
frame_lista = tk.Frame(root, pady=10)
frame_lista.pack(fill=tk.BOTH, expand=True)

# --- COMPONENTES DEL FRAME DE ENTRADA ---

# Etiqueta y Selector de Fecha (DatePicker)
tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
entrada_fecha = DateEntry(frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2,
                          date_pattern='dd/mm/yyyy')
entrada_fecha.grid(row=0, column=1, padx=5, pady=5)

# Etiqueta y caja de texto para la Hora
tk.Label(frame_entrada, text="Hora (Ej. 14:30):").grid(row=1, column=0, padx=5, pady=5)
entrada_hora = tk.Entry(frame_entrada)
entrada_hora.grid(row=1, column=1, padx=5, pady=5)

# Etiqueta y caja de texto para la Descripción
tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
entrada_descripcion = tk.Entry(frame_entrada, width=30)
entrada_descripcion.grid(row=2, column=1, padx=5, pady=5)

# --- COMPONENTES DEL FRAME DE BOTONES ---

# Botón para agregar
btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.pack(side=tk.LEFT, padx=10)

# Botón para eliminar
btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.pack(side=tk.LEFT, padx=10)

# Botón para salir (cierra la ventana)
btn_salir = tk.Button(frame_botones, text="Salir", command=root.quit)
btn_salir.pack(side=tk.LEFT, padx=10)

# --- COMPONENTES DEL FRAME DE LISTA (La tabla o TreeView) ---

# Definimos cuántas columnas tendrá la tabla
columnas = ("Fecha", "Hora", "Descripción")
tabla = ttk.Treeview(frame_lista, columns=columnas, show="headings")

# Le ponemos título a cada columna
tabla.heading("Fecha", text="Fecha")
tabla.heading("Hora", text="Hora")
tabla.heading("Descripción", text="Descripción")

# Ajustamos qué tan ancha se ve cada columna
tabla.column("Fecha", width=100)
tabla.column("Hora", width=100)
tabla.column("Descripción", width=300)

# Mostramos la tabla en la ventana
tabla.pack(fill=tk.BOTH, expand=True, padx=20)

# Arrancamos la aplicación para que se quede abierta escuchando eventos
root.mainloop()