"""
This module validates parameters's sufficiency which were received from parser module,
does some necessary checks on local machine as check OS, exist or not rsync, exist or not
public ssh keys and some checks for remote machine as check passwordless access, exist or
not rsync, exists or not remote directory
"""

import os
import paramiko
from platform import system
from subprocess import call
from os.path import expanduser

from variables import ParserResults
from installer import Installer

class ValidateParams(object):

    @staticmethod
    def check_length(parameter, param_name):    # Staticmethod for check that necessary parameter exist
        magic_number = 777
        try:
            magic_number / len(parameter)
            return True
        except:
            return False

    class SourceFiles(object):
        
        @staticmethod
        def validate():     # Check that source files exists
            return ValidateParams.check_length(ParserResults.dirs + ParserResults.files, "files")

    class Username(object):
        
        @staticmethod
        def validate():     # Check that Username exists
            return ValidateParams.check_length(ParserResults.user, "user")

    class RemoteHost(object):
        
        @staticmethod
        def validate():     # Check that remote host exists  
            return ValidateParams.check_length(ParserResults.host, "host")

    @staticmethod
    def check_is_need_os(os='Linux'):  # Check that local OS is Unix system
        if system() == os:
            return True
        else:
            return False

    @staticmethod
    def check_exists_need_soft(need_soft='rsync'):  # Check that rsync exists on local machine
        if call('which {} > /dev/null'.format(need_soft), shell=True) == 0:
            return True
        else:
            return False

    @staticmethod
    def check_pub_keys():  # Check that public ssh keys exist
        if os.path.exists("{}id_rsa.pub".format(Installer.keys_path)) == True:
            return True
        else:
            return False

class RemoteCheck(object):

    @staticmethod
    def check_passwordless_access(host=ParserResults.host, username=ParserResults.user):  # Check passwordless access with remote machine
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(host, username=username)
            return True
        except:
            return False

    @Installer.to_connect
    def check_exists_remote_need_soft(ssh='ssh', need_soft='rsync'):  # Check that rsync exists on remote machine
        stdin, stdout, stderr = ssh.exec_command('which {}'.format(need_soft))
        data = stdout.readlines()
        if len(data) != 0:
            return True
        else:
            return False

    @Installer.to_connect
    def check_remote_dir_exists(ssh='ssh', remote_dir=ParserResults.dirs):  # Check that directory exists on remote machine
        split_dir = remote_dir.split("/")
        if '*' in remote_dir:
            usefull_part = "/".join(split_dir[2:-1])
        else:
            usefull_part = "/".join(split_dir[2:])
        need_dir = expanduser('~') + '/' + usefull_part
        stdin, stdout, stderr = ssh.exec_command("find {} ".format(need_dir))
        output = stdout.readlines()
        if len(output) != 0:
            return True
        else:
            return False

if __name__ == "__main__":
    from variables import ParserResults
    from installer import Installer
