r""" Pinger - модуль для проверки целостности соединения.

     Функция check_ping проверяет целостности соединения
     с удаленной машиной.
"""


import os
import parser
import sys
from variables import ParserResults

def check_ping():
    hostname = ParserResults.host
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        return True
    else:
        return False


# sys.exit(0)

