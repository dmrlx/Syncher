import re
import os
import sys
import platform
import subprocess


# Class-receiver
class ArgsReceiver(object):
    @staticmethod
    def receiver():
        return sys.argv[1:]


# Class of global vars
class ParserResults(object):
    cli = ""                # Params
    password = ""           # Password
    dirs_and_files = ""     # Sincable files and folders
    user = ""               # User name
    port = ""               # Port (if needed)
    host = ""               # Host name
    dist = ""               # Distenation folder
    pass_file = ""          # Password file


class Parser(object):
    @staticmethod
    def check_for_match(pattern, some_list):
        match_list = []
        for element in some_list:
            match = re.match(pattern, element)
            if match:
                match_list.append(element)
        return " ".join(match_list)

    class Options:
        @staticmethod
        def parser(some_list):
            options_pattern = r'(^-\w+|^--[\w\-\=]+[\w\d\/\.\_]+|^[\'"].+[\'"]$)'
            password_pattern = r'-pass=.+'
            options = Parser.check_for_match(options_pattern, some_list)
            password = Parser.check_for_match(password_pattern, some_list)
            return options.replace(password, '')

    class Password:
        @staticmethod
        def parser(some_list):
            pattern = r'-pass=.+'
            return Parser.check_for_match(pattern, some_list)

    class DirsAndFiles:
        @staticmethod
        def parser(some_list):
            pattern = r'^[^-\'"].+'
            found = Parser.check_for_match(pattern, some_list)
            remote_stuff = Parser.remote_stuff(some_list)
            return found.replace(remote_stuff, '')

# Can be no user nor host at all
    @staticmethod
    def remote_stuff(some_list):
        pattern_full = r'^.+@.+'
        pattern_host = r'^.+:.*'
        for element in some_list:
            remote_full = re.match(pattern_full, element)
            remote_host = re.match(pattern_host, element)
            if remote_full:
                return element
            elif remote_host:
                return element
        return ''

    class RemoteUser:
        @staticmethod
        def parser(some_list):
            pattern = r'^\w+[^\:\.\,\@]*'
            remote_stuff = Parser.remote_stuff(some_list)
            if '@' in remote_stuff:
                user = re.match(pattern, remote_stuff)

                if user:
                    return user.group(0)
            return ''

    class RemotePort:
        @staticmethod
        def parser(some_list):
            user = Parser.RemoteUser.parser(some_list)
            remote_stuff = Parser.remote_stuff(some_list)
            if '@' in remote_stuff:
                remote_stuff = remote_stuff.split('@')
                port = remote_stuff[0].lstrip(user)
                if port:
                    port = port.lstrip(':,.')
                    return port
            return ''

# Host may be ip-like
    class RemoteHost:
        @staticmethod
        def parser(some_list):
            remote_stuff = Parser.remote_stuff(some_list)
            if '@' in remote_stuff:
                host_plus_dir = remote_stuff.split('@')[1].split(':')
                return host_plus_dir[0]
            else:
                host_plus_dir = remote_stuff.split(':')
                return host_plus_dir[0]

    class RemoteDirectory:
        @staticmethod
        def parser(some_list):
            remote_stuff = Parser.remote_stuff(some_list)
            if '@' in remote_stuff:
                host_plus_dir = remote_stuff.split('@')[1].split(':')
                if len(host_plus_dir) > 1:
                    return host_plus_dir[1]
            else:
                host_plus_dir = remote_stuff.split(':')
                if len(host_plus_dir) > 1:
                    return host_plus_dir[1]
                return ''


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
    def Check_length(parametr, param_name):
        magic_number = 777
        try:
            magic_number / len(parametr)
            return parametr
        except:
            print('Unfortunately, you forgot define {}!\nFormat rsync function : rsync [OPTION] ... SRC ... [USER@] HOST:DEST \nPlease, try again'.format(param_name))
            sys.exit(1)

    class Source_files:
        @staticmethod
        def validator():
            return ValidateParams.Check_length(ParserResults.dirs_and_files, "files")

    class Username:
        @staticmethod
        def validator():
            return ValidateParams.Check_length(ParserResults.user, "user")

    class Remote_host:
        @staticmethod
        def validator():
            return ValidateParams.Check_length(ParserResults.host, "host")

    @staticmethod
    def Check_local_os_version():   # Check local OS
        if platform.system() == "Linux":
            ValidateParams.Check_exists()   #Check does exist rsync on local machine
        else:
            print('Unfortunately, your OS is {}! Rsync works only with Unix-like systems.'.format(platform.system()))
            sys.exit(1)

    @staticmethod
    def Check_exists(): #Check does exist rsync on local machine
        if subprocess.call('which rsync > /dev/null', shell=True) == 0:
            pass
        else:
            print("Unfortunately, rsync doesn't exist on your machine! Let's install it!")
            ValidateParams.Install_rsync()  #Install rsync on local machine

    @staticmethod
    def Install_rsync():    #Install rsync on local machine
        try:
            subprocess.call('apt-get install -y rsync > /dev/null || yum install -y rsync > /dev/null', shell=True)
            print("Rsync was successfully installed!")
        except:
            print("OOps..! Rsync wasn't installed on your machine! Please, check machine's configuration and try again!")

    @staticmethod
    def do_validator():
        ValidateParams.Source_files.validator()
        ValidateParams.Username.validator()
        ValidateParams.Remote_host.validator()
        ValidateParams.Check_local_os_version()


# Add password file name
class PasswordFile(object):
    @staticmethod
    def password_file_filler():
        if ParserResults.pass_file:
            pass_file_name = "sshpass"
            f = open(pass_file_name, "w")
            f.write(ParserResults.password)
            f.close


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
            pass_file_param = ParserResults.pass_file + " "
        else:
            pass_file_param = ""

        return cmd + cli_param + ssh_param + dirs_and_files_param + pass_file_param + ParserResults.user + "@" + ParserResults.host + ":" + dist_param


class Runner(object):
    @staticmethod
    def rsync_runner():
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
    PasswordFile.password_file_filler()
    Runner.rsync_runner()

if __name__ == "__main__":
    # Run filling of vars
    ThrowIn.parser_results()
    PasswordFile.password_file_filler()
    Runner.rsync_runner()
