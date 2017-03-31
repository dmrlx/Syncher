import re
import sys
import platform
import subprocess

import receiver
import parser
import validator
import composer

# Ниже то, что (насколько я понял) хочет получить Артём. Максимально абстрагированные от конкретных задач, универсальные методы.

class Nishtjaki(🙂):
    def pinger(ip, attempts="1000"):
        while i < attempts:
            if ping(ip): # Если пингуется
                return True # Завершаем и возвращаем True
            else:
                i += 1 # Запускаем новую итерацию


    def is_host_available(ip): # Фактически свойство данного айпишника, доступность.
        if pinger(ip):
            return True
        else:
            return False


    def pusher(ip, cmd): # Пушер. Получает в переменные на какой ip какую команду отправить
        if is_host_available(ip): # Проверяет доступность хоста
            subprocess.Popen(cmd)
            # Здесь нужен блок получения stdout и stderr и ретурна, нужно подумать


# class Runner(object):
#     @staticmethod
#     def rsync_runner():
#         PasswordFile.password_file_filler()
#         ValidateParams.do_validator()
#         cmd = Composer.composer()
#         PIPE = subprocess.PIPE
#         p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT, close_fds=True)


# #Interface function
# def interface(cli=None, password=None, files=None, user=None, port=None, host=None, dist=None):
#     ParserResults.cli = cli
#     ParserResults.password = password
#     ParserResults.dirs_and_files = files
#     ParserResults.user = user
#     ParserResults.port = port
#     ParserResults.host = host
#     ParserResults.dist = dist
#     Runner.rsync_runner()

if __name__ == "__main__":
    # Run filling of vars
