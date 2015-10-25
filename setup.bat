@echo off

echo "This needs chrome to work"
echo "Please install this EXACTLY as default"
start chrome.exe https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi
echo "Please press any key when you are done"
pause

setx PY_HOME C:\Python27
setx PYTHONPATH %PY_HOME%\Lib;%PY_HOME%\DLLs;%PY_HOME%\Lib\lib-tk;C:\another-library
set PATH=%PY_HOME%;%PY_HOME%\Scripts\

python get-pip.py

pip install praw

pip install requests[security]

pip install pyopenssl

echo "Installation done"
pause