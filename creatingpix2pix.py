import cv2 as cv 
import glob
import numpy as np 
from PIL import Image

# for img in glob.glob("/Users/sachin007/Desktop/BTP_data/SachinGT/gt/*.jpg"):
#     n= cv2.imread(img)
#     print(i)
#     i=i+1

for img in glob.glob("/Users/sachin007/Desktop/BTP_data/SachinGT/*.jpg"):

	# print(img)
	img1 = cv.imread(img,1)
	# import pdb;pdb.set_trace()
	img2 = cv.imread('/Users/sachin007/Desktop/BTP_data/SachinGT/images/COCO_test2014_000000008754.jpg',1)

	# result = (array < 25) * array


	img3 = img2 - img1
	img3 = cv.medianBlur(img3,5)
	# img3 = cv.GaussianBlur(img3,(5,5),0)

	img3R = (img3[:,:,0] > 25) 
	img3G = (img3[:,:,1] > 25) 
	img3B = (img3[:,:,2] > 25)
	img3R = img3R.astype(int) 


	imgbin = img3R & img3G & img3B
	np.int8(imgbin)

	img3[:,:,0] = imgbin * 255
	img3[:,:,1] = imgbin * 255
	img3[:,:,2] = imgbin * 255


	img3 = Image.fromarray(img3)
	import pdb;pdb.set_trace()
	# median = cv.medianBlur(img3[:,:,0],5)

	# img3 = img3.convert('RGB')
	# img3.show()

