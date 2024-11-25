from PIL import Image

def png_a_ico(png_path, ico_path):
    # Abrir la imagen PNG
    with Image.open(png_path) as img:
        # Convertir la imagen a un formato ICO
        img.save(ico_path, format="ICO")

# Ejemplo de uso
png_a_ico('bingo.png', 'bingo.ico')

#pyinstaller --onefile --noconsole --icon=bingo.ico main.py