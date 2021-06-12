import os,re,sys


home=sys.argv[1]

string=""
if(home!="/root"):
    x=re.split("/",home)
    x.remove('home')
    for i in range(0,len(x)):
        #print(x[i])
        string=string+"/"+x[i]
    home=string+"/home"
    spath=string+"/usr/bin"
else:
    home="/root"
    spath="/usr/bin"
    
print(home)
print(spath)
