import cv2

#--- THINNING --
#img = cv2.imread('figures.jpg', 0)
img = cv2.imread('figures2.jpg', 0)
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
dst1 = cv2.ximgproc.thinning(thresh, thinningType = 0)   # cv2.ximgproc.THINNING_ZHANGSUEN = 0
dst2 = cv2.ximgproc.thinning(thresh, thinningType = 1)   # cv2.ximgproc.THINNING_GUOHALL = 1

cv2.imshow("INPUT", thresh)
cv2.imshow("THINNING_ZHANGSUEN", dst1)
#cv2.imwrite('THINNING_ZHANGSUEN.jpg', dst1)
cv2.imshow("THINNING_GUOHALL", dst2)
#cv2.imwrite('THINNING_GUOHALL.jpg', dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
