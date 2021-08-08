def _all_():
    import os
    import time
    import sys
    try:
        import ipapi
    except:
        time.sleep(1)
        print("[-] Pleass Install The Librery --> colorama")
        sys.exit()
    from baner import baner
    from colorama import Fore
    os.system("clear")
    baner()
    time.sleep(0.3)
    text = Fore.LIGHTWHITE_EX + "  [!] " +  Fore.CYAN + "Enter Your IP Target !\n"
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
    ip_target =  input(Fore.RED+"  ┌─["+Fore.GREEN+"H_NWWB"+Fore.BLUE+"~"+Fore.WHITE+"@Information-Data-For-IP"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"IP-Tools"+Fore.RED+"""]
  └──╼ """+Fore.WHITE+"卐 ")
    if ip_target == "" or None:
        time.sleep(1)
        print(Fore.YELLOW + "["+ Fore.RED + "!" + Fore.YELLOW + "]"+ Fore.RED + " Error" + Fore.YELLOW + " >>> " + Fore.RED + "Your Target Ip None !!!")
        time.sleep(0.4)
        sys.exit()
    try:
        info = ipapi.location(ip_target)
    except:
        time.sleep(1)
        print(Fore.RED + "\n[!] ~ Error : Your Ip Is Not Found Or Private ;(((")
        sys.exit()
    time.sleep(0.5)
    print(Fore.BLUE + "[" + Fore.RED + "1" + Fore.BLUE + "]" + Fore.RED + "  ~ " + Fore.YELLOW + "Ip                     :   " + Fore.CYAN + info["ip"])
    time.sleep(0.3)
    print(Fore.BLUE + "[" + Fore.RED + "2" + Fore.BLUE + "]" + Fore.RED + "  ~ " + Fore.YELLOW + "Version                :   " + Fore.CYAN + info["version"])
    time.sleep(0.3)
    print(Fore.BLUE + "[" + Fore.RED + "3" + Fore.BLUE + "]" + Fore.RED + "  ~ " + Fore.YELLOW + "City                   :   " + Fore.CYAN + info["city"])
    time.sleep(0.3)
    print(Fore.BLUE + "[" + Fore.RED + "4" + Fore.BLUE + "]" + Fore.RED + "  ~ " + Fore.YELLOW + "Region                 :   " + Fore.CYAN + info["region"])
    time.sleep(0.3)
    print(Fore.BLUE + "[" + Fore.RED + "5" + Fore.BLUE + "]" + Fore.RED + "  ~ " + Fore.YELLOW + "Country                :   " + Fore.CYAN + info["country"])
    time.sleep(0.3)
    print(Fore.BLUE + "[" + Fore.RED + "6" + Fore.BLUE + "]" + Fore.RED + "  ~ " + Fore.YELLOW + "Country_Name           :   " + Fore.CYAN + info["country_name"])
    time.sleep(0.3)
    print(Fore.BLUE + "[" + Fore.RED + "7" + Fore.BLUE + "]" + Fore.RED + "  ~ " + Fore.YELLOW + "Country_Code           :   " + Fore.CYAN + info["country_code"])
    time.sleep(0.3)
    print(Fore.BLUE + "[" + Fore.RED + "8" + Fore.BLUE + "]" + Fore.RED + "  ~ " + Fore.YELLOW + "Country_Code_Iso3      :   " + Fore.CYAN + info["country_code_iso3"])
    time.sleep(0.3)
    print(Fore.BLUE + "[" + Fore.RED + "9" + Fore.BLUE + "]" + Fore.RED + "  ~ " + Fore.YELLOW + "Country_Capital        :   " + Fore.CYAN + info["country_capital"])
    time.sleep(0.3)
    print(Fore.BLUE + "[" + Fore.RED + "10" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Country_Tld            :   " + Fore.CYAN + info["country_tld"])
    time.sleep(0.3)
    print(Fore.BLUE + "[" + Fore.RED + "11" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Continent_Code         :   " + Fore.CYAN + info["continent_code"])
    time.sleep(0.3)
    #print(Fore.BLUE + "[" + Fore.RED + "number" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Postal                 :   " + Fore.CYAN + info["postal"])
    #time.sleep(0.3)
    #print(Fore.BLUE + "[" + Fore.RED + "number" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Latitude               :   " + Fore.CYAN + info["latitude"])
    #time.sleep(0.3)
    #print(Fore.BLUE + "[" + Fore.RED + "number" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Longitude              :   " + Fore.CYAN + info["longitude"])
    #time.sleep(0.3)
    #print(Fore.BLUE + "[" + Fore.RED + "number" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Timezone               :   " + Fore.CYAN + info["timezone"])
    #time.sleep(0.3)
    #print(Fore.BLUE + "[" + Fore.RED + "number" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Utc_Offset             :   " + Fore.CYAN + info["utc_offset"])
    #time.sleep(0.3)
    print(Fore.BLUE + "[" + Fore.RED + "12" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Country_Calling_Code   :   " + Fore.CYAN + info["country_calling_code"])
    time.sleep(0.3)
    print(Fore.BLUE + "[" + Fore.RED + "13" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Currency               :   " + Fore.CYAN + info["currency"])
    time.sleep(0.3)
    print(Fore.BLUE + "[" + Fore.RED + "14" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Currency_Name          :   " + Fore.CYAN + info["currency_name"])
    time.sleep(0.3)
    print(Fore.BLUE + "[" + Fore.RED + "15" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Languages              :   " + Fore.CYAN + info["languages"])
    time.sleep(0.3)
    #print(Fore.BLUE + "[" + Fore.RED + "number" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Country_Area           :   " + Fore.CYAN + info["country_area"])
    #time.sleep(0.3)
    #print(Fore.BLUE + "[" + Fore.RED + "number" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Country_Population     :   " + Fore.CYAN + info["country_population"])
    #time.sleep(0.3)
    print(Fore.BLUE + "[" + Fore.RED + "16" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Asn                    :   " + Fore.CYAN + info["asn"])
    time.sleep(0.3)
    print(Fore.BLUE + "[" + Fore.RED + "17" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Org                    :   " + Fore.CYAN + info["org"])
    time.sleep(1)
    print("")
    input(Fore.CYAN + "\n[!] Press Enter For Go The Meno ... ")
