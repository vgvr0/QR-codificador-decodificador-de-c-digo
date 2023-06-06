import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

#Funcion para codificar
def codificar(texto):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(texto)
    qr.make(fit=True)
    imagen = qr.make_image(fill="black", back_color="white")
    imagen.save("codigo_qr.png")

#Funcion para decodificar
def decodificar(ruta_imagen):
    imagen = Image.open(ruta_imagen)
    codigo = decode(imagen)
    if codigo:
        return codigo[0].data.decode('utf-8')
    else:
        return None

# Ejemplo de uso
texto_para_codificar = "¡Hola, esto es un código QR!"
ruta_imagen_qr = "codigo_qr.png"

# Codificar texto y generar el código QR
codificar(texto_para_codificar)

# Decodifica el código QR y obtiene el texto
texto_decodificado = decodificar(ruta_imagen_qr)

print("Texto codificado:", texto_para_codificar)
print("Texto decodificado:", texto_decodificado)