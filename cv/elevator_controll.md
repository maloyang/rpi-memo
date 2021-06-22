# 以手勢做電梯控制

## 安裝程式

- for hand detector
```
pip install opencv-python
pip install mediapipe
```

- for QRCode
```
pip install pyzbar
pip install Pillow
```

----

### 用HP i7筆電
- 15~25 fps, 反應即時，效果不錯

### 用x250, i3筆電
- 2~3 fps, 反應慢


----

## rpi4 + picam

### 安裝程式
- ref: https://pypi.org/project/mediapipe-rpi4/
- for repare package:

```
sudo apt install ffmpeg python3-opencv
sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr23

pip3 install mediapipe-rpi4
```

