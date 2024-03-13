from PIL import Image

def generar_miniatura(imagen_grande, tamano_miniatura):
    # Abrir la imagen grande
    imagen = Image.open(imagen_grande)

    # Generar la miniatura
    imagen_miniatura = imagen.resize(tamano_miniatura)

    # Guardar la miniatura
    nombre_miniatura = f"miniatura_{imagen_grande}"
    imagen_miniatura.save(nombre_miniatura)

    print(f"Miniatura generada y guardada como {nombre_miniatura}")

# Ejemplo de uso
imagen_grande_path = "oso.jpg"
tamano_miniatura = (100, 100)  # Puedes ajustar el tamaño según tus necesidades

generar_miniatura(imagen_grande_path, tamano_miniatura)
