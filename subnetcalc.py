def _all_():
    import os
    import time
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
    text = Fore.LIGHTWHITE_EX + "  [!] " +  Fore.CYAN + "Enter Cidr Or IP With Netmask !\n"
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
    target =  input(Fore.RED+"  ┌─["+Fore.GREEN+"H_NWWB"+Fore.BLUE+"~"+Fore.WHITE+"@API-hackertarget"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"IP-Address"+Fore.RED+"""]
  └──╼ """+Fore.WHITE+"卐 ")
    if target == "" or None:
        time.sleep(1)
        print(Fore.YELLOW + "["+ Fore.RED + "!" + Fore.YELLOW + "]"+ Fore.RED + " Error" + Fore.YELLOW + " >>> " + Fore.RED + "Your Target Ip None !!!")
        time.sleep(0.4)
        sys.exit()
    else:
            req = requests.get("https://api.hackertarget.com/subnetcalc/?q=" + target).text
            if req == "error valid key required":
                time.sleep(1)
                print("")
                print(Fore.RED + "error valid key required")
            elif req == "API count exceeded - Increase Quota with Membership":
                time.sleep(1)
                print("")
                print(Fore.RED + "API count exceeded - Increase Quota with Membership")
            else:
                time.sleep(1)
                print("")
                print(Fore.GREEN + req)
    input(Fore.CYAN + "\n[!] Press Enter For Go The Meno ... ")
