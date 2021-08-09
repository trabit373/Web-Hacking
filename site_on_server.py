def _all_():

    import os
    import time
    import sys
    import json
    import requests
    from baner import baner
    from colorama import Fore

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
    target =  input(Fore.RED+"  ┌─["+Fore.GREEN+"H_NWWB"+Fore.BLUE+"~"+Fore.WHITE+"@WEB-Tools"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"site-on-server"+Fore.RED+"""]
  └──╼ """+Fore.WHITE+"卐 ")
    if target == "" or None:
        time.sleep(1)
        print(Fore.YELLOW + "["+ Fore.RED + "!" + Fore.YELLOW + "]"+ Fore.RED + " Error" + Fore.YELLOW + " >>> " + Fore.RED + "Your Target Ip None !!!")
        time.sleep(0.4)
        sys.exit()
    else:
        data_me = {"remoteAddress" : target}
        url = requests.post("https://domains.yougetsignal.com/domains.php",data_me)
        info = json.loads(url.content)
        count = 1
        print("")
        for i in info["domainArray"]:
            if "https://" or "http://" not in i[0]:
                i[0] = "https://" + i[0]
                data_me = Fore.LIGHTBLACK_EX + f"  [{count}] ~ "   + Fore.CYAN + str(i[0])
            else:
                data_me = Fore.LIGHTBLACK_EX + f"  [{count}] ~ "   + Fore.CYAN + str(i[0])
            print(data_me)
            count += 1
    time.sleep(0.3)
    input(Fore.CYAN + "\n[!] Press Enter For Go The Meno ... ")
