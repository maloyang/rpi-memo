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

## install VSCode
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

