import json
import random
import urllib.request

# 512 / 4
n = 128

# json_data_format
data = {"basis": [], "qubits": []}

value = []

for _ in range(n * 4):
    basis = random.choice("+x")
    val = random.choice([0, 1])
    qubits = [1, 1j][val]
    if basis == "x":
        qubits /= 0.707 - 0.707j
    data["basis"] += [basis]
    data["qubits"] += [{"real": qubits.real, "imag": qubits.imag}]
    value += [val]

req = urllib.request.Request(
    "https://cryptoqkd.web.ctfcompetition.com/qkd/qubits",
    json.dumps(data).encode(),
    {"Content-Type": "application/json"})
res = urllib.request.urlopen(req).read()
res = json.loads(res)

share = ""
for i in range(n * 4):
    if len(share) >= n:
        break
    if data["basis"][i] == res["basis"][i]:
        share += str(value[i])

key = int(share, 2) ^ int(res["announcement"], 16)
key = "%x" % key
key = "0" * (int(n / 4) - len(key)) + key

print("key:", key)
