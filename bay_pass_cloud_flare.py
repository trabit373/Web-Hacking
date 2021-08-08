def _all_():
    import os
    import time
    import socket
    import sys
    import requests
    try:
        from colorama import Fore
    except:
        time.sleep(1)
        print("[-] Pleass Install The Librery --> colorama")
        sys.exit()
    from baner import baner
    os.system("clear")
    baner()
    time.sleep(1)
    text = Fore.LIGHTWHITE_EX + "  [!] " +  Fore.CYAN + "Enter Your Domain Target !\n"
    count = 0
    while True:
        try:
            text_me = text[int(count)]
            sys.stdout.write(f"{str(text_me)}"),sys.stdout.flush()
            count += 1
            time.sleep(0.08)
        except:
            print("")
            break
    target =  input(Fore.RED+"  ┌─["+Fore.GREEN+"H_NWWB"+Fore.BLUE+"~"+Fore.WHITE+"@Information-Data-For-IP"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"IP-Tools"+Fore.RED+"""]
  └──╼ """+Fore.WHITE+"卐 ")
    if target == "" or None:
        time.sleep(1)
        print(Fore.YELLOW + "["+ Fore.RED + "!" + Fore.YELLOW + "]"+ Fore.RED + " Error" + Fore.YELLOW + " >>> " + Fore.RED + "Your Target Ip None !!!")
        time.sleep(0.4)
        sys.exit()
    else:
        my_list = """
www
mail
ftp
localhost
webmail
smtp
pop
ns1
webdisk
ns2
cpanel
whm
autodiscover
autoconfig
m
imap
test
ns
blog
pop3
dev
www2
admin
forum
news
vpn
ns3
mail2
new
mysql
old
lists
support
mobile
mx
static
docs
beta
shop
sql
secure
demo
cp
calendar
wiki
web
media
email
images
img
www1
intranet
portal
video
sip
dns2
api
cdn
stats
dns1
ns4
www3
dns
search
staging
server
mx1
chat
wap
my
svn
mail1
sites
proxy
ads
host
crm
cms
backup
mx2
lyncdiscover
info
apps
download
remote
db
forums
store
relay
files
newsletter
app
live
owa
en
start
sms
office
exchange
ipv4
        """.split()
        for i in my_list:
            new_target = str(i) + "." + str(target)
            try:
                ip_target = socket.gethostname(new_target)
            except:
                time.sleep(0.4)
                print(Fore.RED + "\n[-] Sory The Tool Failed")
                time.sleep(0.3)
            else:
                print(Fore.GREEN  + f"{new_target} : {ip_target}")
                time.sleep(0.01)
    time.sleep(0.3)
    input(Fore.CYAN + "\n[!] Press Enter For Go The Meno ... ")
