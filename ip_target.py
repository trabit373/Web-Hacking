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
        try:
            ip_target = socket.gethostname(str(target))
        except:
            time.sleep(0.7)
            print(Fore.RED + "[-] The IP Of The Subject Could Not Be Found !\n")
            time.sleep(0.2)
        else:
            time.sleep(0.7)
            print(Fore.GREEN + f"\n[+] Your target Is : {str(target)} , And IP Your target Is : {str(ip_target)}\n")
            time.sleep(0.2)
    time.sleep(0.3)
    input(Fore.CYAN + "\n[!] Press Enter For Go The Meno ... ")
