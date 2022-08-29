import cv2 

cam = cv2.VideoCapture("F:\OpenCV\OpenCV-Python\Ex2-Camera\sample.avi")
while True:
    ret, frame = cam.read()
    cv2.imshow("Cam", frame)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()