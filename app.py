import customtkinter as ctk
from PIL import Image, ImageTk

# Crear la ventana principal
root = ctk.CTk()

# Cargar el icono como una imagen compatible
icono = ImageTk.PhotoImage(Image.open("bingo.png"))

# Cambiar el icono de la barra de tareas
root.iconphoto(False, icono)  # False significa que no afecta a otras ventanas derivadas

# Configurar dimensiones y mostrar la ventana
root.geometry("400x300")
root.title("Mi Aplicación")
root.mainloop()
