import qrcode
import qrcode.image.svg

factory = qrcode.image.svg.SvgImage
svg_img = qrcode.make('Hello word !',image_factory=factory)
svg_img.save("myqr.svg")