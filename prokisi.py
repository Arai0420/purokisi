# -*- coding:utf-8 -*-
from PIL import Image, ImageChops
import os
import shutil
import cv2
import numpy as np
import win32
import sys
import time
import glob

# フォルダ内の写真の名前を変える----------------------------------------------------------------------------------------------
dir_path_before = r"C:\purokisi\pic_folder\before"
dir_list = os.listdir(dir_path_before)
# print(len(dir_list))  # 画像の枚数
for i in range(len(dir_list)):

    full_path = os.path.join(dir_path_before, dir_list[i])

    if os.path.isfile(full_path):  # ディレクトリORファイルを確認、ファイルのみ処理

        before_pic = "before_name_{0}{1}".format(i,os.path.splitext(dir_list[i])[1])   # 拡張子は変更しない
        os.rename(full_path, os.path.join(dir_path_before, before_pic))

# フォルダ内の同じ写真を３つ結合し、保存----------------------------------------------------------------------------------------
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
    im_v_np = np.tile(im1, (3, 1, 1))  # 縦に3つ結合
    cv2.imwrite(r"C:\purokisi\pic_folder\after_1\after_name" + str(i) + ".jpg", im_v_np)

    img = r"C:\purokisi\pic_folder\after_1\after_name" + str(i) + ".jpg"
    pic_list.append(img)
# print(pic_list)  # リストに写真のpathを格納

#  フォルダ内の画像サイズを一括で統一
FromImgName = r"C:\purokisi\pic_folder\after_1"
ToImgName = r"C:\purokisi\pic_folder\resize"

#  imgフォルダ内の画像名をまとめて取得
files = os.listdir(FromImgName)

#  for文で画像サイズを一括変更
for file in files:
    img = Image.open(os.path.join(FromImgName, file))
    img_resize = img.resize((815, 3561))  # mgへ格納した画像を815×3561サイズ変更
    img_resize.save(os.path.join(ToImgName, file))  # resizeフォルダへ保存

#  画像を３つづつ横に結合----------------------------------------------------------------------------------------------------
# 画像の保存先となるリスト形式の変数
list_img = []
j = 0
for i in range(len(dir_list)):
    # 画像を読み込む
    img_1 = cv2.imread(r"C:\purokisi\pic_folder\resize\after_name" + str(j) + ".jpg")
    img_2 = cv2.imread(r"C:\purokisi\pic_folder\resize\after_name" + str(j + 1) + ".jpg")
    img_3 = cv2.imread(r"C:\purokisi\pic_folder\resize\after_name" + str(j + 2) + ".jpg")
    list_img.append(img_1)
    list_img.append(img_2)
    list_img.append(img_3)
    # 逆にしたい場合
    # list_img.reverse()

    if int(j + 2) == (len(dir_list)):
        print("終了")
        break

    # 画像を横方向に連結
    img_join = cv2.hconcat(list_img)
    # 結合した画像を保存
    cv2.imwrite(r"C:\purokisi\pic_folder\final\final_" + str(i) + ".jpg", img_join)
    list_img.clear()
    j = i + 3
    print("保存完了")

dir_path_final = r"C:\purokisi\pic_folder\final"
list = os.listdir(dir_path_final)

# 余白を追加し保存する------------------------------------------------------------------------------------------------------
def main():
    for i in range(len(list)):
        white = [255, 255, 255]
        img_files = glob.glob(r"C:\purokisi\pic_folder\final\final_" + str(i) + ".jpg")

        for f in img_files:
            img = cv2.imread(f)
            fname, fext = os.path.splitext(f)

            height, width, channels = img.shape

            # 画像の下に余白追加
            output = cv2.copyMakeBorder(img, 17, 521, 15, 450, cv2.BORDER_CONSTANT, value=white)
            cv2.imwrite(r"C:\purokisi\pic_folder\copy\flame" + str(i) + ".png", output)

if __name__ == "__main__":
    main()
    print("保存完了")
