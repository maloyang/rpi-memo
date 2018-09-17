# Just My Raspberry Pi Memo.
- set up env.
- install miniconda
- install jupyter
- and some memo. to make rpi3B as my desktop computer....

## set up basic env.
- 設定語系, 字形: ：下 raspi-cofig 指令
- "4 Localisation Options" / "I1 Change Locale" 選
```
[*] en_US.UTF-8 UTF-8
[*] zh_TW.UTF-8 UTF-8
```
- "4 Localisation Options" / "I2 Change Timezone" / "Asia" / "Taipei"
- "4 Localisation Options" / "I3 Change Keyboard Layout" / "Generic 105-key (Intl) PC" / "English (US)" / "Both Alt keys" / "No compose key"

- 以上大概就設定好語系, 字形, 鍵盤
- 接著安裝注音輸入法: 
``` sudo apt-get install scim-chewing ```

## install miniconda
- download miniconda
```
conda2
wget https://repo.continuum.io/miniconda/Miniconda-latest-Linux-armv7l.sh
conda3
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh
```
- install miniconda
``` bash Miniconda3-latest-Linux-armv7l.sh ```

- 裝完後, 如果有設定 miniconda的python到.bashrc的話, 記得重登, 或重開就會生效

### 安裝 jupyter @miniconda失敗
- 原因是因為conda for armv7的prebuild套件好像沒有這一項
- 後來改用內建的python3的pip3安裝jupyter notebook就沒問題了!

### 安裝 flask
- ```conda install flask``` 過程有安裝：
```
    flask:        0.10.1-py34_1
    itsdangerous: 0.24-py34_0  
    jinja2:       2.8-py34_0   
    markupsafe:   0.23-py34_0  
    pip:          7.1.2-py34_0 
    setuptools:   18.1-py34_0  
    werkzeug:     0.10.4-py34_0
    wheel:        0.24.0-py34_0
```


## install VSCode
- before you run first command, you must do ```sudo apt-get update```, or you will fail when install GPG key
- install vscode (use pre-build package)
    - ref: https://www.raspberrypi.org/forums/viewtopic.php?t=191342
    - install GPG key
sudo wget -qO - https://packagecloud.io/headmelted/codebuilds/gpgkey | sudo apt-key add -;
    - add source
sudo nano /etc/apt/sources.list
    - add this line
deb https://packagecloud.io/headmelted/codebuilds/raspbian/ jessie main
    - update, and install (40M and install for 205MB)
sudo apt-get update
sudo apt-get install code-oss


## 使用webcam
- 參考這一篇[文章](https://www.raspberrypi.org/documentation/usage/webcams/)
- 在插入USB webcam後，在產生一個 ```/dev/video0``` 的設備檔
- 安裝 fswebcam ```sudo apt-get install fswebcam```
- 下指令 ```fswebcam image.jpg``` 就可以由webcam照一張像下來了
- 指令照片的解析度 ```fswebcam -r 640x480 image2.jpg```

## 若想要用電腦(win10)透過USB serial console和rpi0w通訊，來下指令控制rpi0w

- ref: http://www.tal.org/tutorials/raspberry-pi-zero-usb-serial-console

- 修改`BOOT/config.txt`檔，在結尾處加入`dtoverlay=dwc2`

- 修改`BOOT/cmdline.txt`檔，在結尾處加入`modules-load=dwc2,g_serial`，內容如下：

```
dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=PARTUUID=72d5f72a-02 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait modules-load=dwc2,g_serial
```


## 若一開始沒有鍵盤、滑鼠時，要怎麼設定WiFi連線?
- 把sd卡放到電腦裡，在"boot"的磁碟槽中新增一個 ""wpa_supplicant.conf""，內容如下：
- 上電開機後，系統會把檔案剪走，放入系統的```/etc/wpa_supplicant/wpa_supplicant.conf```中，並啟用之
- 只有ssid, psk好像就可以了，其它參數可能系統會自動判別吧(話說系統iwlist不就可以知道proto, key_mgmt, pairwise這些參數了，幹嘛要人輸入呢?)
```
country=TW
ctrl_interface=DIR=/var/run/wpa_supplicantGROUP=netdev
update_config=1
network={
    ssid="my-ap1"
    psk="0123456789"
    proto=RSN
    key_mgmt=WPA-PSK
    pairwise=CCMP
}

network={
    ssid="my-ap2"
    psk="9876543210"
}
```
### 若使用raspbian desktop設定網路，得到的設定檔內容如下：
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
        ssid="ICP DAS"
        psk="icpdas888"
        key_mgmt=WPA-PSK
}
```

## 設定好wifi後, 要如何ssh連上rpi? 又不知道IP...

- 參考[這篇](http://yehnan.blogspot.com/2015/12/raspberry-piip.html), 使用nmap去掃同網域的IP
- sudo apt-get install nmap
- nmap -sn 192.168.43.0/24
    - 這樣是用ping的方式去掃
- 是Windows與Mac OS X，可到[nmap.org](https://nmap.org/)下載nmap這支工具，也有圖形介面Zenmap
- 另外, 也可以用fping去掃: fping -a -q -g 192.168.1.1 192.168.1.255
- 掃到了, 可以這樣連:
    - ssh pi@192.168.43.103
- 如果不能連, 可能是sshd沒有開, 可以把rpi的sd取下, 在/boot槽中加入 "ssh" 這個檔案, 再重新開機 ssh 功能就會開啟了


### 剛裝完時空間狀況
```
pi@raspberrypi:~ $ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        15G  4.2G  9.6G  31% /
devtmpfs        460M     0  460M   0% /dev
tmpfs           464M     0  464M   0% /dev/shm
tmpfs           464M   13M  452M   3% /run
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           464M     0  464M   0% /sys/fs/cgroup
/dev/mmcblk0p1   42M   21M   21M  51% /boot
tmpfs            93M     0   93M   0% /run/user/1000
```

### 設定完環境, 裝完注音輸入法, vscode, miniconda3 後的空間狀況
```
pi@raspberrypi:~ $ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        15G  4.7G  9.1G  34% /
devtmpfs        460M     0  460M   0% /dev
tmpfs           464M   14M  451M   3% /dev/shm
tmpfs           464M   13M  452M   3% /run
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           464M     0  464M   0% /sys/fs/cgroup
/dev/mmcblk0p1   42M   21M   21M  51% /boot
tmpfs            93M     0   93M   0% /run/user/1000
```

### 裝完flask後的空間
```
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        15G  4.9G  8.9G  36% /
devtmpfs        460M     0  460M   0% /dev
tmpfs           464M   54M  411M  12% /dev/shm
tmpfs           464M   13M  452M   3% /run
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           464M     0  464M   0% /sys/fs/cgroup
/dev/mmcblk0p1   42M   21M   21M  51% /boot
tmpfs            93M     0   93M   0% /run/user/1000
```
### 裝完jupyter (matplotlib, scipy, 還有apt-get update) 之後的空間
```
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        15G  5.1G  8.7G  37% /
devtmpfs        460M     0  460M   0% /dev
tmpfs           464M   34M  431M   8% /dev/shm
tmpfs           464M   13M  452M   3% /run
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           464M     0  464M   0% /sys/fs/cgroup
/dev/mmcblk0p1   42M   21M   21M  51% /boot
tmpfs            93M     0   93M   0% /run/user/1000
```
