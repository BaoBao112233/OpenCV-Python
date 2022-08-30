import cv2 
import imutils
camera_id = "F:\OpenCV\OpenCV-Python\Ex2-Camera\sample.avi"
cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    cv2.imshow("Cam", frame)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
