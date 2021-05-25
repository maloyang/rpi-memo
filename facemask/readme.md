# face mask detect

ref1: https://www.tomshardware.com/how-to/raspberry-pi-face-mask-detector

- install tensorflow (120mb 較久）
`sudo pip3 install https://github.com/lhelontra/tensorflow-on-arm/releases/download/v2.1.0/tensorflow-2.1.0-cp37-none-linux_armv7l.whl`
  - 後來一直安裝不上去（99%就會失敗），於是改用 `sudo pip3 install tensorflow` (只是這個source下載超慢，約79.6mb）
- install imutils
`sudo pip3 install imutils`

## 快速通關捷徑 (從現有的git project下載使用，不做training)

- `git clone https://github.com/carolinedunn/face_mask_detection`
- 使用已經建好的model
- `cd face_mask_detection`
- 這邊因為camera類型，而分兩個執行程式（原作很體貼）
- 用外掛的webcam: `python3 detect_mask_webcam.py`
- 用內建的pi camera: `python3 detect_mask_picam.py`
