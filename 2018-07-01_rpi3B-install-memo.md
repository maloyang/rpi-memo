# my rpi3B reinstall memo.

## setup basic env. for chiness

- sudo apt-get install scim-chewing
  - log-out after finishing your install
  - log-in again, you will have scim-chewing to input chiness
  
## setup python3 env. with jupyter notebook

- mkdir pyenv
- cd pyenv/
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
