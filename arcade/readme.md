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


## 產生

- [這篇有提到產生qrcode](https://www.hackster.io/gatoninja236/scan-qr-codes-in-real-time-with-raspberry-pi-a5268b)
- pip3 install qrcode
- 用qrcode package產生
```
import qrcode
code = qrcode.make('Hello world!')
code.save('qr)
```

## 產生：用qrencode

- ref: https://atceiling.blogspot.com/2017/03/raspberry-pi-zbar.html
- `sudo apt-get install zbar-tools qrencode`
- 也可以用s參數產生更大的qrcode，如： `qrencode -o qr-url.png -s 6 'https://github.com/maloyang/macbook_memo/blob/main/README.md'`
- 其中預設值是 -s 3

