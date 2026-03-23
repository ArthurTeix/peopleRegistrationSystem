from lib.interface.interface import *
from lib.archive.archive import *
import os
from time import sleep

arc = 'people.txt'

if not fileExist(arc):
    createFile()

# program main
while True:
    option = menu(['View Registered People', 'Register New Person', 'Exit the System'])

    if option == 1: # option to list people
        readFile('people.txt')
        enter = input("\033[2;37m   Click 'Enter' to Continue!\033[m")
        os.system("cls")

    elif option == 2:
        title('New Cadaster')
        namePeople = str(input("\033[1;33mName: \033[m"))
        agePeople = leiaInt('\033[1;33mIdade: \033[m')
        
        registerPeople(arc, namePeople, agePeople)
        sleep(2)
        os.system("cls")

    elif option == 3:
        title('\033[2;37m   Exiting the System... See you later!\033[m')
        break

    else:
        print("\033[0;31mERROR: PLEASE ENTER A VALID OPTION!\033[m")
