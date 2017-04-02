# -*- coding: utf-8 -*-

import re
import sys
import platform
import subprocess

import receiver
import parser
import validator
import composer

# Генератор ping'a
# Пингует по умолчанию 1 раз. Можно увеличить таймер, но всё равно тригернётся на первый же ответ.
def ping_cmd_generator(host, timer=1):
    ping_cmd = "ping " + str(host) + " -c 1 " + "-W " + str(timer)
    return ping_cmd

# pusher: Отправляет сформированные в модуле composer команды
# Возвращает "0" если всё хорошо и "1" если ошибка. По крайней мере с пингом работает именно так.
def pusher(cmd):
    cmd = cmd.split()
    push = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = push.stdout.read().decode()
    error = push.stderr.read().decode()
    push.wait()
    return push.poll()

if __name__ == "__main__":
    if pusher(ping_cmd_generator("192.168.56.102")) == 1:
        print("Unavailable!")
    else:
        print("Pinged!")
