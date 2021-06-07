import sys
import os
import re

home = sys.argv[1]
file=home+"/temp/plist.txt"
command="pip3 list >> "+file
os.system(command)

f=open(file,"r")
out=home+"/temp/pip.txt"
j=0
for i in f:
    y=f.readline()
    if (j>=1):
        x=re.split("\s",y)
        #print(x[0])
        g=open(out,"a")
        g.write(x[0]+"\n")
    j += 1

f.close()
