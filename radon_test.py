import glob
from PIL import Image
import cv2 as cv
import numpy as np
import scipy.io as sc
from scipy import misc
import os

import scipy
from scipy import misc
from skimage.transform import radon, iradon,iradon_sart, rotate

from skimage.draw import line_aa
from PIL import Image
from PIL import ImageDraw
import matplotlib.pyplot as pltr

import sewar
from matplotlib import pyplot as plt
# %matplotlib inline


orig_img_list = []
data_len = 0

# filename = "/Users/sachin007/Documents/Sym_radon/images/lamp4.png"
filename = "/Users/sachin007/Desktop/BTP_data/ax1.png"
filename2 = "/Users/sachin007/Desktop/BTP_data/ax5.png"
img = cv.imread(filename,0)
img = cv.resize(img,(480,480))

# # rows,cols = img.shape
# # w2 = int(cols/2)
# # orig_img = img[:,:w2]
# # gt_img = img[:,w2:]

theta1 = np.linspace(0., 180., 180, endpoint=False)
sinogram1 = radon(img, theta=theta1, circle=True)
sinogram1 = sinogram1.astype(np.float64)
# import pdb;pdb.set_trace()
sinogram1 = sinogram1 / np.max(sinogram1) * 255

cv.imwrite('messigray4.png',sinogram1)

# w_s = cv.imread(filename2,0)
# import pdb;pdb.set_trace()

# w_s = w_s.astype(np.float64)
# print(w_s.dtype)

# # plt.imshow(w_s, cmap='gray')
# # plt.show()
# ri = iradon_sart(w_s, theta=theta1)

# thresh = np.max(ri)/2
# idx = ri > thresh
# ri[idx] = 1

# plt.imshow(ri, cmap='gray')
# plt.show()
# cv.imwrite('rec.png',sinogram1)

# reconstruction_sart = iradon_sart(gt_img, theta=theta1)
# plt.imshow(reconstruction_sart, cmap='gray')
# cv.imshow('ff',img)
# cv.waitKey(0)

# for img in glob.glob("/Users/sachin007/Desktop/BTP_data/SachinGT/combined/train_data_aug/*.jpg"):
#     n= cv.imread(img,0)
#     orig_img_list.append(n)
#     data_len = data_len + 1


# print(data_len)


# for i in range(data_len):

# 	print(i)
# 	img = orig_img_list[i]
# 	rows,cols = img.shape
# 	w2 = int(cols/2)
# 	orig_img = img[:,:w2]
# 	gt_img = img[:,w2:]

# 	theta1 = np.linspace(0., 180., 180, endpoint=False)
# 	# print(theta1)
# 	sinogram1 = radon(gt_img, theta=theta1, circle=True)
# 	sinogram1 = sinogram1.astype(np.float64)

# 	# import pdb;pdb.set_trace()
# 	aug_img = np.concatenate((orig_img, sinogram1), axis=1)

# 	filename = "/Users/sachin007/Desktop/BTP_data/SachinGT/combined/train_data_aug_radon/trainImg_%i*.jpg"%i
# 	cv.imwrite(filename,aug_img)
