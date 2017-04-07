from variables import ParserResults
import paramiko

class Installer(object):
    __pub_keys_path = '~/.ssh/id_rsa'

    @property
    def pub_keys_path(self):
        return self.__tahograph

    def to_connect(function, host=ParserResults.host, password=ParserResults.password, username=ParserResults.user):
        def wrapper(*args):
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, password=password, username=username)
            return function(*args, ssh=ssh)
        return wrapper