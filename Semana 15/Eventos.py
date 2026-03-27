import tkinter as tk
from tkinter import messagebox


# Función para añadir una tarea a la lista
def agregar_tarea(event=None):
    # El "event=None" sirve para que esta función sirva tanto al darle clic al botón
    # como al presionar la tecla Enter.

    tarea = entrada_tarea.get()  # Sacamos el texto que escribiste en el cuadro

    if tarea != "":  # Verificamos que no esté vacío
        lista_tareas.insert(tk.END, tarea)  # Metemos la tarea al final de la lista
        entrada_tarea.delete(0, tk.END)  # Limpiamos el cuadro de texto para la siguiente
    else:
        # Si está vacío, lanzamos un mensajito de advertencia
        messagebox.showwarning("Aviso", "¡No puedes añadir una tarea vacía!")


# Función para pintar la tarea y que se vea como terminada
def marcar_completada(event=None):
    try:
        seleccion = lista_tareas.curselection()  # Vemos qué tarea tocaste con el mouse
        indice = seleccion[0]  # Sacamos el número de posición de esa tarea

        # Le cambiamos el color de fondo a un verde clarito y la letra a gris
        # para que visualmente se note que ya está lista.
        lista_tareas.itemconfig(indice, bg="#d3f9d8", fg="#888888")

        # Quitamos la selección para que se vea bien el cambio de color
        lista_tareas.selection_clear(0, tk.END)
    except IndexError:
        # Si presionas el botón sin haber seleccionado ninguna tarea, te avisa
        messagebox.showwarning("Aviso", "Selecciona una tarea para marcarla como completada.")


# Función para borrar la tarea de la lista
def eliminar_tarea():
    try:
        seleccion = lista_tareas.curselection()
        indice = seleccion[0]
        lista_tareas.delete(indice)  # Borramos la tarea en esa posición exacta
    except IndexError:
        messagebox.showwarning("Aviso", "Selecciona una tarea para eliminarla.")


# --- Creación de la ventana principal ---
ventana = tk.Tk()
ventana.title("Mi Lista de Tareas")
ventana.geometry("400x480")  # Tamaño de la ventanita
ventana.config(bg="#f4f4f4")  # Color de fondo general

# --- Componentes visuales ---

# Título arriba detodo
etiqueta_titulo = tk.Label(ventana, text="Mis Tareas Pendientes", font=("Arial", 16, "bold"), bg="#f4f4f4")
etiqueta_titulo.pack(pady=10)  # El pady es para darle un respiro de espacio arriba y abajo

# Cuadro de texto para escribir
entrada_tarea = tk.Entry(ventana, font=("Arial", 12), width=30)
entrada_tarea.pack(pady=10)
# Vinculamos la tecla "Enter" a la función de agregar_tarea
entrada_tarea.bind("<Return>", agregar_tarea)

# Botón para añadir
boton_agregar = tk.Button(ventana, text="Añadir Tarea", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"),
                          command=agregar_tarea)
boton_agregar.pack(pady=5)

# La caja grande donde se ven las tareas (Listbox)
lista_tareas = tk.Listbox(ventana, font=("Arial", 12), width=35, height=10, selectbackground="#a6a6a6")
lista_tareas.pack(pady=10)
# Evento extra (opcional): si le das doble clic rápido a una tarea, se marca como completada
lista_tareas.bind("<Double-Button-1>", marcar_completada)

# Botón para marcar como completada
boton_completar = tk.Button(ventana, text="Marcar como Completada", bg="#2196F3", fg="white",
                            font=("Arial", 10, "bold"), command=marcar_completada)
boton_completar.pack(pady=5)

# Botón para eliminar
boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", bg="#f44336", fg="white", font=("Arial", 10, "bold"),
                           command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# --- Iniciar el programa ---
# Esto hace que la ventana se quede abierta esperando a que hagas clics
ventana.mainloop()