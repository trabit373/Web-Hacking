def baner():
    import os
    import time
    import sys
    try:
        from colorama import Fore
    except:
        time.sleep(1)
        print("[-] Pleass Install The Librery --> colorama")
        sys.exit()
    text1 = (Fore.LIGHTBLACK_EX +  """
  ██╗  ██╗                ███╗   ██╗██╗    ██╗██╗    ██╗██████╗
  ██║  ██║                ████╗  ██║██║    ██║██║    ██║██╔══██╗
  ███████║                ██╔██╗ ██║██║ █╗ ██║██║ █╗ ██║██████╔╝
  ██╔══██║                ██║╚██╗██║██║███╗██║██║███╗██║██╔══██╗
  ██║  ██║    ███████╗    ██║ ╚████║╚███╔███╔╝╚███╔███╔╝██████╔╝
  ╚═╝  ╚═╝    ╚══════╝    ╚═╝  ╚═══╝ ╚══╝╚══╝  ╚══╝╚══╝ ╚═════╝
  ═════════════════════════════════════════════════════════════""")



    os.system("clear")
    count = 0
    while True:
        try:
            text_me = text1[int(count)]
            sys.stdout.write(f"{str(text_me)}"),sys.stdout.flush()
            count += 1
            time.sleep(0.003)
        except:
            print("")
            break
    

    text2 = (Fore.LIGHTBLACK_EX    + 
  """  **                      Name : ?                           **
  **                      Family : ?                         **
  **                      Muzic : A M R O F - C O L          **
  **                      Live : M U Z I C                   **""")

    count2 = 0
    while True:
        try:
            text_me = text2[int(count2)]
            sys.stdout.write(f"{str(text_me)}"),sys.stdout.flush()
            count2 += 1
            time.sleep(0.015)
        except:
            print("")
            break


    text3 = (Fore.LIGHTBLACK_EX + """  ═════════════════════════════════════════════════════════════
  """)
    count3 = 0
    while True:
        try:
            text_me = text3[int(count3)]
            sys.stdout.write(f"{str(text_me)}"),sys.stdout.flush()
            count3 += 1
            time.sleep(0.003)
        except:
            print("")
            break
