from rembg import remove
from PIL import Image

nomeFoto = "tatoo1981"
fotoEntrada = "C:/Users/cydyq/AeC/Seleniun/" + nomeFoto + ".jpg"
fotoSaida = "C:/Users/cydyq/AeC/Seleniun/" + nomeFoto + "_out.png"

without_bg = remove(Image.open(fotoEntrada))
without_bg.save(fotoSaida)




