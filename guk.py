import re
import sys
import os

file=sys.argv[1]
x=re.search("kali",file)
if(bool(x)==True):
  os.system("apt update && apt upgrade && apt install kali-win-kex -y")
print("[=]Enter KEX command to run KALI GUI")
