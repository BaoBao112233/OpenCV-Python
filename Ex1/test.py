import cv2

image = cv2.imread('F:\OpenCV\OpenCV-Python\Ex1\Books.png')

# print(image)
cv2.imshow("Books",image)
cv2.waitKey() # Dừng cửa sổ lại để xem kết quả
cv2.destroyAllWindows() # Đóng tất cả các cửa sổ lại

cam = cv2.VideoCapture(camera_id)
while (True):
    ret, frame = cam.read()
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

cam.release()
