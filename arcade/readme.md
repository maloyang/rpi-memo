# qrcode: 產生＆讀取

## 測試csi camera
- 取一張照片：`raspistill -o image.jpg`
- 錄一段影片：`raspivid -o viedeo.h264`
- 用程式測試
  - sudo apt install python-picamera
  - 新增 first_cam.py
```
import picamera

with picamera.PiCamera() as camera:
    camera.start_preview()
    camera.capture('./py-image.jpg')
    camera.stop_preview()
```
  - `python3 first_cam.py`


----
## qr-code 01

- [這篇有提到產生qrcode，並且使用cv2偵測qrcode，效果也不錯](https://www.hackster.io/gatoninja236/scan-qr-codes-in-real-time-with-raspberry-pi-a5268b)

- pip3 install qrcode
- 用qrcode package產生
```
import qrcode
code = qrcode.make('Hello world!')
code.save('qr)
```

- 用cv2抓camera上的qrcode
```
import cv2

# set up camera object
cap = cv2.VideoCapture(0)

# QR code detection object
detector = cv2.QRCodeDetector()

while True:
    # get the image
    _, img = cap.read()
    # get bounding box coords and data
    data, bbox, _ = detector.detectAndDecode(img)
    
    # if there is a bounding box, draw one, along with the data
    if(bbox is not None):
        for i in range(len(bbox)):
            cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255,
                     0, 255), thickness=2)
        cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)
        if data:
            print("data found: ", data)
    # display the image preview
    cv2.imshow("code detector", img)
    if(cv2.waitKey(1) == ord("q")):
        break
# free camera object and exit
cap.release()
cv2.destroyAllWindows()
```


## 產生：用qrencode

- ref: https://atceiling.blogspot.com/2017/03/raspberry-pi-zbar.html
- `sudo apt-get install zbar-tools qrencode`
- 也可以用s參數產生更大的qrcode，如： `qrencode -o qr-url.png -s 6 'https://github.com/maloyang/macbook_memo/blob/main/README.md'`
- 其中預設值是 -s 3

