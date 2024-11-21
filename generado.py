import customtkinter as ctk
import random
from tkinter import messagebox

# Configuración inicial
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Crear ventana principal
root = ctk.CTk()
root.title("Bingo Yapero")
root.geometry("600x600")
root.resizable(False, False)

# Variables para los números sorteados
numeros = [""] * 7  # Los círculos estarán vacíos inicialmente
botones = []  # Lista para guardar los botones de números

# Función para actualizar los números sorteados
def actualizar_numeros():
    for i, boton in enumerate(botones):
        if i == 0 and numeros[i] != "":  # El primer número (nuevo) será rojo con texto blanco
            boton.configure(text=str(numeros[i]), fg_color="red", text_color="white")
        elif numeros[i] != "":  # Los demás números serán melón con texto negro
            boton.configure(text=str(numeros[i]), fg_color="#FFDAB9", text_color="black")
        else:  # Si el número está vacío, el botón será transparente
            boton.configure(text="", fg_color="lightgrey", text_color="black")

# Función para manejar el botón SORT
def sortear():
    nuevo_numero = random.randint(1, 50)  # Generar un número aleatorio entre 1 y 50
    numeros.insert(0, nuevo_numero)  # Insertar el nuevo número al inicio de la lista
    if len(numeros) > 7:  # Mantener solo los últimos 7 números
        numeros.pop()
    actualizar_numeros()  # Actualizar los botones

# Función para manejar el botón Configurar
def configurar():
    # Crear ventana emergente (popup)
    popup = ctk.CTkToplevel(root)
    popup.geometry("300x350")
    popup.overrideredirect(True)  # Deshabilitar botones de cerrar, minimizar, maximizar
    popup.resizable(False, False)

    # Centrar el popup en la ventana principal
    x_offset = root.winfo_x() + (root.winfo_width() // 2) - 150
    y_offset = root.winfo_y() + (root.winfo_height() // 2) - 150
    popup.geometry(f"+{x_offset}+{y_offset}")

    # Marco principal del popup
    popup_frame = ctk.CTkFrame(popup)
    popup_frame.pack(fill="both", expand=True, padx=10, pady=2)

    # Etiqueta y campo para cantidad de cuadros
    cuadros_label = ctk.CTkLabel(popup_frame, text="Cantidad de cuadros:", font=("Arial", 14))
    cuadros_label.pack(pady=2)
    cuadros_entry = ctk.CTkEntry(popup_frame, font=("Arial", 14), width=200)
    cuadros_entry.pack(pady=5)

    # Etiqueta y campo para cantidad de círculos
    circulos_label = ctk.CTkLabel(popup_frame, text="Cantidad de círculos:", font=("Arial", 14))
    circulos_label.pack(pady=10)
    circulos_entry = ctk.CTkEntry(popup_frame, font=("Arial", 14), width=200)
    circulos_entry.pack(pady=5)

    # Etiqueta y campo para precio
    precio_label = ctk.CTkLabel(popup_frame, text="Precio (S/):", font=("Arial", 14))
    precio_label.pack(pady=10)
    precio_entry = ctk.CTkEntry(popup_frame, font=("Arial", 14), width=200)
    precio_entry.pack(pady=5)

    # Función para manejar el botón OK
    def ok_action():
        messagebox.showinfo("Confirmación", "OK")
        popup.destroy()  # Cerrar el popup

    # Función para manejar el botón Cancelar
    def cancel_action():
        popup.destroy()  # Cerrar el popup

    # Botones OK y Cancelar
    button_frame = ctk.CTkFrame(popup_frame)
    button_frame.pack(pady=20)

    ok_button = ctk.CTkButton(button_frame, text="OK", font=("Arial", 14), width=100, command=ok_action)
    ok_button.grid(row=0, column=0, padx=10)

    cancel_button = ctk.CTkButton(button_frame, text="Cancelar", font=("Arial", 14), width=100, command=cancel_action)
    cancel_button.grid(row=0, column=1, padx=10)

# Título principal
titulo_label = ctk.CTkLabel(root, text="BINGO YAPERO", font=("Arial", 24, "bold"))
titulo_label.pack(pady=10)

# Marco superior con información del usuario y precio
info_frame = ctk.CTkFrame(root)
info_frame.pack(pady=10, padx=10, fill="x")

# Información del usuario
user_label = ctk.CTkLabel(info_frame, text="927 881 705\nIsmael Gomez", font=("Arial", 14), width=150, height=60,
                          fg_color=("white", "pink"), justify="center", corner_radius=8)
user_label.pack(side="left", padx=10)

# Precio
precio_label = ctk.CTkLabel(info_frame, text="S/ 2.00", font=("Arial", 18, "bold"), width=150, height=60,
                            fg_color=("white", "red"), justify="center", corner_radius=8)
precio_label.pack(side="right", padx=10)

# Botón Configurar
config_button = ctk.CTkButton(info_frame, text="Configurar", font=("Arial", 14), width=100, height=40, command=configurar)
config_button.pack(pady=10, anchor="center")

# Marco de números sorteados
sorteo_frame = ctk.CTkFrame(root, fg_color=("white", "lightgrey"))
sorteo_frame.pack(pady=10, padx=10, fill="x")

# Botón "Sort"
sort_button = ctk.CTkButton(sorteo_frame, text="SORT", font=("Arial", 12), width=50, height=50, corner_radius=25,
                            command=sortear)
sort_button.grid(row=0, column=0, padx=10, pady=10)

# Números sorteados (como botones circulares)
for i in range(7):
    numero_button = ctk.CTkButton(sorteo_frame, text="", font=("Arial", 18, "bold"),  # Texto inicial vacío
                                  width=50, height=50, fg_color="lightgrey", text_color="black",  # Fondo inicial gris
                                  corner_radius=25)
    numero_button.grid(row=0, column=i + 1, padx=5, pady=5)
    botones.append(numero_button)

# Ejecutar aplicación
root.mainloop()
