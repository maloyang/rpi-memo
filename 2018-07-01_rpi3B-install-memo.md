# my rpi3B reinstall memo.

## setup basic env for chiness

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
  - this step will be long time.... depending your network speed...
  <pre><source>
Downloading https://files.pythonhosted.org/packages/f4/24/2a3e3df732393fed8b3ebf2ec078f05546de641fe1b667ee316ec1dcf3b7/webencodings-0.5.1-py2.py3-none-any.whl
Installing collected packages: ipython-genutils, decorator, six, traitlets, tornado, python-dateutil, pyzmq, jupyter-core, jupyter-client, ptyprocess, pexpect, pickleshare, pygments, backcall, parso, jedi, wcwidth, prompt-toolkit, simplegeneric, ipython, ipykernel, MarkupSafe, jinja2, jsonschema, nbformat, terminado, Send2Trash, mistune, entrypoints, pandocfilters, testpath, webencodings, html5lib, bleach, nbconvert, notebook, widgetsnbextension, ipywidgets, qtconsole, jupyter-console, jupyter
Successfully installed MarkupSafe-1.0 Send2Trash-1.5.0 backcall-0.1.0 bleach-2.1.3 decorator-4.3.0 entrypoints-0.2.3 html5lib-1.0.1 ipykernel-4.8.2 ipython-6.4.0 ipython-genutils-0.2.0 ipywidgets-7.2.1 jedi-0.12.1 jinja2-2.10 jsonschema-2.6.0 jupyter-1.0.0 jupyter-client-5.2.3 jupyter-console-5.2.0 jupyter-core-4.4.0 mistune-0.8.3 nbconvert-5.3.1 nbformat-4.4.0 notebook-5.5.0 pandocfilters-1.4.2 parso-0.3.0 pexpect-4.6.0 pickleshare-0.7.4 prompt-toolkit-1.0.15 ptyprocess-0.6.0 pygments-2.2.0 python-dateutil-2.7.3 pyzmq-17.0.0 qtconsole-4.3.1 simplegeneric-0.8.1 six-1.11.0 terminado-0.8.1 testpath-0.3.1 tornado-5.0.2 traitlets-4.3.2 wcwidth-0.1.7 webencodings-0.5.1 widgetsnbextension-3.2.1
  </source></pre>

  - use this command `jupyter-notebook` to run up your jupyter notebook

- 
