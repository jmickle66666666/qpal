import sys
import math
from PIL import Image

def color_bytes_to_list(bytelist):
    output = []
    for i in range(256):
        index = i * 3
        col = ( int(bytelist[index]), int(bytelist[index+1]),int(bytelist[index+2]) )
        output.append(col)
    return output

def convert_palette_to_image(input_path, output_path):

    f = open(input_path, 'rb')
    color_bytes = f.read()
    f.close()

    colors = color_bytes_to_list(color_bytes)
    img = Image.new("RGB", (16,16), "black")
    for i in range(256):
        x = i % 16
        y = math.floor(i / 16)
        img.putpixel((x, y), colors[i])
    
    img.save(output_path, 'PNG')


def convert_image_to_palette(input_path, output_path):

    f = open(output_path, 'wb')

    img = Image.open(input_path)
    img = img.convert("RGB")
    for i in range(256):
        x = i % 16
        y = math.floor(i / 16)
        color = img.getpixel((x, y))
        f.write(color[0].to_bytes(1, byteorder="big"))
        f.write(color[1].to_bytes(1, byteorder="big"))
        f.write(color[2].to_bytes(1, byteorder="big"))

    f.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit()

    input_path = sys.argv[1]

    if input_path.endswith('.png'):
        convert_image_to_palette(input_path, 'palette.lmp')
    elif input_path.endswith('.lmp'):
        convert_palette_to_image(input_path, 'palette.png')


