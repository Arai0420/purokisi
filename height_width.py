# -*- coding:utf-8 -*-
from PIL import Image

dir_path_before = r"C:\purokisi\pic_folder\before"
dir_list = os.listdir(dir_path_before)
# 入力画像の読み込み
for i in range(6):
    img = Image.open(r"C:\purokisi\pic_folder\resize\after_name" + str(i) + ".jpg")

    width, height = img.size

    print(i)

    # 画像の幅を表示
    print('width:', width)

    # 画像の高さを表示
    print('height:', height)
    print("\n")

    i = i+1