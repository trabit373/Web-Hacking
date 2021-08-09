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
    print(Fore.YELLOW + "\t\t\t\t\t  [" + Fore.GREEN + "1" + Fore.YELLOW + "]" + Fore.BLUE + " ~ " + Fore.CYAN + "NETWORK TESTS")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t\t\t  [" + Fore.GREEN + "2" + Fore.YELLOW + "]" + Fore.BLUE + " ~ " + Fore.CYAN + "DNS QUERIES")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t\t\t  [" + Fore.GREEN + "3" + Fore.YELLOW + "]" + Fore.BLUE + " ~ " + Fore.CYAN + "IP ADDRESS")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t\t\t  [" + Fore.GREEN + "4" + Fore.YELLOW + "]" + Fore.BLUE + " ~ " + Fore.CYAN + "WEB TOOLS")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t\t\t  [" + Fore.GREEN + "00" + Fore.YELLOW + "]" + Fore.BLUE + " ~ " + Fore.CYAN + "BACK")
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
            import main_network
            main_network._all_()
            import main_information_data
            main_information_data._all_()
            # در اینجا کدی میزنیم که به بخش قبل برود

        elif number == 2:
            import main_dns_queries
            main_dns_queries._all_()
            import main_information_data
            main_information_data._all_()
            # در اینجا کدی میزنیم که به بخش قبل برود

        elif number == 3:
            import main_ip_address
            main_ip_address._all_()
            import main_information_data
            main_information_data._all_()
            # در اینجا کدی میزنیم که به بخش قبل برود
        
        elif number == 4:
            import main_web_tools
            main_web_tools._all_()
            import main_information_data
            main_information_data._all_()
            # در اینجا کدی میزنیم که به بخش قبل برود

        elif number == 00:
            import main_information_data
            main_information_data._all_()
           # در اینجا کدی میزنیم که به بخش قبل برود
        
        else:
            time.sleep(0.4)
            print(Fore.RED + "\n[-] Your Number Is Not Found !")
            time.sleep(0.4)
            sys.exit()
_all_()
