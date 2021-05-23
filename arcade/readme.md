# qrcode: 產生＆讀取

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

