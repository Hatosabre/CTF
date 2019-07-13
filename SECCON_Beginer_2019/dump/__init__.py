import gzip

with open("dump.txt") as dump:
    data = dump.read()

data_list = data.split()

bin_data = bytearray()

for oct_d in data_list:
    if len(oct_d) == 4:
        continue
    bin_data.append(int(oct_d, 8))


gzip_data = gzip.decompress(bin_data)

with open("flag", mode="wb") as w:
    w.write(gzip_data)



