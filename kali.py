import re
import sys
import os

if(sys.argv[1]==None):
  file=sys.argv[1]
else:
  command="cd $HOME && cat /etc/os-release > $HOME/os.txt"
  os.system(command)
  file=$HOME/os.txt
f=open(file,"r")
#x=re.split("\n",f)
x=re.search("kali",f.read())
if(bool(x)==True):
  a=1
else:
  a=0
print(a)

