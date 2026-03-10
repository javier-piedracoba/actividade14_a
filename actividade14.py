import qrcode

url = input("Introduce una URL: ")

img = qrcode.make(url)

img.save("actividade14.png")
