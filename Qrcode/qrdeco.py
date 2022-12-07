from pyzbar.pyzbar import decode
from PIL import Image

img=Image.open("E:/Practice/python/projects/Qrcode/download.png")

result=decode(img)
satu=result[0][0].decode("UTF-8").split(";")
print(satu)

