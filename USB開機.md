# 如何用USB隨身碟開機

- 會找這方法開機, 是因為有時SD關機後有時會有無法開機的問題
- [參考](http://blog.xuite.net/scl7333/XuiteBlog/513907912-Raspberry+Pi+3+%E4%BD%BF%E7%94%A8+USB+%E7%A1%AC%E7%A2%9F%E9%96%8B%E6%A9%9F)
- 在rpi3開機後 ```sudo nano /boot/config.txt``` 加入 ```program_usb_boot_mode=1``` 在最末行, 重開機
- 開完機後, ```vcgencmd otp_dump | grep 17:``` 查是否成功, 若回 ```17:3020000a``` 就代表成功了

- 接著下載 ```NOOBS``` 解壓到USB (format完的), 就可以用來開機了 ([這邊下載](https://www.raspberrypi.org/downloads/noobs/))
- 用USB開會停個10秒, 才會出現畫面, 是和SD最大的不同
