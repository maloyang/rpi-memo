# jetson initial setup
----

# VNC server
- ref: https://developer.nvidia.com/embedded/learn/tutorials/vnc-setup
- command as below, change 'thepassword' to setup your password:

```
mkdir -p ~/.config/autostart
cp /usr/share/applications/vino-server.desktop ~/.config/autostart/.

gsettings set org.gnome.Vino prompt-enabled false
gsettings set org.gnome.Vino require-encryption false

gsettings set org.gnome.Vino authentication-methods "['vnc']"
gsettings set org.gnome.Vino vnc-password $(echo -n 'thepassword'|base64)

sudo reboot
```

----

