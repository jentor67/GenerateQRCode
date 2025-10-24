#!/usr/bin/python3

import qrcode

data = "33" #https://example.com"
img = qrcode.make(data)
img.save("my_qrPY.png")
