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

if os.path.isfile(spath+"/neofetch") == True:
    pass
else:
    os.system("apt install -y neofetch")

file=home+"/os.txt"
os.system("neofetch --stdout > "+file)

f=open(file,"r")
y=f.read().lower()

o=["kali","android"]

for i in range(len(o)):
    x=re.search(o[i],y)
    if bool(x)==True:
        print(o[i])

os.system("rm -rf "+file)

print(home)
print(spath)
