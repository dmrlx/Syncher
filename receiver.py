r""" Receiver - модуль, принимающий аргументы командной строки.
     Функция receiver передает список аргументов командной строки.
"""

from sys import argv


class ArgsReceiver(object):  # Получает аргументы от CLI

    @staticmethod
    def receiver():
        return argv[1:]