import re
import os

os.system("apt update && apt upgrade -y")

os.system("apt list >> $HOME/temp/list.txt")
file="$HOME/temp/list.txt"
f =open(file,"r")

for i in f:
    line=f.readline()
    temp=re.split("/",line)
   # print(temp[0])
    string="apt install -y "+temp[0]+"\n"
    g=open("$HOME/temp/applist.txt","a")
    g.write(string)

q=input("\n[?]Do you want to view installer documentation ??(Y/n)\n[>] ").lower()

if q=='y' or q=='yes':
    os.system("cat $HOME/temp/applist.txt")

os.system("rm $HOME/temp/list.txt")
