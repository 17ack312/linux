import re
import os

os.system("apt update && apt upgrade -y")

os.system("apt list >> $HOME/list.txt")
file="$HOME/list.txt"
f =open(file,"r")

for i in f:
    line=f.readline()
    temp=re.split("/",line)
   # print(temp[0])
    string="apt install -y "+temp[0]+"\n"
    g=open("$HOME/applist.txt","a")
    g.write(string)

q=input("\n[?]Do you want to view installer documentation ??(Y/n)\n[>] ").lower()

if q=='y' or q=='yes':
    os.system("cat $HOME/applist.txt")

os.system("rm $HOME/list.txt")
