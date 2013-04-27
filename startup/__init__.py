from os import path.getmtime , system
from datetime import datetime

coms = ["dmidecode", "lshw -C multimedia -quiet", "lshw -C display -quiet", "lshw -C network -quiet", "ifconfig", "iwconfig"]
docs = ["/opt/eInfo/info/dmiinfo", "/opt/eInfo/info/auddevinfo", "/opt/eInfo/info/viddevinfo", "/opt/eInfo/info/netdevinfo", "/opt/eInfo/info/netintlocinfo", "/opt/eInfo/info/netintreminfo"]
now = rep(datetime.now()) ; now.pop(-1) ; now = "".join(now)

system("update-pciids")

for i, x in docs:
    doctime = "".join(rep(datetime.fromtimestamp(path.getmtime(x))))
    
    if now > (doctime + 9):
        system("%s > %s" %(coms[i], docs[i]))
