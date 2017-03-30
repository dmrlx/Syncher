import re
import sys
import platform
import subprocess

import receiver
import parser
import validator
import composer


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
