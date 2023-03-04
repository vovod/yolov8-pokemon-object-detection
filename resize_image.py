from PIL import Image
import os
from tqdm import tqdm

in_file = "E:\\data\\pokemon_classify\\images\\test\\"
out_file = "E:\\data\\pokemon_classify\\resize_image\\test\\"

dict_file = os.listdir(in_file)

def main(dict_file, in_file, out_file):
    for file in tqdm(dict_file):
        img = Image.open(in_file + file)
        w,h = img.size
        ratio = w/h
        new_w = 640
        new_h = int(new_w/ratio) 
        new_img = img.resize((new_w,new_h), Image.ANTIALIAS)
        file = file[:-4] + '.jpg'
        new_img.save(out_file + file, quality = 100)

if __name__ == '__main__':
    main(dict_file, in_file, out_file)
