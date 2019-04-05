import glob
from PIL import Image
import cv2 as cv
import numpy as np
import scipy.io as sc
import os

orig_img_list = []
data_len = 0
# dataDir = "/Users/sachin007/Desktop/BTP_data/SachinGT/NYU_Database/M_mat_files/"
# lineThickness = 5


for img in glob.glob("/Users/sachin007/Desktop/BTP_data/test_data/*.png"):
# for img in glob.glob("/Users/sachin007/Desktop/data_aug/*.jpg"):
    n= cv.imread(img)
    orig_img_list.append(n)
    data_len = data_len + 1



# import pdb;pdb.set_trace()
k = 0;
for i in range(data_len):
	print(i)
	orig_img = orig_img_list[i]
	aug_orig_img = np.rot90(orig_img,1)

	filename = "/Users/sachin007/Desktop/BTP_data/test_data/rot/testdr%i*.jpg"%i
	# filename = "/Users/sachin007/Desktop/data_aug/out/train_aug_%i.jpg"%k
	cv.imwrite(filename,aug_orig_img)


