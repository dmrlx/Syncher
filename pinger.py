r""" Pinger - модуль для проверки целостности соединения.

     Функция check_ping проверяет целостности соединения
     с удаленной машиной.
"""

import os
import parser

def check_ping(ip):
    hostname = ip
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        return True
    else:
        return False


#sys.exit(0)

