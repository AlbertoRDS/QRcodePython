import qrcode

img = qrcode.make("https://www.instagram.com/_betoo_rocha_/")
img.save("qrcode.png")