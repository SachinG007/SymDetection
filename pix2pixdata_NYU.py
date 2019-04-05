import glob
from PIL import Image
import cv2 as cv
import numpy as np
import scipy.io as sc
import os

orig_img_list = []
sym_data_list = []
data_len = 176
# dataDir = "/Users/sachin007/Desktop/BTP_data/SachinGT/NYU_Database/M_mat_files/"
lineThickness = 3


# for img in glob.glob("/Users/sachin007/Desktop/BTP_data/SachinGT/NYU_Database/M/*.png"):
#     n= cv.imread(img)
#     orig_img_list.append(n)
#     data_len = data_len + 1

# for file in os.listdir( dataDir ) :    
#     data = sc.loadmat(dataDir+file)
#     sym_data = data['segments']
#     sym_data_list.append(sym_data)


# import pdb;pdb.set_trace()

for i in range(data_len):

	if (i<9):
		k = i+1
		img_filename = "/Users/sachin007/Desktop/BTP_data/SachinGT/NYU_Database/S/I00%i.png"%k
	elif (i<99):
		k = i+1
		img_filename = "/Users/sachin007/Desktop/BTP_data/SachinGT/NYU_Database/S/I0%i.png"%k

	else:
		k = i+1
		img_filename = "/Users/sachin007/Desktop/BTP_data/SachinGT/NYU_Database/S/I%i.png"%k

	
	orig_img = cv.imread(img_filename)
	orig_img = np.array(orig_img)

	if (i<9):
		k = i+1
		mat_filename = "/Users/sachin007/Desktop/BTP_data/SachinGT/NYU_Database/S/I00%i.mat"%k
	elif (i<99):
		k = i+1
		mat_filename = "/Users/sachin007/Desktop/BTP_data/SachinGT/NYU_Database/S/I0%i.mat"%k

	else:
		k = i+1
		mat_filename = "/Users/sachin007/Desktop/BTP_data/SachinGT/NYU_Database/S/I%i.mat"%k

	mat = sc.loadmat(mat_filename)
	sym_data = mat['segments']

	s = np.shape(sym_data)
	numb_axis = s[1]		#number of symmetry axis 

	sym_img = np.zeros(np.shape(orig_img), np.uint8)



	for j in range(numb_axis):

		x1 = sym_data[0][j][0][0]
		x1 = x1.astype(int)
		y1 = sym_data[0][j][0][1]
		y1 = y1.astype(int)
		x2 = sym_data[0][j][1][0]
		x2 = x2.astype(int)
		y2 = sym_data[0][j][1][1]
		y2 = y2.astype(int)

		cv.line(sym_img, (x1, y1), (x2, y2), (255,255,255), lineThickness)

	sym_img = cv.GaussianBlur(sym_img,(3,3),10)
	out_img = np.concatenate((orig_img, sym_img), axis=1)
	# out_img = Image.fromarray(out_img)
	# out_img = out_img.convert('RGB')
	filename = "/Users/sachin007/Desktop/BTP_data/SachinGT/combined/combined_NYU_S/img_NYU_%i.jpg"%i
	cv.imwrite(filename,out_img)
	print(i)
	# img.show()
