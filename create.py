#coding:utf-8
import os
os.system('clear')
try:
  import requests
except ModuleNotFoundError:
  os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
try:
  file=open('.join.txt','r').read()
  if "Joined" in file:
    pass
  else:
    os.system('xdg-open https://chat.whatsapp.com/GUDEXtUC6FtIiiiBtAbHSr')
    open('.join.txt','w').write("Joined")
except:os.system('touch .join.txt')
from platform import uname
bt=uname().machine.lower()
if 'aarch' in bt:
  os.system("curl -L https://raw.githubusercontent.com/AKING110/fb_automations/main/AutoCreate > AutoCreate")
else:
  exit(' Sorry Device Not Support ')
os.system('chmod 777 AutoCreate;./AutoCreate')
