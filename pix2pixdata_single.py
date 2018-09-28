import glob
from PIL import Image
import cv2 as cv
import numpy as np
import scipy.io as sc
import os

orig_img_list = []
sym_data_list = []
data_len = 99
# dataDir = "/Users/sachin007/Desktop/BTP_data/SachinGT/NYU_Database/M_mat_files/"
lineThickness = 5


# import pdb;pdb.set_trace()

# mat = sc.loadmat('/Users/sachin007/Desktop/BTP_data/SachinGT/single/label_refs.mat')
# sym_data = mat['lbl']

filename = '/Users/sachin007/Desktop/BTP_data/SachinGT/ref_s/label_refs.txt'
sym_data = np.loadtxt(filename, delimiter=',')


# for i in range(data_len):
for i in range(1):

	i =99;

	# if (i<9):
	# 	k = i+1
	# 	img_filename = "/Users/sachin007/Desktop/BTP_data/SachinGT/ref_s/refs_00%i.jpg"%k
	# else:
	# 	k = i+1
	# 	img_filename = "/Users/sachin007/Desktop/BTP_data/SachinGT/ref_s/refs_0%i.jpg"%k
	img_filename = "/Users/sachin007/Desktop/BTP_data/SachinGT/ref_s/refs_100.jpg"

	
	orig_img = cv.imread(img_filename)
	orig_img = np.array(orig_img)

	numb_axis = 1		#number of symmetry axis 

	sym_img = np.zeros(np.shape(orig_img), np.uint8)



	for j in range(numb_axis):

		x1 = sym_data[i][0]
		x1 = x1.astype(int)
		y1 = sym_data[i][1]
		y1 = y1.astype(int)
		x2 = sym_data[i][2]
		x2 = x2.astype(int)
		y2 = sym_data[i][3]
		y2 = y2.astype(int)

		cv.line(sym_img, (x1, y1), (x2, y2), (255,255,255), lineThickness)


	out_img = np.concatenate((orig_img, sym_img), axis=1)
	# out_img = Image.fromarray(out_img)
	# out_img = out_img.convert('RGB')
	# filename = "/Users/sachin007/Desktop/BTP_data/SachinGT/combined/combined_ref_s/img_refs_%i.jpg"%i
	filename = "/Users/sachin007/Desktop/img_refs_%i.jpg"%i
	cv.imwrite(filename,out_img)
	# import pdb;pdb.set_trace()
	print(i)
	# img.show()
