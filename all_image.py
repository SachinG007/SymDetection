import glob
from PIL import Image
import cv2 as cv
import numpy as np
gt = []
orig = []
for img in glob.glob("/Users/sachin007/Desktop/BTP_data/SachinGT/gt/*.jpg"):
    n= cv.imread(img)
    gt.append(n)

for img in glob.glob("/Users/sachin007/Desktop/BTP_data/SachinGT/images/*.jpg"):
    n= cv.imread(img)
    orig.append(n)


for i in range(250):
	img1 = gt[i]
	img2 = orig[i]

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
	# img3.show()

	img4 = np.concatenate((img2, img3), axis=1)
	img = Image.fromarray(img4)
	# img.show()

	filename = "/Users/sachin007/Desktop/BTP_data/SachinGT/combined/img_%i.jpg"%i
	cv.imwrite(filename,img4)
	print(i)

	# import pdb;pdb.set_trace()


# a = gt[1]
# a = Image.fromarray(a)
# a.show()

# b = orig[1]
# b = Image.fromarray(b)
# b.show()

# import pdb;pdb.set_trace()