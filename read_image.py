import cv2
img=cv2.imread("butterfly.jpg")
cv2.imshow("Display",img)
print(img)
cv2.waitKey(0)
gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("Grayscale",gray_img)
cv2.waitKey(0)
print(gray_img)
