def _all_():
    import os
    import time
    import requests
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
    target =  input(Fore.RED+"  ┌─["+Fore.GREEN+"H_NWWB"+Fore.BLUE+"~"+Fore.WHITE+"@Brute-Force"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Brute-Force-All-Web-Site"+Fore.RED+"""]
  └──╼ """+Fore.WHITE+"卐 ")
    if target == "" or None:
        time.sleep(1)
        print(Fore.YELLOW + "["+ Fore.RED + "!" + Fore.YELLOW + "]"+ Fore.RED + " Error" + Fore.YELLOW + " >>> " + Fore.RED + "Your Target Ip None !!!")
        time.sleep(0.4)
        sys.exit()
    else:
        if "http://" or "https://" not in target:
            target = "https://" + target
        my_list = """
        admin
        login
        login-admin
        login/admin
        admin-login
        ADMIN-LOGIN
        LOGIN-ADMIN
        PANEL-ADMIN
        panel-admin
        admin-panel
        ADMIN-PANEL
        """.split()
        for i in my_list:
            new_target = target+ "/" + str(i)
            try:
                R = requests.get(new_target).status_code
            except:
                pass
            else:
                if R == 200 or 400:
                    print(Fore.GREEN + f"[+] This Is Found : {str(new_target)}")
                else:
                    pass
    time.sleep(0.3)
    input(Fore.CYAN + "\n[!] Press Enter For Go The Meno ... ")
