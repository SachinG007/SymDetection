import cv2
import numpy as np
from PIL import Image
import pdb

from scipy import ndimage
import numpy as np
import math
import cv2   


def subimage(image, center, theta, width, height):

   shape = image.shape[:2]

   matrix = cv2.getRotationMatrix2D( center=center, angle=theta, scale=1 )
   image = cv2.warpAffine( src=image, M=matrix, dsize=shape )

   x = int( center[0] - width/2  )
   y = int( center[1] - height/2 )

   image = image[ y:y+height, x:x+width ]

   return image

hog = cv2.HOGDescriptor()
im = cv2.imread("/Users/sachin007/Desktop/pix2pix_train/sym_test/images/joined/testd22-joined.png")
row,col,chan = np.shape(im)
min_i = 1000;
max_i = 0;

j = 100
for i in range(50,140):
	if (np.all(im[i,j,:])==np.all((0,0,1))):
		print(i)
		if (i<min_i):
			min_i = i
		if(i>max_i):
			max_i = i

mid_i = int((min_i+max_i)/2)
print("mid",mid_i)

#take a 20 20 patch near the symmetry axis 

# patch1 = im[i-25:i+25,mid_i-50:mid_i,:]
# patch2 = im[i-25:i+25,mid_i:mid_i+50,:]
# print(np.shape(patch1))

# cv2.imshow('Image1',patch1)
# cv2.imshow('Image2',patch2)
# patch1 = Image.fromarray(patch1, 'RGB')
# patch2 = Image.fromarray(patch2, 'RGB')
# cv2.imwrite("patch1.png",patch1)
# cv2.imwrite("patch2.png",patch2)
# p1 = cv2.imread("patch1.png")
# p2 = cv2.imread("patch2.png")

# orb = cv2.ORB_create()
# # sift = cv2.SIFT()
# im_cropped = im[10:50,10:50,:]
# kp, des = orb.detectAndCompute(im_cropped,None)

#calculating the correlation 
# sigma1 = np.var(patch1)
# sigma2 = np.var(patch2)
# mean1 = np.mean(patch1)
# mean2 = np.mean(patch2)

# row,col,chan = np.shape(patch1)

# corr=0.0
# for m in range(row):
# 	for n in range(col):
# 		for k in range(3):
# 			corr = corr + (patch1[m,n,k]-mean1)*(patch2[m,col-n-1,k] - mean2)

# corr = corr/(3*sigma1*sigma2)
# print(corr)

# self_corr=0.0
# for m in range(row):
# 	for n in range(col):
# 		for k in range(3):
# 			self_corr = self_corr + (patch1[m,n,k]-mean1)*(patch1[m,n,k] - mean1)

# self_corr = self_corr/(3*sigma1*sigma1)
# print(self_corr)
# print("ratio",corr/self_corr)


# gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray,50,150,apertureSize = 3)

# lines = cv2.HoughLines(edges,1,np.pi/180,200)
# for rho,theta in lines[0]:
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a*rho
#     y0 = b*rho
#     x1 = int(x0 + 1000*(-b))
#     y1 = int(y0 + 1000*(a))
#     x2 = int(x0 - 1000*(-b))
#     y2 = int(y0 - 1000*(a))

#     cv2.line(im,(x1,y1),(x2,y2),(0,0,255),2)

# cv2.imwrite('houghlines.jpg',im)


image = subimage(im, center=( j,mid_i), theta=90, width=50, height=50)
cv2.imwrite('patch.jpg', image)


# pdb.set_trace()

# cv2.waitKey(0)
