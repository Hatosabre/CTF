import base64
import uu

enc_file = open("encrypto.txt", mode="r")
enc = enc_file.read()
enc_file.close()
while True:
    try:
        enc = base64.urlsafe_b64decode(enc)
    except Exception as e:
        break

with open("result.txt", mode="w") as f:
    f.write(enc.decode("utf-8"))

result = uu.decode("result.txt", "output.txt")
print(result)