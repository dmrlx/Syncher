import re
import sys
import subprocess


# Class-receiver
class ArgsReceiver(object):
    @staticmethod
    def receiver():
        return sys.argv[1:]


# Class of global vars
class ParserResults(object):
    cli = ""
    password = ""
    loc = ""
    files = ""
    user = ""
    port = ""
    host = ""
    dist = ""


# Parser class
class Parser(object):

    class Rsync_options():
        @staticmethod
        def parser(some_list):
            options_pattern = r'^(-\w+|--[\w\-\=]+[\w\d\/\.\_]+)'
            password_pattern = r'-pass=.+'
            options = Parser.check_for_match(options_pattern, some_list)
            password = Parser.check_for_match(password_pattern, some_list)
            return options.replace(password, '')

    # Password parser
    class Password:
        @staticmethod
        def parser(some_list):
            pattern = r'-pass=.+'
            return Parser.check_for_match(pattern, some_list)

    # Local dir parser
    class Local_directory:
        @staticmethod
        def parser(some_list):
            pattern = r'^/.+'
            return Parser.check_for_match(pattern, some_list)

    # Files have no digits in extentions
    class Files:
        @staticmethod
        def parser(some_list):
            pattern = r'^[^-\/]{1,2}.+\D+$'
            found = Parser.check_for_match(pattern, some_list)
            remote_stuff = Parser.remote_stuff(some_list)
            return found.replace(remote_stuff, '')

    # User parser
    class Remote_user:
        @staticmethod
        def parser(some_list):
            pattern = r'^\w+[^\:\.\,]*'
            remote_stuff = Parser.remote_stuff(some_list).split('@')
            user = re.match(pattern, remote_stuff[0])
            if user or user is not None:
                return user.group(0)
            return ''

    # Remote port parser
    class Remote_port:
        @staticmethod
        def parser(some_list):
            user = Parser.Remote_user.parser(some_list)
            remote_stuff = Parser.remote_stuff(some_list).split('@')
            port = remote_stuff[0].lstrip(user)
            if port or port is not None:
                port = port.lstrip(':,.')
            return port

    class Test:
        pass

    # Host may be ip-like (i think)
    class Remote_host:
        @staticmethod
        def parser(some_list):
            remote_stuff = Parser.remote_stuff(some_list).split('@')
            if len(remote_stuff) > 1:
                host_plus_dir = remote_stuff[1].split(':')
                return host_plus_dir[0]
            return ''

    # Remote directory parser
    class Remote_directory:
        @staticmethod
        def parser(some_list):
            remote_stuff = Parser.remote_stuff(some_list).split('@')
            if len(remote_stuff) > 1:
                host_plus_dir = remote_stuff[1].split(':')
                if len(host_plus_dir) > 1:
                    return host_plus_dir[1]
            return ''

    # Can be no user nor host at all (checked)
    @staticmethod
    def remote_stuff(some_list):
        pattern = r'^.*@.*'
        for element in some_list:
            remote = re.match(pattern, element)
            if remote or remote is not None:
                return element
        return ''

    @staticmethod
    def check_for_match(pattern, some_list):
        match_list = []
        for element in some_list:
            match = re.match(pattern, element)
            if match or match is not None:
                match_list.append(element)
        return " ".join(match_list)


# Class which update global vars
class Throw_in(object):
    @staticmethod
    def parser_results():
        ParserResults.cli = Parser.Rsync_options.parser(ArgsReceiver.receiver())
        ParserResults.password = Parser.Password.parser(ArgsReceiver.receiver())
        ParserResults.loc = Parser.Local_directory.parser(ArgsReceiver.receiver())
        ParserResults.files = Parser.Files.parser(ArgsReceiver.receiver())
        ParserResults.user = Parser.Remote_user.parser(ArgsReceiver.receiver())
        ParserResults.port = Parser.Remote_port.parser(ArgsReceiver.receiver())
        ParserResults.host = Parser.Remote_host.parser(ArgsReceiver.receiver())
        ParserResults.dist = Parser.Remote_directory.parser(ArgsReceiver.receiver())


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
            return ValidateParams.Check_length(ParserResults.loc + ParserResults.files, "files")

    class Username:
        @staticmethod
        def validator():
            return ValidateParams.Check_length(ParserResults.user, "user")

    class Remote_host:
        @staticmethod
        def validator():
            return ValidateParams.Check_length(ParserResults.host, "host")

    @staticmethod
    def do_validator():
        ValidateParams.Source_files.validator()
        ValidateParams.Username.validator()
        ValidateParams.Remote_host.validator()


#Interface function
def interface(cli=None, password=None, files=None, user=None, port=None, host=None, dist=None):
    ParserResults.cli = cli
    ParserResults.password = password
    ParserResults.files = files
    ParserResults.user = user
    ParserResults.port = port
    ParserResults.host = host
    ParserResults.dist = dist
    ValidateParams.do_validator()
    # Compiler.compile()
    if ParserResults.port:
        cmd = "rsync {} {} \"ssh -p {}\" {}:{} {}".format(ParserResults.cli, ParserResults.files, ParserResults.port, ParserResults.user, ParserResults.host, ParserResults.dist)
        print("Full rsync: {}".format(cmd))
    else:
        cmd = "rsync {} {} {}:{} {}".format(ParserResults.cli, ParserResults.files, ParserResults.user, ParserResults.host, ParserResults.dist)
        print("Full rsync: {}".format(cmd))
        
if __name__ == "__main__":
    # Add OS check

    # Debug info
    Throw_in.parser_results()
    print("cli: {}".format(ParserResults.cli))
    print("password: {}".format(ParserResults.password))
    print("loc: {}".format(ParserResults.loc))
    print("files: {}".format(ParserResults.files))
    print("user: {}".format(ParserResults.user))
    print("port: {}".format(ParserResults.port))
    print("host: {}".format(ParserResults.host))
    print("dist: {}".format(ParserResults.dist))

    # Run checker
    ValidateParams.do_validator()

    if ParserResults.port:
        cmd = "rsync {} {} \"ssh -p {}\" {}:{} {}".format(ParserResults.cli, ParserResults.files, ParserResults.port, ParserResults.user, ParserResults.host, ParserResults.dist)
        print("Full rsync: {}".format(cmd))
    else:
        cmd = "rsync {} {} {}:{} {}".format(ParserResults.cli, ParserResults.files, ParserResults.user, ParserResults.host, ParserResults.dist)
        print("Full rsync: {}".format(cmd))

    # PIPE = subprocess.PIPE
    # p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT, close_fds=True)
    # print(p.stderr.read())
