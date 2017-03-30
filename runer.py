import re
import sys
import platform
import subprocess

import receiver
import parser
import validator
import composer


# Class-receiver
class ArgsReceiver(object):
    @staticmethod
    def receiver():
        return sys.argv[1:]


# Class which update global vars
class ThrowIn(object):
    @staticmethod
    def parser_results():
        ParserResults.cli = Parser.Options.parser(ArgsReceiver.receiver())
        # print("cli: {}".format(ParserResults.cli))
        ParserResults.password = Parser.Password.parser(ArgsReceiver.receiver())
        # print("password: {}".format(ParserResults.password))
        ParserResults.dirs_and_files = Parser.DirsAndFiles.parser(ArgsReceiver.receiver())
        # print("dirs and files: {}".format(ParserResults.dirs_and_files))
        ParserResults.user = Parser.RemoteUser.parser(ArgsReceiver.receiver())
        # print("user: {}".format(ParserResults.user))
        ParserResults.port = Parser.RemotePort.parser(ArgsReceiver.receiver())
        # print("port: {}".format(ParserResults.port))
        ParserResults.host = Parser.RemoteHost.parser(ArgsReceiver.receiver())
        # print("host: {}".format(ParserResults.host))
        ParserResults.dist = Parser.RemoteDirectory.parser(ArgsReceiver.receiver())
        # print("dist: {}".format(ParserResults.dist))


# Validator class
class ValidateParams(object):
    @staticmethod
    def check_length(parameter, param_name):
        magic_number = 777
        try:
            magic_number / len(parameter)
            return parameter
        except ZeroDivisionError:
            print('Unfortunately, you forgot define {}!\nFormat rsync function : rsync [OPTION] ... SRC ... [USER@] HOST:DEST \nPlease, try again'.format(param_name))
            sys.exit(1)

    class SourceFiles:
        @staticmethod
        def validator():
            return ValidateParams.check_length(ParserResults.dirs_and_files, "files")

    class Username:
        @staticmethod
        def validator():
            return ValidateParams.check_length(ParserResults.user, "user")

    class RemoteHost:
        @staticmethod
        def validator():
            return ValidateParams.check_length(ParserResults.host, "host")

    @staticmethod
    def check_local_os_version():   # Check local OS
        if platform.system() == "Linux":
            ValidateParams.check_exists()   #Check does exist rsync on local machine
        else:
            print('Unfortunately, your OS is {}! Rsync works only with Unix-like systems.'.format(platform.system()))
            sys.exit(1)

    @staticmethod
    def check_exists(): #Check does exist rsync on local machine
        if subprocess.call('which rsync > /dev/null', shell=True) == 0:
            pass
        else:
            print("Unfortunately, rsync doesn't exist on your machine! Let's install it!")
            ValidateParams.install_rsync()  #Install rsync on local machine

    @staticmethod
    def install_rsync():    #Install rsync on local machine
        try:
            subprocess.call('apt-get install -y rsync > /dev/null || yum install -y rsync > /dev/null', shell=True)
            print("Rsync was successfully installed!")
        except:
            print("OOps..! Rsync wasn't installed on your machine! Please, check machine's configuration and try again!")

    @staticmethod
    def do_validator():
        ValidateParams.SourceFiles.validator()
        ValidateParams.Username.validator()
        ValidateParams.RemoteHost.validator()
        ValidateParams.check_local_os_version()


# Add password file name
class PasswordFile(object):
    @staticmethod
    def password_file_filler():
        if ParserResults.password:
            ParserResults.pass_file = "sshpass.txt"
            f = open(ParserResults.pass_file, "w")
            f.write(ParserResults.password)
            f.close()


class Composer(object):
    @staticmethod
    def composer():
        cmd = "rsync "
        if ParserResults.port:
            ssh_param = "-e \"ssh -p {}\" ".format(ParserResults.port)
        else:
            ssh_param = ""

        if ParserResults.cli:
            cli_param = ParserResults.cli + " "
        else:
            cli_param = ""

        if ParserResults.dirs_and_files:
            dirs_and_files_param = ParserResults.dirs_and_files + " "
            cli_param += "-r "
        else:
            dirs_and_files_param = ""

        if ParserResults.dist:
            dist_param = ParserResults.dist
        else:
            dist_param = ""

        if ParserResults.pass_file:
            pass_file_param = "--password-file={} ".format(ParserResults.pass_file)
        else:
            pass_file_param = ""

        return cmd + cli_param + ssh_param + dirs_and_files_param + pass_file_param + ParserResults.user + "@" + ParserResults.host + ":" + dist_param


class Runner(object):
    @staticmethod
    def rsync_runner():
        PasswordFile.password_file_filler()
        ValidateParams.do_validator()
        cmd = Composer.composer()
        PIPE = subprocess.PIPE
        p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT, close_fds=True)


#Interface function
def interface(cli=None, password=None, files=None, user=None, port=None, host=None, dist=None):
    ParserResults.cli = cli
    ParserResults.password = password
    ParserResults.dirs_and_files = files
    ParserResults.user = user
    ParserResults.port = port
    ParserResults.host = host
    ParserResults.dist = dist
    Runner.rsync_runner()

if __name__ == "__main__":
    # Run filling of vars
    ThrowIn.parser_results()
    Runner.rsync_runner()
