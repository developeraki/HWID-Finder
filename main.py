

# aki's development.  2022

try:
    import subprocess
except ModuleNotFoundError as md:
    print(f'installing all dependencies... {md}')
    os.system('py -m pip install subprocess')

try:
    from colorama import Fore
except ModuleNotFoundError as md:
    print(f'installing all dependencies... {md}')
    os.system('py -m pip install colorama')


import os
import time


os.system('cls' if os.name == 'nt' else 'clear')

os.system('title HWID Finder     - by akii')
print(Fore.BLUE + '\t\t\t\tHWID Finder  - by aki.\n\n')

input(Fore.CYAN + '\t\tpress \'Enter\' to scan your pc and get your uuid.  ')
Fore.RESET

time.sleep(1.50)
os.system('cls' if os.name == 'nt' else 'clear')

print('scanning...')
time.sleep(1.50)

try:
    current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
    print(Fore.BLUE + f'\n\t\there your HWID : {current_machine_id}')
except:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + 'error. closing program.')
    exit(1)


# aki's development.   built for github