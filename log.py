import os
import time

from getpass import getpass

def menu():
    os.system('clear')
    print("\033[1;96m")
    x = input('\033[1;92mUsername \033[1;93m: ')
    print("")
    o = input(" Yakin Mau Lanjut!!! [ iya ] : ")
    print("")
    if o=="Tidak":
        e = input('\033[1;92mPassword \033[1;93m: ')
    elif o=="iya":
        e = getpass('\033[1;92mPassword \033[1;93m: ')
    if x=="Ardi" and e=="Ardi":
        print("")
    else:
         print("")
         print("")
         print("\033[1;91m Sekarang Loginnya Gak Bisa Di Inject lho 😜")
         time.sleep(2)
         os.system('ps')
         os.system('killall -9 com.termux')
menu()

os.system('clear')