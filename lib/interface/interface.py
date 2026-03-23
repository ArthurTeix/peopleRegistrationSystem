def leiaInt(msg):
    """
    :msg: parâmetro a ser passado para checagem
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mERROR: PLEASE ENTER A VALID OPTION!\033[m")
        else:
            return n

def line(tam=42):
    print("\033[1m-\033[m" * tam)

def title(txt):
    line()
    print(f"\033[1m\033[3;35m{txt}\033[m".center(56))
    line()

def menu(list):
    title("Menu Principal")
    cont = 1

    for item in list:
        print(f"    \033[1;33m{cont}- \033[m     \033[1;36m{item}\033[m")
        cont += 1
    
    line()

    opt = leiaInt("\033[1;34mSua opção: \033[m")
    return opt
