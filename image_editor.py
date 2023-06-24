from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./passport_photo"
path_edit = "./"

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert()

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f".{path_edit}/{clean_name}_edited.jpg")