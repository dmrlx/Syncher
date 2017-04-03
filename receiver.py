#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


class ArgsReceiver(object):  # Получает аргументы от CLI

    @staticmethod
    def receiver():
        return sys.argv[1:]

print(ArgsReceiver.receiver())