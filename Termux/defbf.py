import os
import instaloader
from getpass import getpass
import time
import subprocess as sub
import random
class bcolors:
    BOLD = '\033[1m'
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[95m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
def start():
    print(bcolors.OKBLUE+'''
                     :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
termux        !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
 instagram    :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
  bruteforce  ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
   attack      !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~

Version: 0.1.2
https://github.com/redKatz
https://www.instagram.com/katz.py                                                                                    
    '''
    +bcolors.ENDC)
    print(bcolors.WARNING+"\n\nš©šš ššŖš©šš¤š§ ššØšØšŖš¢ššØ š£š¤ š§ššØš„š¤š£šØšššš”šš©š® šš¤š§ šš¤š¬ š©šššØ šš¤š£š©šš£š© š¬šš”š” šš šŖšØšš\n=======================================================================\n\n"+bcolors.ENDC)
    sceltadisc = input("\n\nUse this content for educational purposes only? [yes/no]: ")
    if sceltadisc == "yes":
        print("\n")
        os.system("clear")
    else:
        exit()

def acquisizione():
    while True:
        if veri_break == "si":
            break
        USER = ""
        USER = input('\nEnter Instagram Username to bruteforce: ')
        wl = input("\nEnter world list name: ")
        sleepp = int(input("\nInsert sleep time for login [Raccomanded 900(15min)]: "))
        while True:
            sub.call("clear")
            procedere = input("Username to bruteforce = "+USER+"\n\nWordlist = "+wl+"\n\nSleep time = "+str(sleepp)+bcolors.WARNING+"\n\nProoceding? [y/break/modify]: "+bcolors.ENDC)
            if procedere == "y":
                veri_break = "si"
                break
            elif procedere == "modify":
                print("\nReturn...")
                break
            elif procedere == "break":
                exit()
            else:
                pass
