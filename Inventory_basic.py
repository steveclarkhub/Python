"""
Inventory host values to stdout
Stack overflow: https://stackoverflow.com/questions/3103178/how-to-get-the-system-info-with-python
use platfrom.dist() as version test case. deprecated in 5 & removed in 8
"""
import platform
import socket
import re
import uuid
import psutil # not part of std lib

print('platform:',platform.system())
print('platform-release:',platform.release())
print('architecture:',platform.machine())
print('hostname:',socket.gethostname())
print('ip-address:',socket.gethostbyname(socket.gethostname()))
print('mac-address:',':'.join(re.findall('..', '%012x' % uuid.getnode())))
print('ram:',str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB")
print('cpu %:',psutil.cpu_percent(1))
print('cpu cores:',psutil.cpu_count())
