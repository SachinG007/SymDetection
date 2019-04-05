import glob
from PIL import Image
import cv2 as cv
import numpy as np
import scipy.io as sc
import os

# k = 14 #img numb

orig_img_list = []
data_len = 0
# sym_data_list = []
# data_len = 99
# # dataDir = "/Users/sachin007/Desktop/BTP_data/SachinGT/NYU_Database/M_mat_files/"
# lineThickness = 5


# import pdb;pdb.set_trace()

# mat = sc.loadmat('/Users/sachin007/Desktop/BTP_data/SachinGT/single/label_refs.mat')
# sym_data = mat['lbl']


for img in glob.glob("/Users/sachin007/Desktop/face.png"):
    n= cv.imread(img)
    n = cv.resize(n,(256,256))
    orig_img_list.append(n)
    data_len = data_len + 1
    print(data_len)


# for i in range(data_len):
# img_filename = "/Users/sachin007/Desktop/test_data/test%i.png"%k

for i in range(data_len):

	orig_img = orig_img_list[i]
	out_img = np.concatenate((orig_img,orig_img), axis=1)
	# out_img = Image.fromarray(out_img)
	# out_img = out_img.convert('RGB')
	# filename = "/Users/sachin007/Desktop/BTP_data/SachinGT/combined/combined_ref_s/img_refs_%i.jpg"%i
	k = i + 51
	filename = "/Users/sachin007/Desktop/testd%i.jpg"%k
	cv.imwrite(filename,out_img)
