import cv2 as cv 
import numpy as np 
from PIL import Image

img1 = cv.imread('/Users/sachin007/Desktop/BTP_data/SachinGT/gt/COCO_test2014_000000059690.jpg',1)
# import pdb;pdb.set_trace()
img2 = cv.imread('/Users/sachin007/Desktop/BTP_data/SachinGT/images/COCO_test2014_000000059690.jpg',1)

# result = (array < 25) * array


img3 = img2 - img1
img3 = cv.medianBlur(img3,5)
img3R = (img3[:,:,0] > 25) 
img3G = (img3[:,:,1] > 25) 
img3B = (img3[:,:,2] > 25)
img3R = img3R.astype(int) 


imgbin = img3R & img3G & img3B
np.int8(imgbin)

# h = np.shape(imgbin)[0]
# w = np.shape(imgbin)[1]

# eqmask = np.zeros(np.shape(imgbin))
# for i in range(h):
# 	for j in range(w):
# 		# print(j)
# 		if(img1[i,j,0] == img1[i,j,1] == img1[i,j,2]):
# 			eqmask[i][j] = 1

# eqmask = eqmask.astype(int)

# imgbin = imgbin & eqmask



img3[:,:,0] = imgbin * 255
img3[:,:,1] = imgbin * 255
img3[:,:,2] = imgbin * 255


img3 = Image.fromarray(img3)
# median = cv.medianBlur(img3[:,:,0],5)

# img3 = img3.convert('RGB')
img3.show()

