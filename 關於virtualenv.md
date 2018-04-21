## rpi中virtualenv做操作 memo

- 在rpi3中用raspbian, 其環境就有python2, python3, 操作時沒指定容易弄錯, 用virtualenv會比較確實
- 現在都改用python3了, 所以下指令 ```sudo pip3 install virtualenv``` 安裝
- 設置測試環境：
```
virtualenv flasktest
source ./bin/activate
pip freeze

pip freeze > requirements.txt
pip -r requiment.txt
deactive
```
過程：
```
pi@raspberrypi:~/work_env $ virtualenv flasktest
Using base prefix '/usr'
New python executable in /home/pi/work_env/flasktest/bin/python3
Also creating executable in /home/pi/work_env/flasktest/bin/python
Installing setuptools, pip, wheel...done.
pi@raspberrypi:~/work_env $ ls
flasktest
pi@raspberrypi:~/work_env $ cd flasktest/
pi@raspberrypi:~/work_env/flasktest $ source bin/activate
(flasktest) pi@raspberrypi:~/work_env/flasktest $ pip install flask
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting flask
  Using cached https://files.pythonhosted.org/packages/77/32/e3597cb19ffffe724ad4bf0beca4153419918e7fa4ba6a34b04ee4da3371/Flask-0.12.2-py2.py3-none-any.whl
Collecting Jinja2>=2.4 (from flask)
  Using cached https://files.pythonhosted.org/packages/7f/ff/ae64bacdfc95f27a016a7bed8e8686763ba4d277a78ca76f32659220a731/Jinja2-2.10-py2.py3-none-any.whl
Collecting Werkzeug>=0.7 (from flask)
  Using cached https://files.pythonhosted.org/packages/20/c4/12e3e56473e52375aa29c4764e70d1b8f3efa6682bef8d0aae04fe335243/Werkzeug-0.14.1-py2.py3-none-any.whl
Collecting click>=2.0 (from flask)
  Using cached https://files.pythonhosted.org/packages/34/c1/8806f99713ddb993c5366c362b2f908f18269f8d792aff1abfd700775a77/click-6.7-py2.py3-none-any.whl
Collecting itsdangerous>=0.21 (from flask)
  Downloading https://www.piwheels.org/simple/itsdangerous/itsdangerous-0.24-py3-none-any.whl
Collecting MarkupSafe>=0.23 (from Jinja2>=2.4->flask)
  Downloading https://www.piwheels.org/simple/markupsafe/MarkupSafe-1.0-cp35-cp35m-linux_armv7l.whl
Installing collected packages: MarkupSafe, Jinja2, Werkzeug, click, itsdangerous, flask
Successfully installed Jinja2-2.10 MarkupSafe-1.0 Werkzeug-0.14.1 click-6.7 flask-0.12.2 itsdangerous-0.24
(flasktest) pi@raspberrypi:~/work_env/flasktest $ pip freeze
click==6.7
Flask==0.12.2
itsdangerous==0.24
Jinja2==2.10
MarkupSafe==1.0
Werkzeug==0.14.1
(flasktest) pi@raspberrypi:~/work_env/flasktest $ pip freeze > requirements.txt

(flasktest) pi@raspberrypi:~/work_env/flasktest $ deactivate 
pi@raspberrypi:~/work_env/flasktest $ 

```
