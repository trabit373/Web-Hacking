def _all_():
    import os
    import time
    import sys
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
    print(Fore.YELLOW + "\t\t\t\t\t  [" + Fore.GREEN + "1" + Fore.YELLOW + "]" + Fore.BLUE + " ~ " + Fore.CYAN + "HTTP Header Check")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t\t\t  [" + Fore.GREEN + "2" + Fore.YELLOW + "]" + Fore.BLUE + " ~ " + Fore.CYAN + "Extract Links From Page")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t\t\t  [" + Fore.GREEN + "3" + Fore.YELLOW + "]" + Fore.BLUE + " ~ " + Fore.CYAN + "Reverse Analytics Search")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t\t\t  [" + Fore.GREEN + "00" + Fore.YELLOW + "]" + Fore.BLUE + " ~ " + Fore.CYAN + "Back")
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
            import httpheaders
            httpheaders._all_()
            # در اینجا کدی میزنیم که به بخش قبل برود

        elif number == 2:
            import pagelinks
            pagelinks._all_()
            # در اینجا کدی میزنیم که به بخش قبل برود

        elif number == 3:
            import analyticslookup
            analyticslookup._all_()
            # در اینجا کدی میزنیم که به بخش قبل برود

        elif number == 00:
            pass
            # در اینجا کدی میزنیم که به بخش قبل برود
        
        else:
            time.sleep(0.4)
            print(Fore.RED + "\n[-] Your Number Is Not Found !")
            time.sleep(0.4)
            sys.exit()
