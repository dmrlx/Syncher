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
    full_host = ""


# Parser class
class Parser(object):
    @staticmethod
    def check_for_match(pattern, some_list):
        match_list = []
        for element in some_list:
            match = re.match(pattern, element)
            if match:
                match_list.append(element)
        return " ".join(match_list)

    class Rsync_options():
        @staticmethod
        def parser(some_list):
            options_pattern = r'^(-\w+|--[\w\-\=]+[\w\d\/\.\_]+)'
            password_pattern = r'-pass=.+'
            options = Parser.check_for_match(options_pattern, some_list)
            password = Parser.check_for_match(password_pattern, some_list)
            options = options.replace(password, '')
            return options

    class Password:
        @staticmethod
        def parser(some_list):
            pattern = r'-pass=.+'
            return Parser.check_for_match(pattern, some_list)


# Final
    class Local_directory:
        @staticmethod
        def parser(some_list):
            pattern = r'^/.+'
            return Parser.check_for_match(pattern, some_list)

# Final (Files have no digits in extentions)
    class Files:
        @staticmethod
        def parser(some_list):
            pattern = r'^[^-].+\.\D+'
            return Parser.check_for_match(pattern, some_list)

    @staticmethod
    def remote_stuff(some_list):
        pattern = r'^.+@.+'
        for element in some_list:
            remote = re.match(pattern, element)
            if remote:
                return element

# Final?!
    class Remote_user():
        @staticmethod
        def parser(some_list):
            pattern = r'^\w+[^\:\.\,]'
            remote_stuff = Parser.remote_stuff(some_list).split('@')
            user = re.match(pattern, remote_stuff[0])
            if user:
                return user.group(0)

# Final?!O_o
    class Remote_port:
        @staticmethod
        def parser(some_list):
            user = Parser.Remote_user.parser(some_list)
            remote_stuff = Parser.remote_stuff(some_list).split('@')
            port = remote_stuff[0].lstrip(user)
            if port:
                port = port.lstrip(':,.')
            return port

# Host may be ip-like
    class Remote_host:
        @staticmethod
        def parser(some_list):
            remote_stuff = Parser.remote_stuff(some_list).split('@')
            host_plus_dir = remote_stuff[1].split(':')
            return host_plus_dir[0]

    class Remote_directory:
        @staticmethod
        def parser(some_list):
            remote_stuff = Parser.remote_stuff(some_list).split('@')
            host_plus_dir = remote_stuff[1].split(':')
            if len(host_plus_dir) > 1:
                return host_plus_dir[1]
            else:
                return ''


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
        ParserResults.full_host = Parser.remote_stuff(ArgsReceiver.receiver())


# Validator class
class ValidateParams(object):
    @staticmethod
    def validator(ParsResult):
        pass


#Interface class
class Interface(object):

    @staticmethod
    @property
    def interface(params):
        pass


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
    print("full_host: {}".format(ParserResults.full_host))

    if ParserResults.port:
        cmd = "rsync {} {} \"ssh -p {}\" {}:{} {}".format(ParserResults.cli, ParserResults.files, ParserResults.port,
                                                          ParserResults.user, ParserResults.host, ParserResults.dist)
        print("Full rsync: {}".format(cmd))
    else:
        cmd = "rsync {} {} {}:{} {}".format(ParserResults.cli, ParserResults.files, ParserResults.user,
                                            ParserResults.host, ParserResults.dist)
        print("Full rsync: {}".format(cmd))

    # PIPE = subprocess.PIPE
    # p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT, close_fds=True)
    # print(p.stderr.read())
