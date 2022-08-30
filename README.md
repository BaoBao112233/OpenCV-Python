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

Hàm lưu ảnh: 
cv2.imwrite("đặt tên file", biến chứa file)

Hệ màu trong Open CV (BGR)

Hàm Conver hệ màu của ảnh:
cv2.cvtColor(image, cv2.BGR)

Hàm resize ảnh:
cv2. resize(biến chứa ảnh, dsize = (n,m)) 
resize ảnh về kích thước n.m

Xoay ảnh:
Download imutils: pip install imutils

imutils.rotate(biến chứa ảnh, qóc quay(radian))

Hàm threshold:
cv2.threshold(biến ảnh, b - ngưỡng, a - quy ước, Chế độ )

Nếu x(màu của điểm ảnh) > b thì return x = a
Nếu x <= b thì return x = 0