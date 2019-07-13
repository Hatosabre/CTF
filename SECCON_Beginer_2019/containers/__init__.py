import glob
from PIL import Image

# binwalk
# file = open("e35860e49ca3fa367e456207ebc9ff2f_containers")

files = glob.glob("extracted/*.png")


def connect(png1, png2):

    if png2 is None:
        dst = Image.new('RGB', (png1.width, png1.height))
        dst.paste(png1, (0, 0))
        return dst

    dst = Image.new('RGB', (png1.width + png2.width, png1.height))
    dst.paste(png1, (0, 0))
    dst.paste(png2, (png1.width, 0))
    return dst


result = None
for num in range(len(files)):
    png = Image.open("extracted/{}.png".format(len(files) - num))
    result = connect(png, result)

result.save("result/result.png")

