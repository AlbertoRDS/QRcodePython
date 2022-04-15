import qrcode

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=50,
                   border=1)

qr.add_data("https://www.instagram.com/_betoo_rocha_/")
qr.make(fit=True)

img = qr.make_image(fill_color='orange',back_color='black')
img.save("advanced.png")