# OpenCV-Python
Open CV by python

Tham khảo các tài liệu: https://www.miai.vn/thu-vien-mi-ai/

Download OpenCV Python: pip install opencv-python

Hàm đọc ảnh: cv2.imread("đường dẫn file ảnh", chế độ đọc ảnh(nếu có))

Hàm hiển thị ảnh: imshow("Tên cửa sổ", ảnh muốn show)

cv2.waitKey() # Dừng cửa sổ lại để xem kết quả

cv2.destroyAllWindows() # Đóng tất cả các cửa sổ lại

Mở camera:
cam = cv2.VideoCapture(camera_id) 
camera_id = 0, 1, ...
Có thế thay camera_id thành đường dẫn để file video để đọc ảnh từ 

Đọc ảnh từ camera: 
while (True):
    ret, frame = cam.read()
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

Giải phóng camera:
cam.release()