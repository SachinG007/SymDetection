import glob
from PIL import Image
import cv2 as cv
import numpy as np
import scipy.io as sc
from scipy import misc
import os

orig_img_list = []
data_len = 0
# dataDir = "/Users/sachin007/Desktop/BTP_data/SachinGT/NYU_Database/M_mat_files/"
# lineThickness = 5


for img in glob.glob("/Users/sachin007/Desktop/BTP_data/SachinGT/combined/train_data/*.jpg"):
# for img in glob.glob("/Users/sachin007/Desktop/data_aug/*.jpg"):
    n= cv.imread(img)
    orig_img_list.append(n)
    data_len = data_len + 1


print(data_len)
# # import pdb;pdb.set_trace()
k = 3915
# for i in range(data_len):
# 	print(i)
# 	for j in range(8):

# 		img = orig_img_list[i]
# 		rows,cols,channel = img.shape
# 		# import pdb;pdb.set_trace()
# 		w2 = int(cols/2)
# 		orig_img = img[:,:w2,:]
# 		gt_img = img[:,w2:,:]

# 		if (j==0):

# 			aug_orig_img = np.fliplr(orig_img)
# 			aug_gt_img = np.fliplr(gt_img)
# 			aug_orig_img = cv.resize(aug_orig_img, dsize=(256, 256), interpolation=cv.INTER_CUBIC)
# 			aug_gt_img = cv.resize(aug_gt_img, dsize=(256, 256), interpolation=cv.INTER_CUBIC)
# 			aug_img = np.concatenate((aug_orig_img, aug_gt_img), axis=1)
# 			k = k + 1
# 			filename = "/Users/sachin007/Desktop/BTP_data/SachinGT/combined/train_data_aug/trainAug_%i*.jpg"%k
# 			cv.imwrite(filename,aug_img)

# 		aug_orig_img = misc.imrotate(orig_img, 45*(j+1)).astype('float64')
# 		aug_gt_img = misc.imrotate(gt_img, 45*(j+1)).astype('float64')
# 		# aug_orig_img = np.rot90(orig_img,j+1)
# 		# aug_gt_img = np.rot90(gt_img,j+1)	
# 		aug_orig_img = cv.resize(aug_orig_img, dsize=(256, 256), interpolation=cv.INTER_CUBIC)
# 		aug_gt_img = cv.resize(aug_gt_img, dsize=(256, 256), interpolation=cv.INTER_CUBIC)
# 		aug_img = np.concatenate((aug_orig_img, aug_gt_img), axis=1)

# 		k = k + 1
# 		filename = "/Users/sachin007/Desktop/BTP_data/SachinGT/combined/train_data_aug/trainAug_%i*.jpg"%k
# 		# filename = "/Users/sachin007/Desktop/data_aug/out/train_aug_%i.jpg"%k
# 		cv.imwrite(filename,aug_img)
# 		# print(i)
# 		# import pdb;pdb.set_trace()
# 		# img.show()

for i in range(data_len):
	print(i)

	for j in range(2):

		img = orig_img_list[i]
		rows,cols,channel = img.shape
		# import pdb;pdb.set_trace()
		w2 = int(cols/2)
		orig_img = img[:,:w2,:]
		gt_img = img[:,w2:,:]

		if(j==0):
			aug_orig_img = orig_img[50:50+156,50:50+156]
			aug_gt_img = gt_img[50:50+156,50:50+156]

		if(j==1):
			aug_orig_img = orig_img[25:25+206,25:25+206]
			aug_gt_img = gt_img[25:25+206,25:25+206]

		aug_orig_img = cv.resize(aug_orig_img, dsize=(256, 256), interpolation=cv.INTER_CUBIC)
		aug_gt_img = cv.resize(aug_gt_img, dsize=(256, 256), interpolation=cv.INTER_CUBIC)
		
		aug_img = np.concatenate((aug_orig_img, aug_gt_img), axis=1)
		k = k + 1
		filename = "/Users/sachin007/Desktop/BTP_data/SachinGT/combined/train_data_augc/trainAug_%i*.jpg"%k
		cv.imwrite(filename,aug_img)



