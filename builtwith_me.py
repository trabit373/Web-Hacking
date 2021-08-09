def _all_():
    import os
    import time
    try:
        import builtwith
    except:
        time.sleep(1)
        print("[-] Pleass Install The Librery --> builtwith")
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
    text = Fore.LIGHTWHITE_EX + "  [!] " +  Fore.CYAN + "Enter Your Domain Or IP Target !\n"
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
    target =  input(Fore.RED+"  ┌─["+Fore.GREEN+"H_NWWB"+Fore.BLUE+"~"+Fore.WHITE+"@Information-Data"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"builtwith"+Fore.RED+"""]
  └──╼ """+Fore.WHITE+"卐 ")
    if target == "" or None:
        time.sleep(1)
        print(Fore.YELLOW + "["+ Fore.RED + "!" + Fore.YELLOW + "]"+ Fore.RED + " Error" + Fore.YELLOW + " >>> " + Fore.RED + "Your Target Ip None !!!")
        time.sleep(0.4)
        sys.exit()
    else:
        if "http://" or "https://" not in target:
          target = "https://" + target
        try:
            info = builtwith.parse(target)
        except:
            time.sleep(1)
            print("")
            time.sleep(1)
        else:
            count = 1
            time.sleep(0.6)
            #print(Fore.GREEN + f"\n{info}")
            for keys,values in info.items():
              print( Fore.YELLOW + "[" + Fore.RED + f"{str(count)}"+ Fore.YELLOW + "]"+ Fore.BLUE +  " ~ "+Fore.GREEN + f"{keys}    " +Fore.BLUE + ":" + Fore.CYAN + f"    {str(values)}")
              count += 1
            time.sleep(0.3)

    time.sleep(0.3)
    input(Fore.CYAN + "\n[!] Press Enter For Go The Meno ... ")
