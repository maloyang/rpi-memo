# install mediapipe for rpi4 @2021-07-13

## 用2021-03-04的image

# 系統軟體更新，這邊第二指令較久(15分)，若用05-07 OS可能較快
- 一開始需要做GUI版的initial的update, 少數時候還會出錯

```
sudo apt update
sudo apt upgrade

# 開始安裝
sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr23

sudo apt install ffmpeg python3-opencv

pip3 install mediapipe-rpi4


# 中文字處理
pip3 install pyzbar Pillow freetype-py
pip3 install pyzbar freetype-py

- for mssql
sudo apt-get install python3-pymssql
pip3 install sqlalchemy
```


## 用2021-05-07的image
- 用這個版本，不需要在GUI版中的update，安裝起來很方便

```
sudo apt update
sudo apt upgrade

# 開始安裝
sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr23

sudo apt install ffmpeg python3-opencv

pip3 install mediapipe-rpi4


# 中文字處理
pip3 install pyzbar Pillow freetype-py
pip3 install pyzbar freetype-py

- for mssql
sudo apt-get install python3-pymssql
pip3 install sqlalchemy
```


## for PC @2021-03-04 image
```
# cv package
pip install opencv-python
pip install mediapipe
pip install pyzbar
# 中文字處理
pip install freetype-py
# 安裝 pymssql
pip install pymssql
pip install sqlalchemy
```
