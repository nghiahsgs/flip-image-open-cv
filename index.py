import cv2
src = cv2.imread('dinh.jpg')
image = cv2.flip(src, 1)
cv2.imwrite('dinh2.jpg', image)