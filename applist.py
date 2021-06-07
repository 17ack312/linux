import re
import os
import sys

home = sys.argv[1]

command="apt update && apt upgrade -y"
os.system(command)

file=home+"/temp/list.txt"

command="apt list >> "+file
os.system(command)

out=home+"/temp/applist.txt"

f =open(file,"r")

for i in f:
    line=f.readline()
    temp=re.split("/",line)
   # print(temp[0])
    string="apt install -y "+temp[0]+"\n"
    g=open(out,"a")
    g.write(string)

q=input("\n[?]Do you want to view installer documentation ??(Y/n)\n[>] ").lower()
if q=='y' or q=='yes':
    command="cat "+out
    os.system(command)

command="rm "+file
os.system(command)
