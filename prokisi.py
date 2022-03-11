# -*- coding:utf-8 -*-
from PIL import Image, ImageChops
import os
import shutil
import cv2
import numpy as np

dir_path_before = r"C:\purokisi\pic_folder\before"
dir_list = os.listdir(dir_path_before)
for i in range(len(dir_list)):

    full_path = os.path.join(dir_path_before, dir_list[i])

    if os.path.isfile(full_path):  # ディレクトリORファイルを確認、ファイルのみ処理

        before_pic = "before_name_{0}{1}".format(i,os.path.splitext(dir_list[i])[1])   # 拡張子は変更しない
        os.rename(full_path, os.path.join(dir_path_before, before_pic))

# print("before_len")
# print(int(len(dir_list)))
# shutil.rmtree(r"C:\Users\81702\OneDrive\画像\PC壁紙\バトスピ_プロキシ\before")
# os.mkdir(r"C:\Users\81702\OneDrive\画像\PC壁紙\バトスピ_プロキシ\before")

pic_list = []
for i in range(len(dir_list)):
    img = Image.open(r"C:\purokisi\pic_folder\before\before_name_" + str(i) + ".jpg")

    # 2値化画像の生成
    bw_img = img.convert(mode='1', dither=None)

    # 白黒反転
    bw_inv_img = ImageChops.invert(bw_img)

    # クロップ範囲の計算とクロップの実行
    crop_range = bw_inv_img.convert('RGB').getbbox()
    crop_img = img.crop(crop_range)

    crop_img.save(r"C:\purokisi\pic_folder\after\after_name" + str(i) + ".jpg")
    im1 = cv2.imread(r"C:\purokisi\pic_folder\after\after_name" + str(i) + ".jpg")
    im_v_np = np.tile(im1, (3, 1, 1))
    cv2.imwrite(r"C:\purokisi\pic_folder\after_1\after_name" + str(i) + ".jpg", im_v_np)

    img = r"C:\purokisi\pic_folder\after_1\after_name" + str(i) + ".jpg"
    pic_list.append(img)
print(pic_list)


# 画像複製して付け足す
# wordに挿入
#