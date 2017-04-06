r""" Receiver - модуль, принимающий аргументы командной строки.

     Функция receiver передает список аргументов командной строки.
"""
    
    
import sys


class ArgsReceiver(object):  # Получает аргументы от CLI

    @staticmethod
    def receiver():
        return sys.argv[1:]
