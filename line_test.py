import numpy as np 
import cv2 as cv 
from PIL import Image

img = np.zeros((512,512,3), np.uint8)
lineThickness = 5
x1 = 2
y1 = 3
x2 = 30
y2 = 40
cv.line(img, (x1, y1), (x2, y2), (0,255,0), lineThickness)
print(np.max(img))
img = Image.fromarray(img)
img = img.convert('RGB')
img.show()