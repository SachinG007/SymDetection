import glob
from PIL import Image
import cv2 as cv
import numpy as np
import scipy.io as sc
import os

orig_img_list = []
sym_data_list = []
data_len = 45
# dataDir = "/Users/sachin007/Desktop/BTP_data/SachinGT/NYU_Database/M_mat_files/"
lineThickness = 5


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
	k = i

	img_filename = "/Users/sachin007/Desktop/pix2pix_train/sym_test30deg_2/images/testd%i-inputs.png"%k
	out_filename = "/Users/sachin007/Desktop/pix2pix_train/sym_test30deg_2/images/testd%i-outputs.png"%k
	
	orig_img = cv.imread(img_filename)
	orig_img = np.array(orig_img)

	out_img = cv.imread(out_filename,0)
	out_img = np.array(out_img)
	# import pdb;pdb.set_trace()
	print(i)
	for a in range(256):
		for b in range(256):
			if(out_img[a,b] > 200):
				orig_img[a,b,:] = (255,0,0)

	# final_out_img = np.add(out_img,orig_img)

	
	filename = "/Users/sachin007/Desktop/pix2pix_train/sym_test30deg_2/images/joined/testd%i-joined.png"%k
	cv.imwrite(filename,orig_img)
	# img.show()
