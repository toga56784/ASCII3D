import os

def clear_console():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
