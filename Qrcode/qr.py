import qrcode
from PIL import Image

data=input("Enter the  data you want to encode")

img=qrcode.make(data)

img.save("E:/Practice/python/projects/Qrcode/git.png")
img1=Image.open("E:/Practice/python/projects/Qrcode/git.png")
img1.show()