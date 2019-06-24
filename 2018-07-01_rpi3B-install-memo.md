# my rpi3B reinstall memo.

## setup basic env. for chiness

- sudo apt-get install scim-chewing
  - log-out after finishing your install
  - log-in again, you will have scim-chewing to input chiness
  
## setup python3 env. with jupyter notebook

- mkdir pyenv
- cd pyenv/
- if no pip3 --> `sudo apt-get install python3-pip`
- sudo pip3 install virtualenv
- virtualenv my-jupyter-env
- cd my-jupyter-env/
- source bin/activate
- pip install jupyter
  - this step will be long time.... depending your network speed... and install packages as below:
  `
Downloading https://files.pythonhosted.org/packages/f4/24/2a3e3df732393fed8b3ebf2ec078f05546de641fe1b667ee316ec1dcf3b7/webencodings-0.5.1-py2.py3-none-any.whl
Installing collected packages: ipython-genutils, decorator, six, traitlets, tornado, python-dateutil, pyzmq, jupyter-core, jupyter-client, ptyprocess, pexpect, pickleshare, pygments, backcall, parso, jedi, wcwidth, prompt-toolkit, simplegeneric, ipython, ipykernel, MarkupSafe, jinja2, jsonschema, nbformat, terminado, Send2Trash, mistune, entrypoints, pandocfilters, testpath, webencodings, html5lib, bleach, nbconvert, notebook, widgetsnbextension, ipywidgets, qtconsole, jupyter-console, jupyter
Successfully installed MarkupSafe-1.0 Send2Trash-1.5.0 backcall-0.1.0 bleach-2.1.3 decorator-4.3.0 entrypoints-0.2.3 html5lib-1.0.1 ipykernel-4.8.2 ipython-6.4.0 ipython-genutils-0.2.0 ipywidgets-7.2.1 jedi-0.12.1 jinja2-2.10 jsonschema-2.6.0 jupyter-1.0.0 jupyter-client-5.2.3 jupyter-console-5.2.0 jupyter-core-4.4.0 mistune-0.8.3 nbconvert-5.3.1 nbformat-4.4.0 notebook-5.5.0 pandocfilters-1.4.2 parso-0.3.0 pexpect-4.6.0 pickleshare-0.7.4 prompt-toolkit-1.0.15 ptyprocess-0.6.0 pygments-2.2.0 python-dateutil-2.7.3 pyzmq-17.0.0 qtconsole-4.3.1 simplegeneric-0.8.1 six-1.11.0 terminado-0.8.1 testpath-0.3.1 tornado-5.0.2 traitlets-4.3.2 wcwidth-0.1.7 webencodings-0.5.1 widgetsnbextension-3.2.1
  `

  - use this command `jupyter-notebook` to run up your jupyter notebook

- install micropython kernel
  - mkdir micropython
  - cd micropython
  - git config --global user.name "Your Name"
  - git config --global user.email email@example.com
  - git clone git://github.com/goatchurchprime/jupyter_micropython_kernel
  - pip install -e jupyter_micropython_kernel
  - install message:
  `
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Obtaining file:///home/pi/pyenv/my-jupyter-env/micropython/jupyter_micropython_kernel
Collecting pyserial>=3.4 (from jupyter-micropython-kernel==0.1.3)
  Downloading https://files.pythonhosted.org/packages/0d/e4/2a744dd9e3be04a0c0907414e2a01a7c88bb3915cbe3c8cc06e209f59c30/pyserial-3.4-py2.py3-none-any.whl (193kB)
    100% |████████████████████████████████| 194kB 86kB/s 
Collecting websocket-client>=0.44 (from jupyter-micropython-kernel==0.1.3)
  Downloading https://files.pythonhosted.org/packages/8a/a1/72ef9aa26cfe1a75cee09fc1957e4723add9de098c15719416a1ee89386b/websocket_client-0.48.0-py2.py3-none-any.whl (198kB)
    100% |████████████████████████████████| 204kB 111kB/s 
Requirement already satisfied: six in /home/pi/pyenv/my-jupyter-env/lib/python3.5/site-packages (from websocket-client>=0.44->jupyter-micropython-kernel==0.1.3) (1.11.0)
Installing collected packages: pyserial, websocket-client, jupyter-micropython-kernel
  Running setup.py develop for jupyter-micropython-kernel
Successfully installed jupyter-micropython-kernel pyserial-3.4 websocket-client-0.48.0  
  `
  - python -m jupyter_micropython_kernel.install
  - install message:
  `
Installing IPython kernel spec of micropython
...into /home/pi/.local/share/jupyter/kernels/micropython
  `
  - jupyter kernelspec list
  `
Available kernels:
  micropython    /home/pi/.local/share/jupyter/kernels/micropython
  python3        /home/pi/pyenv/my-jupyter-env/share/jupyter/kernels/python3  
  `
  
  - run jupyter-notebook, you will find "MicropPython -USB" option at your "new" button

