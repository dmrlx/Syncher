import os
import paramiko
from platform import system
from subprocess import call
from os.path import expanduser

class ValidateParams(object):

    @staticmethod
    def check_length(parameter, param_name):
        magic_number = 777
        try:
            magic_number / len(parameter)
            return True
        except:
            return False

    class SourceFiles(object):
        @staticmethod
        def validate():
            return ValidateParams.check_length(ParserResults.dirs + ParserResults.files, "files")

    class Username(object):
        @staticmethod
        def validate():
            return ValidateParams.check_length(ParserResults.user, "user")

    class RemoteHost(object):
        @staticmethod
        def validate():
            return ValidateParams.check_length(ParserResults.host, "host")

    @staticmethod
    def check_is_need_os(os='Linux'):  # Check local OS
        if system() == os:
            return True
        else:
            return False

    @staticmethod
    def check_exists_need_soft(need_soft='rsync'):  # Check does exist rsync on local machine
        if call('which {} > /dev/null'.format(need_soft), shell=True) == 0:
            return True
        else:
            return False

    @staticmethod
    def check_pub_keys():  # Check if public ssh keys exist
        if os.path.exists(expanduser('~') + '/.ssh/id_rsa.pub') == True:
            return True
        else:
            return False

class RemoteCheck(object):

    @staticmethod
    def check_passwordless_access(host=ParserResults.host, username=ParserResults.user):  # Check passwordless access with remote host
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(host, username=username)
            return True
        except:
            return False

    @Installer.to_connect
    def check_exists_remote_need_soft(ssh='ssh', need_soft='rsync'):  # Check does exist rsync on remote machine
        stdin, stdout, stderr = ssh.exec_command('which {}'.format(need_soft))
        data = stdout.readlines()
        if len(data) != 0:
            return True
        else:
            return False

    @Installer.to_connect
    def check_remote_dir_exists(ssh='ssh', remote_dir=ParserResults.dirs):  # Check if remote directory exists
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
