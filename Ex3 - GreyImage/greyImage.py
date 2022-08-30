from email.mime import image
import cv2 
import imutils
camera_id = "F:\OpenCV\OpenCV-Python\Ex3 - GreyImage\Books.png"
# cam = cv2.VideoCapture(0)
# while True:
#     ret, frame = cam.read()
#     cv2.imshow("Cam", frame)
#     if cv2.waitKey(1) and 0xFF == ord('q'):
#         break

# cam.release()
# cv2.destroyAllWindows()

# Đọc ảnh
image = cv2.imread(camera_id)
cv2.imshow('Ảnh gốc', image)
cv2.waitKey()
grey_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Ảnh đen trắng', grey_image)
cv2.waitKey()
# grey_image = cv2.cvtColor(grey_image,cv2.COLOR_BGR2GRAY)

# Threshold
ret, threshold = cv2.threshold(grey_image,127,255,cv2.THRESH_BINARY)
cv2.imshow('Ảnh threshold', threshold)
cv2.waitKey()
cv2.destroyAllWindows()