----

## jupyter notebook remote

- generate config first: `jupyter notebook --generate-config`
- use `jupyter notebook password` to config your password
- run `jupyter notebook --no-browser --ip="*"` , you will access notebook local and remotely

----

## install pandas

active in my virtualenv for jupyter first

- use `pip --no-cache-dir install pandas` to install, get it!

```
Installing collected packages: pytz, numpy, pandas
Successfully installed numpy-1.15.1 pandas-0.23.4 pytz-2018.5
```

----

## install anydesk for remote operation

- download: https://anydesk.org/en/downloads/raspberry-pi
- install command: `sudo dpkg -i anydesk_2.9.4-1_armhf.deb`


----

## export your requirements.txt file for next rpi3 project
- `pip freeze > requirements.txt`
- for next project, install all packages one time: `pip install -r path/to/requirements.txt`

## auto-run your program after desktop load
ref: https://www.raspberrypi-spy.co.uk/2014/05/how-to-autostart-apps-in-rasbian-lxde-desktop/

- edit `~/.config/lxsession/LXDE/autostart` , to add my autorun.sh script `/home/pi/autorun.sh`
- other NG for me
  - `sudo nano /etc/xdg/lxsession/LXDE-pi/autostart` to add my autorun.sh
  - ref. this one: https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/
    - `sudo nano /etc/rc.local` not work
    - `sudo nano /home/pi/.bashrc` not good for me, it will run program after i open a terminal
    - use init.d `sudo update-rc.d sample.py defaults` --> usually it will be ok in my other linux platform, but fail in pi.. I don't know what's happend.
    
## open chrome after boot (for ubuntu desktop version)
- use command `google-chrome "your-url" --start-maximized`
- add file `my_chrome.desktop` in `~/.config/autostart/`, with content below:
```
[Desktop Entry]
Comment=Autostart chrome with my url
Exec=google-chrome "http://your-url" --start-maximized
Name=chrome-start
OnlyShowIn=LXQt
Type=Application
Version=1.0
```

----
## for some hardware component
### hardware config
- Buzzer
- RS-485
- RTC

#### Buzzer
- `sudo apt install python3-gpiozero`
- `nano ~/buzzer2.py`, code as :
```
from gpiozero import Buzzer
import time

print('start')
buzzer = Buzzer(4)

print('ON')
buzzer.on()
time.sleep(0.1)
print('OFF')
buzzer.off()
```

- `nano ~/buzzer-off.sh`
```
#!/bin/bash

python /home/pi/buzzer2.py
```

- `sudo nano /etc/rc.local` , add as below before `exit 0` --> let it autostart @ boot
```
# init. and OFF buzzer
/home/pi/buzzer-off.sh &
```

### RS-485 --> /dev/ttyS0
- `sudo nano /boot/config.txt`, append a line at end:
```
enable_uart=1
```
- after reboot, system will has `dev/ttyS0`

- 因為boot command中預設serial0 (也就是/dev/ttyS0)為 console，所以要 `sudo nano /boot/cmdline.txt`，把console設定到別處，如下 console=tty1
```
dwc_otg.lpm_enable=0 console=tty1 root=PARTUUID=f4e31847-02 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles
```

- 設定好後，重新開機，可以用以下的程式進行測試
```
import serial

# function to check serial data

def check_serial_data(mbComPort='/dev/ttyUSB0'):
    port = serial.Serial(mbComPort, 9600, timeout=1)
    with port as s:
        data = s.read(1024)
        print(len(data), '> ', data)

        print('write:')
        s.write('abcd\n')

    return len(data)
    


while True:
    check_serial_data()
```

### RTC, 
- use `sudo raspi-config` to enable i2c bus
enable "5 Localisation Options" / "p5 I2C"

- `nano rtc-set.sh`
```
sudo modprobe i2c-bcm2708

echo ds3231 0x68 | sudo tee /sys/class/i2c-adapter/i2c-1/new_device
sudo hwclock

# system time --> RTC
sudo hwclock -w
sudo hwclock

# when boot, RTC-->system time
#sudo update-rc.d ntp disable
#sudo update-rc.d fake-hwclock disable
```

- add two line into `/etc/rc.local` before `exit 0`
```
echo ds3231 0x68 > /sys/class/i2c-adapter/i2c-1/new_device
sudo hwclock -s
```
