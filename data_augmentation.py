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


for img in glob.glob("/Users/sachin007/Desktop/pix2pix_train/pix2pix-tensorflow/train_data/*.jpg"):
    n= cv.imread(img)
    orig_img_list.append(n)
    data_len = data_len + 1



# import pdb;pdb.set_trace()

for i in range(data_len):

	img = orig_img_list[i]

	img = cv.resize(img,(256,512,3))
	# height,width,channel = np.shape(img)
	# # import pdb;pdb.set_trace()
	# w2 = int(width/2)
	# orig_img = img[:,:w2,:]
	# gt_img = img[:,w2:,:]
	filename = "/Users/sachin007/Desktop/pix2pix_train/pix2pix-tensorflow/train_data_sized/train_%i.jpg"%i
	cv.imwrite(filename,img)
	print(i)
	# import pdb;pdb.set_trace()
	# img.show()
