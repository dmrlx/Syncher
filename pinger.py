# -*- coding: utf-8 -*-
#!/usr/bin/python


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

