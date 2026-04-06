import tkinter as tk
from tkinter import messagebox


# ==========================================
# Funciones (Manejadores de Eventos)
# ==========================================

def agregar_tarea(event=None):
    # Obtenemos el texto que el usuario escribió
    tarea = entrada_tarea.get()

    if tarea != "":  # Verificamos que no esté vacío
        lista_tareas.insert(tk.END, tarea)  # Lo ponemos al final de la lista
        entrada_tarea.delete(0, tk.END)  # Limpiamos el cuadro de texto para la siguiente
    else:
        # Si está vacío, mostramos un pequeño aviso
        messagebox.showwarning("Aviso", "Por favor escribe una tarea antes de añadir.")


def completar_tarea(event=None):
    try:
        # Buscamos qué tarea está seleccionada con el clic
        seleccion = lista_tareas.curselection()
        indice = seleccion[0]
        tarea_actual = lista_tareas.get(indice)

        # Revisamos si ya tiene el visto bueno para no duplicarlo
        if not tarea_actual.startswith("✓ "):
            # La borramos y la volvemos a insertar con un visto y otro color
            lista_tareas.delete(indice)
            lista_tareas.insert(indice, "✓ " + tarea_actual)
            # Feedback visual: Fondo verde claro para tareas completadas
            lista_tareas.itemconfig(indice, {'bg': '#d3ffd3'})
            # Quitamos la selección para que no se quede marcada en azul
            lista_tareas.selection_clear(0, tk.END)
    except IndexError:
        pass  # Si presionan "C" pero no han seleccionado nada, no hace nada y no da error


def eliminar_tarea(event=None):
    try:
        seleccion = lista_tareas.curselection()
        indice = seleccion[0]
        lista_tareas.delete(indice)  # Borra la tarea seleccionada de la lista
    except IndexError:
        pass


def cerrar_aplicacion(event=None):
    ventana.destroy()  # Cierra la ventana principal


# ==========================================
# Configuración de la Interfaz Gráfica
# ==========================================

ventana = tk.Tk()
ventana.title("Gestión de Tareas")
ventana.geometry("400x480")  # Tamaño de la ventana adaptado para Windows

# Título principal
etiqueta_titulo = tk.Label(ventana, text="Mis Tareas Pendientes", font=("Arial", 14, "bold"))
etiqueta_titulo.pack(pady=15)

# Cuadro de entrada (Entry)
entrada_tarea = tk.Entry(ventana, width=40, font=("Arial", 11))
entrada_tarea.pack(pady=5)

# Botón para añadir (Evento de clic)
# Nota: El command= llama a la función sin pasar parámetros
btn_agregar = tk.Button(ventana, text="Añadir Tarea (Enter)", command=agregar_tarea, bg="#add8e6")
btn_agregar.pack(pady=5)

# Lista donde se muestran las tareas (Listbox)
lista_tareas = tk.Listbox(ventana, width=45, height=15, font=("Arial", 11))
lista_tareas.pack(pady=10)

# Un pequeño marco para agrupar los dos botones de abajo
marco_botones = tk.Frame(ventana)
marco_botones.pack(pady=5)

btn_completar = tk.Button(marco_botones, text="Completada (C)", command=completar_tarea, bg="#90ee90")
btn_completar.grid(row=0, column=0, padx=10)

btn_eliminar = tk.Button(marco_botones, text="Eliminar (Supr/D)", command=eliminar_tarea, bg="#ffcccb")
btn_eliminar.grid(row=0, column=1, padx=10)

# ==========================================
# Vinculación de Atajos de Teclado (Event Binding)
# ==========================================

# Enter para añadir tarea
ventana.bind('<Return>', agregar_tarea)

# Teclas para completar la tarea (C minúscula y mayúscula)
ventana.bind('<c>', completar_tarea)
ventana.bind('<C>', completar_tarea)

# Teclas para eliminar (Delete/Suprimir, y la D minúscula/mayúscula)
ventana.bind('<Delete>', eliminar_tarea)
ventana.bind('<d>', eliminar_tarea)
ventana.bind('<D>', eliminar_tarea)

# Escape para cerrar el programa
ventana.bind('<Escape>', cerrar_aplicacion)

# Arrancamos el bucle principal de la aplicación
ventana.mainloop()