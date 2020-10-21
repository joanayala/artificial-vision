import cv2 #OpenCV

img1 = cv2.imread('images/bananas.jpg')
cv2.imshow(':::Image :::', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()