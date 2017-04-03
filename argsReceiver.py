#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
import sys


class ArgsReceiver(object):  # Получает аргументы от CLI

    @staticmethod
    def receiver():
        return sys.argv[1:]

print(ArgsReceiver.receiver())
"""

class ArgsReceiver():
    @staticmethod
    def receiver():
        first_list = ['-a', "'ssh -P -i'", "'-e ssh -P -i'", '--pass-file=/take.here',
                      "-pass='111'", './123', './1*', '/usr', '/usr/word*', '45.123',
                      'qwer.ty', 'e.t', 'user@host:/usr', 'D:\\', 'D:\\LunchBox\\inception.png']
        some_list = ['-t', '*.c', 'foo:/ps', "'-e ssh -P -i'"]
        return first_list