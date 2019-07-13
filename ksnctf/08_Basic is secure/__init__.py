import base64

code = "cTg6RkxBR181dXg3eksyTktTSDhmU0dB"

enc = base64.urlsafe_b64decode(code)

print(enc)