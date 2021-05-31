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
  - 3秒後拍照，輸出格式為640x480的png檔 `raspistill -t 3000 -o test.png -e png -w 640 -h 480`
- 錄影3秒: `raspivid -o test.h264 -t 3000`
    - 以640x480解析度錄影10秒 `raspivid -t 10000 -w 640 -h 480 -o video.h264`
- 如果都可以再自己的home目錄下看到照片、影片，那表示基礎建設都ok囉


## 臉部辨識1: [ref](https://www.oursteam.com.tw/view-news.php?id=111)
- 先參考這邊安裝相依套件: [ref](https://gist.github.com/mrpjevans/9885e853b603ed046cbc5326b9942991)
- 安裝相依套件:
```
sudo apt install build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-base-dev \
    libavcodec-dev \
    libavformat-dev \
    libboost-all-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    python3-pip \
    zip
    python3-picamera
```
- 更新picamera --> 我做了，但好像沒必要
- `sudo pip3 install --upgrade picamera`
- 把swap加大: `sudo nano /etc/dphys-swapfile`
- 找到 `CONF_SWAPSIZE` 把100改為1024
- 重啟swap設定，讓他生效 `sudo /etc/init.d/dphys-swapfile restart`
- Build and install dlib (聽說這步驟再rpi4要30分鐘，rpi3就....)
```
git clone -b 'v19.6' --single-branch https://github.com/davisking/dlib.git
cd ./dlib
sudo python3 setup.py install --compiler-flags "-mfpu=neon"
```
- 安裝到這邊，我們就可以開始安裝我們最需要的模組了: `sudo pip3 install face_recognition`

### 來跑我們的程式囉!
- 下載程式 `git clone --single-branch https://github.com/ageitgey/face_recognition.git`
- 進到example資料夾: `cd face_recognition/example`
- 執行程式: `python3 facerec_on_raspberry_pi.py`
- 這樣就可以採用基於一張照片的人臉辨識了!

### real-time face recognition: `facerec_from_webcam_faster.py` (faster這一個會把以1/4的大小處理，速度才夠快，不然rasp4也很難跟上)


## 另一個重點是~~ 這個project可以在mac, linux上跑 --> 晚點再來試試看

----
## 另外，補充
- [ref](https://www.slideshare.net/raspberrypi-tw/raspberry-pi-camera-and-opencv-day2): sosorry 的picamera & cv 介紹
- 
