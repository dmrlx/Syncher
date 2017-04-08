"""
This module contains functions for installation ssh connection with remote machine, installation
necessary software on local/remote machine, make remote directory and generate SSH keys
"""

import paramiko
from subprocess import call
from os.path import expanduser
from variables import ParserResults

class Installer(object):

    # @staticmethod   # Install ssh connection with remote machine
    def to_connect(function):
        def wrapper(*args):
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host=ParserResults.host, password=ParserResults.password, username=ParserResults.user)
            done = function(*args, ssh=ssh)
            ssh.close()
            return done
        return wrapper

    @staticmethod
    def install_local_need_soft(need_soft='rsync'):  # Install rsync on local machine
        try:
            call('sudo apt-get install -y {} > /dev/null || sudo yum install -y {} > /dev/null'.format(need_soft, need_soft), shell=True)
            return True
        except:
            return False

    @to_connect
    def install_remote_need_soft(ssh='ssh', need_soft='rsync'):  # Install rsync on remote machine
        try:
            stdin, stdout, stderr = ssh.exec_command('apt-get install -y {} > /dev/null || yum install -y {} > /dev/null'.format(need_soft, need_soft))
            return True
        except:
            return False

    @to_connect
    def remote_mkdir(ssh='ssh',need_dir=ParserResults.dirs):  # Make remote directory
        try:
            stdin, stdout, stderr = ssh.exec_command("mkdir -p {}".format(need_dir))
            return True
        except:
            return False

    pub_keys_path = expanduser('~') + '/.ssh/id_rsa'

    @staticmethod
    def generate_keys():  # Generate SSH keys
        try:
            call('ssh-keygen -t rsa -N "" -f {} > /dev/null'.format(Installer.pub_keys_path), shell=True)
            return True
        except:
            return False

if __name__ == "__main__":
    pass
