import customtkinter as ctk
import random
from tkinter import messagebox
from PIL import Image
from tkinter.colorchooser import askcolor
popup_instance = None

numero_random_maximo = 0

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("......::::::::Bingo:::::::....")
app.geometry("1170x900") 


frame_superior = ctk.CTkFrame(app, height=50, corner_radius=0,fg_color="transparent")
frame_superior.pack(fill="both")

frame_centrado = ctk.CTkFrame(frame_superior, fg_color="transparent")
frame_centrado.place(relx=0.5, rely=0.5, anchor="center")  # Centramos el subframe

# Escribir "BINGO YAPERO" con colores diferentes
texto = "BINGO YAPERO"
colores = ["red", "green", "blue", "#ffbf4f", "#8fce00"] + ["purple"] * 7
# Crear etiquetas con cada letra en un color diferente
for i, letra in enumerate(texto):
    color = colores[i] if i < len(colores) else "black"
    etiqueta = ctk.CTkLabel(
        frame_centrado,  # Añadir la etiqueta al subframe
        text=letra,
        font=("Georgia", 48, "bold"),
        text_color=color
    )
    etiqueta.pack(side="left", padx=5)  # Colocar las letras en fila






frame_medio = ctk.CTkFrame(app, height=150, corner_radius=0,fg_color="transparent")
frame_medio.pack(fill="both")



frame_izquierdo = ctk.CTkFrame(frame_medio, fg_color="transparent")
frame_izquierdo.place(relx=0, rely=0, relwidth=0.5, relheight=1)  # Ocupa la mitad izquierda

frame_izquierdo_yape = ctk.CTkFrame(frame_izquierdo,fg_color="transparent")
frame_izquierdo_yape.place(relx=0, rely=0, relwidth=0.5, relheight=1) 


imagen = Image.open("img/qtmili.png")

imagen_ctk = ctk.CTkImage(light_image=imagen, size=(150, 150))  # Ajustar tamaño

imagen_label = ctk.CTkLabel(frame_izquierdo_yape, image=imagen_ctk, text="S/  ",font=("Arial", 24, "bold"), text_color="white",compound="center") # Texto sobre la imagen
imagen_label.pack(expand=True)


# inicio frame nombre yape
frame_derecho_nombre = ctk.CTkFrame(frame_izquierdo,fg_color="transparent")
frame_derecho_nombre.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)


contenedor_centrado = ctk.CTkFrame(frame_derecho_nombre, fg_color="transparent")
contenedor_centrado.pack(expand=True, fill="both",pady="50")

numero_entry_yape = ctk.CTkEntry(
    contenedor_centrado,
    placeholder_text="927 881 708",
    justify="center",
    font=("Helvetica", 24, "bold"),
    border_width=0,
    fg_color="transparent",
    width=300
)
numero_entry_yape.pack(pady=0)
numero_entry_yape.insert(0,"986 487 914")

nombre_entry_yape = ctk.CTkEntry(
    contenedor_centrado,
    placeholder_text="Ismael Gomez",
    justify="center",
    font=("Helvetica", 16, "bold"),
    border_width=0,
    fg_color="transparent"
)
nombre_entry_yape.pack(pady=0) 
nombre_entry_yape.insert(0,'Elda M. Rebaza')
# fin frame nombre yape







#inicio frame precio
# Frame principal derecho que ocupa la mitad derecha del frame_medio
frame_derecho_precio = ctk.CTkFrame(frame_medio, fg_color="transparent")
frame_derecho_precio.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)  # Ocupa la mitad derecha

# Contenedor izquierdo (amarillo)
contenedor_izquierdo_precio = ctk.CTkFrame(frame_derecho_precio, width=100, height=40, fg_color="transparent")
contenedor_izquierdo_precio.place(relx=0.25, rely=0.5, anchor="center")  # Centrado verticalmente y desplazado hacia la izquierda

# Contenedor derecho (azul)
contenedor_derecho_info = ctk.CTkFrame(frame_derecho_precio, width=150, height=40, fg_color="transparent")
contenedor_derecho_info.place(relx=0.75, rely=0.5, anchor="center") 

nombre_entry_yape = ctk.CTkEntry(
    contenedor_izquierdo_precio,
    placeholder_text="S/ 2.00",
    justify="center",
    font=("Helvetica", 36, "bold"),
    border_width=2,
    fg_color="transparent",
    width=200,
    border_color="black",
    
)
nombre_entry_yape.insert(0,"S/ 1.00")
nombre_entry_yape.pack(pady=0)  # Sin espacio vertical entre los campos


