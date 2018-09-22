import scipy.io as sc
from PIL import Image
import numpy as np 
# i = 
mat = sc.loadmat('/Users/sachin007/Desktop/BTP_data/SachinGT/NYU_Database/M/I001.mat')
orig_img = Image.open('/Users/sachin007/Desktop/BTP_data/SachinGT/NYU_Database/M/I001.png')
orig_img = np.array(orig_img)

sym_data = mat['segments']
s = np.shape(sym_data)
numb_axis = s[1]		#number of symmetry axis 



for i in range(numb_axis):





sym_data = sym_data * 255

for i in range(3):
	orig_img[:,:,i] = orig_img[:,:,i] + sym_data

orig_img = Image.fromarray(orig_img)
orig_img = orig_img.convert('RGB')
orig_img.show()

sym_img = Image.fromarray(sym_data)
sym_img.show()