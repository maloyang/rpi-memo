# About CV

這邊先記錄我用rpi4的學習雜技

## 初始化
- 格式化: WinSetup-1-0-beta7
- win32DiskImager 寫`2021-03-04-raspios-buster-armhf.img`入SD卡
- 接上micro HDMI到電視，接type c的5V3A電源
- 設定 wifi

## 基本安裝
- sudo apt update
- 先在桌面(或用raspi-config)設定 ssh, camera, vnc 開啟
- 因為新的rpi4 image預設沒接hdmi時，沒有video output, 所以要先在桌面(或用raspi-config)設定 default display -> 我設定 1024x768
- 這樣再用vnc client(我用vnc viewer)就可以看到螢幕了

## 測試camera
- 拍張照片: `raspistill -v -o test.jpg`
- 錄影3秒: `raspivid -o test.h264 -t 3000`
- 如果都可以再自己的home目錄下看到照片、影片，那表示基礎建設都ok囉

