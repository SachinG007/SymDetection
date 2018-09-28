import scipy.io as sc
from PIL import Image
import numpy as np 
import cv2 as cv 

lineThickness = 5
 
mat = sc.loadmat('/Users/sachin007/Desktop/BTP_data/SachinGT/NYU_Database/M/I001.mat')
orig_img = Image.open('/Users/sachin007/Desktop/BTP_data/SachinGT/NYU_Database/M/I001.png')
orig_img = np.array(orig_img)

sym_data = mat['segments']
s = np.shape(sym_data)
numb_axis = s[1]		#number of symmetry axis 

sym_img = np.zeros(np.shape(orig_img), np.uint8)


for i in range(numb_axis):

	x1 = sym_data[0][i][0][0]
	x1 = x1.astype(int)
	y1 = sym_data[0][i][0][1]
	y1 = y1.astype(int)
	x2 = sym_data[0][i][1][0]
	x2 = x2.astype(int)
	y2 = sym_data[0][i][1][1]
	y2 = y2.astype(int)

	cv.line(sym_img, (x1, y1), (x2, y2), (255,255,255), lineThickness)


out_img = np.concatenate((orig_img, sym_img), axis=1)
img = Image.fromarray(out_img)
img = img.convert('RGB')
img.show()