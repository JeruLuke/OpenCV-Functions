# https://programmer.help/blogs/special-effects-of-oil-painting-based-on-opencv-using-python.html
# https://docs.opencv.org/4.5.2/dd/d8c/tutorial_xphoto_oil_painting_effect.html

# book reference: https://docs.opencv.org/4.5.2/d0/de3/citelist.html#CITEREF_Holzmann1988

import cv2
import os
output_path = r'C:\Users\selwyn77\Desktop\New folder (2)\My Learnings\OpenCV\Functions\Images'

img = cv2.imread('scene1.jpg')
#dst = cv2.xphoto.oilPainting(img, 5, i)

#---- variations in kernel size
for i in range(1, 30, 4):
  dst = cv2.xphoto.oilPainting(img, i, 1)
  #cv2.imshow('output', dst)
  #cv2.imwrite(os.path.join(output_path, 'oi_paint_kernel_{}.jpg'.format(i)), dst)
  cv2.imwrite('oil_paint_{}.jpg'.format(i), dst)
  #cv2.waitKey(0)
#----

#---- variations in dynamic ratio
#for i in range(1, 60, 2):
#  dst = cv2.xphoto.oilPainting(img, 5, i)
#  cv2.imshow('output', dst)
#  cv2.waitKey()
#----

#cv2.imshow('output', dst)
#cv2.waitKey()
cv2.destroyAllWindows()