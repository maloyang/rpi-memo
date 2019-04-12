# 開機後執行程式的方式

參考：http://felix-lin.com/linux/debianubuntu-%E6%96%B0%E5%A2%9E%E9%96%8B%E6%A9%9F%E8%87%AA%E5%8B%95%E5%9F%B7%E8%A1%8C%E7%A8%8B%E5%BC%8F/

## 新增`/etc/init.d/run_fw`檔

```
#! /bin/sh
# /etc/init.d/run_fw
#
 
# Some things that run always
touch /var/lock/run_fw
 
# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting firmware"
    /home/pi/autorun.sh
    ;;
  stop)
    echo "Stopping firmware"
    echo "you can kill your firmware here"
    ;;
  *)
    echo "Usage: /etc/init.d/run_fw {start|stop}"
    exit 1
    ;;
esac
 
exit 0
```

### 改為可執行:

`chmod 755 /etc/init.d/run_fw.sh`

### 加入開機執行

`update-rc.d run_fw.sh defaults`


### 若要取消

`update-rc.d -f  remove`
