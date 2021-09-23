# https://docs.opencv.org/3.4.1/df/db9/namespacecv_1_1xphoto.html
# https://en.wikipedia.org/wiki/Color_balance

# To train WB model with dataset
# https://docs.opencv.org/4.5.2/dc/dcb/tutorial_xphoto_training_white_balance.html
# https://github.com/opencv/opencv_contrib/blob/master/modules/xphoto/tutorials/training_white_balance.markdown

import cv2
import numpy as np

img_src = cv2.imread('city.jpg', 1)
#img_src_lab = cv2.cvtColor(img_src, cv2.COLOR_BGR2Lab)

wb1 = cv2.xphoto.createSimpleWB() # createGrayworldWB()  # createSimpleWB(), createLearningBasedWB()
#wb.setSaturationThreshold(0.02)
image_wb1 = wb1.balanceWhite(img_src)

wb2 = cv2.xphoto.createGrayworldWB()
image_wb2 = wb2.balanceWhite(img_src)

wb3 = cv2.xphoto.createLearningBasedWB()
image_wb3 = wb3.balanceWhite(img_src)

cv2.imshow('Simple_White_balnced', image_wb1)
cv2.imshow('GrayWorld_White_balnced', image_wb2)
cv2.imshow('Learning_Based_White_balnced', image_wb3)

cv2.imwrite('city_Simple_WB.jpg', image_wb1)
cv2.imwrite('city_GrayWorld_WB.jpg', image_wb2)
cv2.imwrite('city_Learning_Based_WB.jpg', image_wb3)

cv2.imshow('Original', img_src)

print('PSNR for Simple_WB', cv2.PSNR(img_src, image_wb1))
print('PSNR for GrayWorld_WB', cv2.PSNR(img_src, image_wb2))
print('PSNR for earning_based_WB', cv2.PSNR(img_src, image_wb3))
#for i in range(

cv2.waitKey(0)
cv2.destroyAllWindows()
