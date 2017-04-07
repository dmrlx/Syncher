r""" Pinger - модуль для проверки целостности соединения.

     Функция check_ping проверяет целостности соединения
     с удаленной машиной.
"""


import os
import sys

def check_ping(ip):
    response = os.system("ping -c 1 " + ip)
    if response == 0:
        return True
    else:
        return False

check_ping(ip)
