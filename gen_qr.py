"""
Regeneruje QR kod smerujuci na web Depo Loco.
Spustenie:  python3 gen_qr.py https://presna-adresa-webu.sk
Bez argumentu pouzije docasny placeholder - PRED NASADENIM NAOSTRO NAHRAD SKUTOCNOU ADRESOU.
"""
import sys, qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask

url = sys.argv[1] if len(sys.argv) > 1 else "https://depo-loco-web.vercel.app"

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=20, border=2)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    color_mask=SolidFillColorMask(front_color=(21, 18, 15), back_color=(255, 255, 255)),
)
img.save("img/qr.png")
print("QR ulozene pre:", url)
