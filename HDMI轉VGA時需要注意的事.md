## HDMI轉VGA時需要注意的事
- RPi3 B是可以的，但第一次開機可以，第二次開機常是有問題的(不懂??)，查到資料可以修改"boot" disk中的 config.txt檔
- 把 "#hdmi_force_hotplug=1" 這一行註解掉就可以了
- 實測確實可以，例有時解析度會變的很怪(很小)，可能是因為直接使用最易相容的640x480的原因吧!?
- RPi Zero W 的話就不行，有可能是因為HDMI沒有外接電源，因此推力不足以顯示，要買有外接電源的比較好(正在買「有源的HDMI轉VGA線」，試過再補上來)
- RPi Zero W目前有時在HDMI的電視上也不行(用raspbian)-->把```hdmi_safe=1```把開有幫助，但解析度變的比較差 -->後來發現我的miniHDMI轉HDMI轉接頭可能也怪怪的，要再買別家的來試試…
- 原設定如下：

```
# For more options and information see
# http://rpf.io/configtxt
# Some settings may impact device functionality. See link above for details

# uncomment if you get no picture on HDMI for a default "safe" mode
#hdmi_safe=1

# uncomment this if your display has a black border of unused pixels visible
# and your display can output without overscan
#disable_overscan=1

# uncomment the following to adjust overscan. Use positive numbers if console
# goes off screen, and negative if there is too much border
#overscan_left=16
#overscan_right=16
#overscan_top=16
#overscan_bottom=16

# uncomment to force a console size. By default it will be display's size minus
# overscan.
#framebuffer_width=1280
#framebuffer_height=720

# uncomment if hdmi display is not detected and composite is being output
#hdmi_force_hotplug=1

# uncomment to force a specific HDMI mode (this will force VGA)
#hdmi_group=1
#hdmi_mode=1

# uncomment to force a HDMI mode rather than DVI. This can make audio work in
# DMT (computer monitor) modes
#hdmi_drive=2

# uncomment to increase signal to HDMI, if you have interference, blanking, or
# no display
#config_hdmi_boost=4

# uncomment for composite PAL
#sdtv_mode=2

#uncomment to overclock the arm. 700 MHz is the default.
#arm_freq=800

# Uncomment some or all of these to enable the optional hardware interfaces
#dtparam=i2c_arm=on
#dtparam=i2s=on
#dtparam=spi=on

# Uncomment this to enable the lirc-rpi module
#dtoverlay=lirc-rpi

# Additional overlays and parameters are documented /boot/overlays/README

# Enable audio (loads snd_bcm2835)
dtparam=audio=on
```
