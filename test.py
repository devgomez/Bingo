import tkinter as tk
import customtkinter as ctk

def animacion_boton(btn):
    # Función de animación que se ejecuta cada vez que el botón es presionado
    def animar(i=0):
        # Se calcula el ángulo para el giro del botón
        angle = (i % 360)
        
        # Cambiar el color del botón en cada paso de la animación
        colores = ["#ffbf4f", "lightgreen", "lightblue", "pink", "#ff6f61"]
        btn.configure(fg_color=colores[i % len(colores)])

        # Gira el canvas y sus elementos
        canvas.itemconfig(btn_id, angle=angle)

        # Continuar la animación cada 50 ms
        if i < 100:  # Puedes hacer que dure más tiempo cambiando el número
            btn.after(50, animar, i + 1)
        else:
            # Después de la animación, volver al estado normal del botón
            btn.configure(width=150, height=50, fg_color="white", text="Sorteo")

    # Llamar a la función de animación
    animar()

# Crear la ventana
app = ctk.CTk()

# Crear un Canvas para la animación
canvas = tk.Canvas(app, width=200, height=100)
canvas.pack(pady=20)

# Crear el botón dentro del Canvas
btn = ctk.CTkButton(app, text="Sorteo", width=150, height=50, fg_color="white", command=lambda: animacion_boton(btn))
btn_id = canvas.create_window(100, 50, window=btn)

app.mainloop()
