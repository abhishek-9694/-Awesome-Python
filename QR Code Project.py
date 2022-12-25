# import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode

# String which represents the QR code .
site = "https://www.youtube.com/watch?v=usKaateSP7o"

# Generating QR Code
url_QR = pyqrcode.create(site)


# Create & save the svg file 
#url_QR.svg("great.svg",scale = 8)


# Create & save the svg file 
url_QR.png("great.png",scale = 6)
