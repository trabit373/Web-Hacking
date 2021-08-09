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
    print(Fore.YELLOW + "\t\t\t\t\t  [" + Fore.GREEN + "1" + Fore.YELLOW + "]" + Fore.BLUE + " ~ " + Fore.CYAN + "GeoIP – IP Location Lookup")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t\t\t  [" + Fore.GREEN + "2" + Fore.YELLOW + "]" + Fore.BLUE + " ~ " + Fore.CYAN + "Reverse IP Lookup")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t\t\t  [" + Fore.GREEN + "3" + Fore.YELLOW + "]" + Fore.BLUE + " ~ " + Fore.CYAN + "TCP Port Scan")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t\t\t  [" + Fore.GREEN + "4" + Fore.YELLOW + "]" + Fore.BLUE + " ~ " + Fore.CYAN + "Subnet Lookup Online")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t\t\t  [" + Fore.GREEN + "5" + Fore.YELLOW + "]" + Fore.BLUE + " ~ " + Fore.CYAN + "Autonomous System Lookup (AS / ASN / IP)")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t\t\t  [" + Fore.GREEN + "6" + Fore.YELLOW + "]" + Fore.BLUE + " ~ " + Fore.CYAN + "Banner Grabbing (Search)")
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
            import geoip
            geoip._all_()
            import main_file_for_api
            main_file_for_api._all_()
            # در اینجا کدی میزنیم که به بخش قبل برود

        elif number == 2:
            import reverseiplookup
            reverseiplookup._all_()
            import main_file_for_api
            main_file_for_api._all_()
            # در اینجا کدی میزنیم که به بخش قبل برود

        elif number == 3:
            import nmap
            nmap._all_()
            import main_file_for_api
            main_file_for_api._all_()
            # در اینجا کدی میزنیم که به بخش قبل برود

        elif number == 4:
            import subnetcalc
            subnetcalc._all_()
            import main_file_for_api
            main_file_for_api._all_()
            # در اینجا کدی میزنیم که به بخش قبل برود

        elif number == 5:
            import aslookup
            aslookup._all_()
            import main_file_for_api
            main_file_for_api._all_()
            # در اینجا کدی میزنیم که به بخش قبل برود

        elif number == 6:
            import bannerlookup
            bannerlookup._all_()
            import main_file_for_api
            main_file_for_api._all_()
            # در اینجا کدی میزنیم که به بخش قبل برود


        elif number == 00:
            import main_file_for_api
            main_file_for_api._all_()
            # در اینجا کدی میزنیم که به بخش قبل برود
        
        else:
            time.sleep(0.4)
            print(Fore.RED + "\n[-] Your Number Is Not Found !")
            time.sleep(0.4)
            sys.exit()