label_info = ctk.CTkLabel(
    master=contenedor_derecho_info,  # Cambia 'frame_superior' por el contenedor que prefieras
    text="Ocupados: 0 | Disponibles: 0",  # Texto inicial
    font=("Georgia", 14, "bold"),  # Fuente personalizada
    fg_color="transparent",  # Color de fondo del Label
    text_color="#000000"  # Color del texto
)
label_info.pack(pady=10) 

def configurar():
    global popup_instance
    if popup_instance is not None and popup_instance.winfo_exists():
        # Si el popup ya existe, no hacer nada
        return
    
    # Crear ventana emergente (popup)
    popup_instance = ctk.CTkToplevel(app)
    popup_instance.geometry("350x150")
    popup_instance.overrideredirect(True)  # Deshabilitar botones de cerrar, minimizar, maximizar
    popup_instance.resizable(False, False)

    # Centrar el popup en la ventana principal
    x_offset = app.winfo_x() + (app.winfo_width() // 2) - 150
    y_offset = app.winfo_y() + (app.winfo_height() // 2) - 175
    popup_instance.geometry(f"+{x_offset}+{y_offset}")

    # Marco principal del popup
    popup_frame = ctk.CTkFrame(popup_instance)
    popup_frame.pack(fill="both", expand=True, padx=10, pady=2)

    # Etiqueta y campo para cantidad de cuadros
    cuadros_label = ctk.CTkLabel(popup_frame, text="Cantidad de jugadores:", font=("Arial", 14))
    cuadros_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")  # Alinear a la izquierda
    cuadros_entry = ctk.CTkEntry(popup_frame, font=("Arial", 14), width=150)
    cuadros_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")  # Alinear a la derecha
    cuadros_entry.insert(0,30)

    # Etiqueta y campo para cantidad de círculos
    circulos_label = ctk.CTkLabel(popup_frame, text="Cantidad de Intentos:", font=("Arial", 14))
    circulos_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")  # Alinear a la izquierda
    circulos_entry = ctk.CTkEntry(popup_frame, font=("Arial", 14), width=150)
    circulos_entry.grid(row=1, column=1, padx=10, pady=5, sticky="e")  # Alinear a la derecha
    circulos_entry.insert(0,5)

    # Etiqueta y campo para precio
    #precio_label = ctk.CTkLabel(popup_frame, text="Precio (S/):", font=("Arial", 14))
    #precio_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")  # Alinear a la izquierda
    #precio_entry = ctk.CTkEntry(popup_frame, font=("Arial", 14), width=150)
    #precio_entry.grid(row=2, column=1, padx=10, pady=5, sticky="e")  # Alinear a la derecha

    # Función para manejar el botón OK
    def ok_action():
        try:
            cuadros = int(cuadros_entry.get())  # Convertir a int
            circulos = int(circulos_entry.get())  # Convertir a int
            #precio = int(precio_entry.get())  # Convertir a int
            resetear_sorteo()
            resetear_frame_inferior()
            global numero_random_maximo
            numero_random_maximo = cuadros
            crear_cuadros(cuadros, circulos)
            actualizar_label_info()
            popup_instance.destroy()  # Cerrar el popup
        except ValueError:
            # Mostrar error si no se puede convertir
            messagebox.showerror("Error", "Por favor, ingrese números válidos en todos los campos.")

    # Función para manejar el botón Cancelar
    def cancel_action():
        popup_instance.destroy()  # Cerrar el popup

    # Botones OK y Cancelar
    button_frame = ctk.CTkFrame(popup_frame)
    button_frame.grid(row=3, column=0, columnspan=2, pady=20)

    ok_button = ctk.CTkButton(button_frame, text="OK", font=("Arial", 14), width=100, command=ok_action)
    ok_button.grid(row=0, column=0, padx=10)

    cancel_button = ctk.CTkButton(button_frame, text="Cancelar", font=("Arial", 14), width=100, command=cancel_action)
    cancel_button.grid(row=0, column=1, padx=10)

    # Hacer que la ventana sea modal
    popup_instance.grab_set()  # Bloquear interacción con la ventana principal
    popup_instance.wait_window() 

botones_circulos = []
def crear_cuadros(cantidad_cuadros, cantidad_circulos):

    for i in range(cantidad_cuadros):
        cuadro = ctk.CTkFrame(
            frame_inferior,
            corner_radius=10,
            fg_color="#ffbf4f",
            border_width=1,  # Establecer el grosor del borde
            border_color="black"  # Establecer el color del borde
        )
        cuadro.grid(row=i // 8, column=i % 8, padx=2, pady=2)

        # Sección 1: Nombre del jugador y selección de color
        frame_nombre = ctk.CTkFrame(cuadro, corner_radius=0,fg_color="#ffbf4f")
        frame_nombre.pack(fill="x", pady=3,padx=5)

        nombre_entry = ctk.CTkEntry(frame_nombre, placeholder_text="...",justify="center",fg_color="#ffbf4f",font=("Georgia", 14,"bold"), border_width=0, width=100)
        nombre_entry.pack(fill="x",padx=0)

        nombre_entry.bind("<Button-3>", cambiar_color)
        nombre_entry.bind("<KeyRelease>", lambda event: actualizar_label_info())

        # Sección 2: Número de orden del cuadro
        frame_numero = ctk.CTkFrame(cuadro, corner_radius=0,fg_color="#ffbf4f")
        frame_numero.pack(fill="x", pady=0,padx=5)

        label_numero = ctk.CTkLabel(frame_numero, text=str(i + 1), font=("Georgia", 36,"bold"))
        label_numero.pack(fill="x", pady=0,padx=5)

        # Sección 3: Círculos
        frame_circulos = ctk.CTkFrame(cuadro, corner_radius=0,fg_color="#ffbf4f")
        frame_circulos.pack(fill="x", pady=3,padx=5)

        # Generar los círculos
        for j in range(cantidad_circulos):
            # Crear un círculo por cada cantidad de círculos solicitada
            def crear_boton_circulo(circulo_idx, cuadro=cuadro):
                btn_circulo = ctk.CTkButton(frame_circulos, text="",hover_color="#d2eb99", width=20, height=20, corner_radius=50, fg_color="white",border_width=2,border_color="black",
                                            command=lambda: cambiar_color_circulo(btn_circulo))
                btn_circulo.pack(side="left", padx=3)
                botones_circulos.append(btn_circulo)
            crear_boton_circulo(j)

def contar_cuadros_sin_nombre():
    cuadros_sin_nombre = 0
    
    for cuadro in frame_inferior.winfo_children():  # Iterar sobre todos los cuadros en el frame_inferior
        for child in cuadro.winfo_children():  # Buscar dentro de cada cuadro
            if isinstance(child, ctk.CTkFrame):  # Encontrar el frame_nombre
                for sub_child in child.winfo_children():
                    if isinstance(sub_child, ctk.CTkEntry):  # Buscar el campo nombre_entry
                        if sub_child.get().strip() == "":  # Verificar si está vacío
                            cuadros_sin_nombre += 1  # Incrementar el contador si está vacío
                        break  # Detenerse al encontrar el primer nombre_entry en el cuadro
    return cuadros_sin_nombre

def contar_cuadros_con_nombre():
    cuadros_con_nombre = 0
    
    for cuadro in frame_inferior.winfo_children():  # Iterar sobre todos los cuadros en el frame_inferior
        for child in cuadro.winfo_children():  # Buscar dentro de cada cuadro
            if isinstance(child, ctk.CTkFrame):  # Encontrar el frame_nombre
                for sub_child in child.winfo_children():
                    if isinstance(sub_child, ctk.CTkEntry):  # Buscar el campo nombre_entry
                        if sub_child.get().strip() != "":  # Verificar si no está vacío
                            cuadros_con_nombre += 1  # Incrementar el contador si no está vacío
                        break  # Detenerse al encontrar el primer nombre_entry en el cuadro
    return cuadros_con_nombre

def actualizar_label_info():
    cuadros_con_nombre = contar_cuadros_con_nombre()
    cuadros_sin_nombre = contar_cuadros_sin_nombre()
    texto = f"Ocupados: {cuadros_con_nombre} | Disponibles: {cuadros_sin_nombre}"
    label_info.configure(text=texto)

def reset_intentos():
    resetear_sorteo()
    for boton in botones_circulos:
        boton.configure(fg_color="white")

nombre_boton_yape = ctk.CTkButton(
    contenedor_izquierdo_precio,
    text="Configurar",  # El texto que aparecerá en el botón
    font=("Helvetica", 12, "bold"),  # Fuente y estilo
    border_width=2,
    #fg_color="blue",  # Color de fondo
    width=100,  # Ancho del botón
    height=30,  # Altura del botón
    command=configurar
)
nombre_boton_yape.pack(pady=5)

nombre_boton_limpiar = ctk.CTkButton(
    contenedor_izquierdo_precio,
    text="Limpiar",  # El texto que aparecerá en el botón
    font=("Helvetica", 12, "bold"),  # Fuente y estilo
    border_width=2,
    #fg_color="blue",  # Color de fondo
    width=100,  # Ancho del botón
    height=30,  # Altura del botón
    command=reset_intentos
)
nombre_boton_limpiar.pack(pady=5)




 #fin frame precio



#inicio frame abajo sorteo
frame_abajo = ctk.CTkFrame(app, corner_radius=0, fg_color="transparent", height=80)
frame_abajo.pack(fill="x")

# Frame para "sortear"
frame_sortear = ctk.CTkFrame(frame_abajo, corner_radius=0, fg_color="transparent", height=80)
frame_sortear.pack(side="left", padx=5)  # El uso de "side='left'" coloca los frames horizontalmente

numeros = []  # Los círculos estarán vacíos inicialmente
circulos = [] 
etiquetas = []

def resetear_sorteo():
    global numeros  # Acceder a la lista global
    numeros = []  # Vaciar la lista de números
    actualizar_numeros()

def resetear_frame_inferior():
    limpiar_frame(frame_inferior)

def actualizar_numeros():
    for i, etiqueta in enumerate(etiquetas):
        if i < len(numeros):  # Si hay un número para esta etiqueta
            if i == 0:  # El primer número (nuevo) será rojo
                etiqueta.configure(text=str(numeros[i]), text_color="white")  # Texto blanco
                circulos[i].configure(fg_color="red")  # Fondo rojo
            else:  # Los demás números serán melón
                etiqueta.configure(text=str(numeros[i]), text_color="black")  # Texto negro
                circulos[i].configure(fg_color="#FFDAB9")  # Fondo melón
        else:  # Si no hay un número, el círculo será blanco y vacío
            etiqueta.configure(text="")  # Vaciar texto
            circulos[i].configure(fg_color="white")  # Fondo blanco

def sortear():
    nuevo_numero = random.randint(1, numero_random_maximo)  # Generar un número aleatorio entre 1 y 50
    numeros.insert(0, nuevo_numero)  # Insertar el nuevo número al inicio de la lista
    if len(numeros) > 50:  # Mantener solo los últimos 10 números
        numeros.pop()
    actualizar_numeros()
    # Pintar un círculo verde en el cuadro correspondiente al número sorteado
    for cuadro in frame_inferior.winfo_children():  # Iterar sobre todos los cuadros
        # Buscar el número en la etiqueta de este cuadro
        for child in cuadro.winfo_children():
            if isinstance(child, ctk.CTkFrame):  # Buscar la sección que contiene el número
                for sub_child in child.winfo_children():
                    if isinstance(sub_child, ctk.CTkLabel):
                        if sub_child.cget("text") == str(nuevo_numero):  # Si el número coincide
                            # Pintar solo el primer botón blanco dentro del contenedor de círculos
                            for circulo in cuadro.winfo_children():
                                if isinstance(circulo, ctk.CTkFrame):  # Encontrar el contenedor de círculos
                                    for boton in circulo.winfo_children():
                                        if isinstance(boton, ctk.CTkButton) and boton.cget("fg_color") == "white":
                                            boton.configure(fg_color="green")  # Pintar de verde
                                            return

sort_button = ctk.CTkButton(frame_sortear, text="", font=("Arial", 12), width=50, height=50, corner_radius=25,
                            command=sortear)
sort_button.grid(row=0, column=0, padx=10, pady=10)


# Frame para "tubo"
frame_tubo = ctk.CTkFrame(frame_abajo, corner_radius=15, fg_color="white", height=80, border_width=2, border_color="black")
frame_tubo.pack(side="left", fill="both", expand=True,padx="3", pady="10")  # Expande para ocupar el resto del espacio disponible


for i in range(50):
    circulo = ctk.CTkFrame(frame_tubo, width=50, height=50, fg_color="transparent", corner_radius=25)  # Fondo inicial gris
    circulo.pack(side="left", padx=5, pady=5)
    circulos.append(circulo)
    # Etiqueta para el número dentro del círculo
    etiqueta = ctk.CTkLabel(circulo, text="", font=("Arial", 18, "bold"), text_color="black")
    etiqueta.place(relx=0.5, rely=0.5, anchor="center")  # Centrar la etiqueta en el círculo
    etiquetas.append(etiqueta)
#fin frame abajo sorteo



def cambiar_color(event):
    """Abre una paleta de colores y cambia el color del componente en que se hizo doble clic."""
    widget = event.widget
    color = askcolor(title="Selecciona un color")[1]
    if color:
        widget.configure(bg=color)

# Cambiar color de un círculo
def cambiar_color_circulo(btn):
    # Cambiar el color entre blanco y verde
    if btn.cget("fg_color") == "white":
        btn.configure(fg_color="#8fce00")
    else:
        btn.configure(fg_color="white")

def limpiar_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
def toggle_frame(frame):
    if frame.winfo_ismapped():  # Si el frame está visible
        frame.pack_forget()     # Ocultar el frame
    else:
        frame.pack(fill="both", expand=True)


frame_inferior = ctk.CTkFrame(app, corner_radius=0,fg_color="transparent")
frame_inferior.pack(fill="both", padx="5", pady="5", expand=True)


app.mainloop()