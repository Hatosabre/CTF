import base64
import zlib

encrypted_f = open("encrypted.txt")
encrypted = encrypted_f.read()
encrypted_f.close()

encrypted = base64.urlsafe_b64decode(encrypted)

flag_base64 = None
while True:
    try:
        flag_base64 = zlib.decompress(encrypted)
        encrypted = base64.urlsafe_b64decode(flag_base64)
    except Exception:
        print(flag_base64)
        break



