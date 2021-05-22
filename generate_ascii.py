import sys
from PIL import Image
import json

#name scheme
#image000570.jpg  540 -> 570

def img_2_ascii(image_path):
    img = Image.open(image_path)

    # resize the image
    width, height = img.size
    aspect_ratio = height/width
    new_height = aspect_ratio * 70 * 0.55
    img = img.resize((70, int(new_height)))
    img = img.convert('L')
    pixels = img.getdata()
    new_pixels = []
    for pixel in pixels:
        if pixel==0:
            new_pixels.append("8")
        else:
            new_pixels.append(".")
    new_pixels = ''.join(new_pixels)
    ascii_image = []
    for index in range(0, len(new_pixels), 70):
        s = ""
        for i in range(index, index+70):
            s+=new_pixels[i]
        ascii_image.append(s)
    return "\n".join(ascii_image)

def run():
    d = {}
    for i in range(1, 2):
        d[i]=img_2_ascii(f"./frames/image{str(i).zfill(6)}.jpg")
        print(d[i])
    with open("output.json", "w") as fp:
        json.dump(d,fp) 

run()
