from lib.interface.interface import *

def fileExist(name):
    try:
        a = open(name, 'rt')
        a.close()
        return True
    except FileNotFoundError:
        return False


def createFile():
    open('people.txt', 'wt+').close


def readFile(name):
    try:
        a = open(name, 'rt')
    except:
        print("\033[1;31mERROR: READ THE FILE")
    else:
        title("REGISTERED PEOPLE")
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].strip()
            print(f"{dado[0]:<30}  {dado[1]:>3} anos")
    finally:
        a.close


def registerPeople(archive, name='Desconhecido', age='0'):
    try:
        a = open(archive, 'at')
    except:
        print("\033[1;31mERROR: FILE NOT OPEN\033[m")
    else:
        try:
            a.write(f"{name};{age}\n")
        except:
            print("\033[1;31mERROR: WRITING\033[m")
        else:
            print("\033[1;32mNew Cadaster Concluited!\033[m")
