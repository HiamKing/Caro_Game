import cv2

img = cv2.imread("Caro.png")
img = cv2.resize(img, (450, 450))

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
for contour in contours:
    cv2.drawContours(img, contour, -1, (0, 255, 0), 3)
print(contours)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()