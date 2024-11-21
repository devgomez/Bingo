import customtkinter as ctk
from tkinter import colorchooser

# Crear la ventana principal
app = ctk.CTk()
app.title("Formulario con CustomTkinter")
app.geometry("800x600")  # Establecer tamaño de ventana

# ========================
# Sección 1: Rojo
# ========================
frame_seccion1 = ctk.CTkFrame(app, height=100, corner_radius=0)
frame_seccion1.pack(fill="x", padx=10, pady=(10, 0))

# Crear un contenedor de dos secciones dentro de la sección 1
frame_izquierda = ctk.CTkFrame(frame_seccion1, height=100, corner_radius=0)
frame_izquierda.pack(side="left", fill="y", expand=True)

frame_derecha = ctk.CTkFrame(frame_seccion1, height=100, corner_radius=0)
frame_derecha.pack(side="right", fill="y", expand=True)

# Sección izquierda: "BINGO" con colores diferentes
colores = ["red", "green", "blue", "yellow", "purple"]

# Escribir "BINGO" con cada letra en un color diferente, alineado al centro
for i, letra in enumerate("BINGO"):
    label = ctk.CTkLabel(frame_izquierda, text=letra, text_color=colores[i], font=("Arial", 36))
    label.pack(side="left", padx=5)

# Sección derecha: dos cajas de texto y un botón "GENERAR"
# Cajas de texto
entry1 = ctk.CTkEntry(frame_derecha, placeholder_text="Cantidad de cuadros", width=150)
entry1.pack(pady=5)

entry2 = ctk.CTkEntry(frame_derecha, placeholder_text="Cantidad de círculos", width=150)
entry2.pack(pady=5)


# Botón Generar
def generar():
    try:
        cantidad_cuadros = int(entry1.get())
        cantidad_circulos = int(entry2.get())
        crear_cuadros(cantidad_cuadros, cantidad_circulos)
    except ValueError:
        print("Por favor ingrese números válidos.")


btn_generar = ctk.CTkButton(frame_derecha, text="Generar", command=generar)
btn_generar.pack(pady=5)

# ========================
# Sección 3: Azul (donde se crearán los cuadros)
# ========================
frame_seccion3 = ctk.CTkFrame(app, corner_radius=0)
frame_seccion3.pack(fill="both", expand=True, padx=10, pady=(0, 10))


# Función para crear los cuadros
def crear_cuadros(cantidad_cuadros, cantidad_circulos):
    for i in range(cantidad_cuadros):
        cuadro = ctk.CTkFrame(
            frame_seccion3,
            corner_radius=10,
            fg_color="yellow",
            border_width=2,  # Establecer el grosor del borde
            border_color="black"  # Establecer el color del borde
        )
        cuadro.grid(row=i // 5, column=i % 5, padx=2, pady=2)

        # Sección 1: Nombre del jugador y selección de color
        frame_nombre = ctk.CTkFrame(cuadro, height=50, corner_radius=0,fg_color="red")
        frame_nombre.pack(fill="x", pady=3,padx=5)

        nombre_entry = ctk.CTkEntry(frame_nombre, placeholder_text="Nombre", width=100)
        nombre_entry.pack(padx=5)

        def seleccionar_color(event, entry):
            # Abrir el cuadro de diálogo de colores
            color = colorchooser.askcolor(title="Seleccionar Color")[
                1]  # El segundo valor es el color en formato hexadecimal
            if color:  # Si se seleccionó un color
                entry.configure(fg_color=color)

        nombre_entry.bind("<Button-3>",lambda event,entry=nombre_entry :seleccionar_color(event, nombre_entry))

        # Sección 2: Número de orden del cuadro
        frame_numero = ctk.CTkFrame(cuadro, height=30, corner_radius=0,fg_color="yellow")
        frame_numero.pack(fill="x", pady=0,padx=5)

        label_numero = ctk.CTkLabel(frame_numero, text=str(i + 1), font=("Arial", 36))
        label_numero.pack(fill="x", pady=0,padx=5)

        # Sección 3: Círculos
        frame_circulos = ctk.CTkFrame(cuadro, height=30, corner_radius=0,fg_color="yellow")
        frame_circulos.pack(fill="x", pady=3,padx=5)

        # Generar los círculos
        for j in range(cantidad_circulos):
            # Crear un círculo por cada cantidad de círculos solicitada
            def crear_boton_circulo(circulo_idx, cuadro=cuadro):
                btn_circulo = ctk.CTkButton(frame_circulos, text="",hover_color="#90EE90", width=20, height=20, corner_radius=50, fg_color="white",
                                            command=lambda: cambiar_color(btn_circulo))
                btn_circulo.pack(side="left", padx=3)

            crear_boton_circulo(j)


# Cambiar color de un círculo
def cambiar_color(btn):
    # Cambiar el color entre blanco y verde
    if btn.cget("fg_color") == "white":
        btn.configure(fg_color="green")
    else:
        btn.configure(fg_color="white")


# Ejecutar la aplicación
app.mainloop()
