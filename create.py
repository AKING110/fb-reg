#coding:utf-8
import os
os.system('clear')
try:
  import requests
except ModuleNotFoundError:
  os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
try:
  import pycurl
except:os.system('pip install pycurl')
os.system('xdg-open https://chat.whatsapp.com/FwFmZyWx4X3GQyxV4jEtSU')
os.system('git pull')
from platform import uname
bt=uname().machine.lower()
if 'aarch' in bt:
  os.system('chmod 777 AutoCreate;./AutoCreate')
else:
  exit(' Sorry Device Not Support ')
