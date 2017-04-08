# -*- coding: utf-8 -*-

import re
import sys
import platform
import subprocess
import parser
import receiver
from variables import ParserResults
import pinger
import validator
import installer
import bridge
import composer

# Генератор ping'a
# Пингует по умолчанию 1 раз. Можно увеличить таймер, но всё равно тригернётся на первый же ответ.
# def ping_cmd_generator(host, timer=1):
#     ping_cmd = "ping " + str(host) + " -c 1 " + "-W " + str(timer)
#     return ping_cmd

# pusher: Отправляет сформированные в модуле composer команды
# Возвращает "0" если всё хорошо и "1" если ошибка. По крайней мере с пингом работает именно так.
# def pusher(cmd):
#     cmd = cmd.split()
#     push = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     output = push.stdout.read().decode()
#     error = push.stderr.read().decode()
#     push.wait()
#     return push.poll()

# if pusher(ping_cmd_generator("192.168.56.102")) == 1:
#     print("Unavailable!")
# else:
#     print("Pinged!")

def cmd_runer(cmd):
    try:
        subprocess.call(cmd, shell=True)
        return True
    except:
        return False


def main():
    parser.execute(receiver.ArgsReceiver.receiver(), ParserResults)

    # print("cli: {}".format(ParserResults.cli))
    # print("password: {}".format(ParserResults.password))
    # print("remote dirs: {}".format(ParserResults.dirs))
    # print("files: {}".format(ParserResults.files))
    # print("user: {}".format(ParserResults.user))
    # print("port: {}".format(ParserResults.port))
    # print("host: {}".format(ParserResults.host))
    # print("dist: {}".format(ParserResults.dist))

    if not validator.ValidateParams.SourceFiles.validate():
        print("Required parameter is not specified: source files")
        exit()
    if not validator.ValidateParams.Username.validate():
        print("Required parameter is not specified: username")
        exit()
    if not validator.ValidateParams.RemoteHost.validate():
        print("Required parameter is not specified: remote host")
        exit()


    if validator.ValidateParams.check_is_need_os:
        if pinger.check_ping(ParserResults.host): # Если пингуется машина
            if not validator.ValidateParams.check_exists_need_soft(): # Проверяем установлен ли rsync
                # print(validator.ValidateParams.check_exists_need_soft())
                installer.Installer.install_local_need_soft() # Устанавливаем если нет
                # print(installer.Installer.install_local_need_soft())

            print(validator.ValidateParams.check_pub_keys())
            if not validator.ValidateParams.check_pub_keys(): # Проверяем проброшены ли ключи
                installer.Installer.generate_keys() # Генерируем ключи
            #bridge.key_transfer(installer.Installer.pub_keys_path) # Пробрасываем
            print(ParserResults.dirs)
            print(ParserResults.files)
            cmd_runer(composer.Composer.composer())

        else:
            print("Host is unavailable!")
    else:
        print("Wrong OS!")

