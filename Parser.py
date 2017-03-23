"""
import re
import sys


class ArgsReceiver:

    @staticmethod
    def receiver():
        options_list = ['-a', '-av', '--pass-file=/take.here', "-pass='111'"]
        dirs_list = ['/usr', '/usr/', 'host:/usr']
        files_list = ['45.123', 'qwer.ty', 'rte.']
        users_list = ['user:22@host:/usr']
        some_list = options_list + dirs_list + files_list + users_list
        return some_list


class Parser_Results:
    cli = ""
    password = ""
    loc = ""
    files = ""
    user = ""
    port = ""
    host = ""
    dist = ""
    full_host = ""

"""
class Parser(object):

    @staticmethod
    def check_for_match(pattern, some_list):
        match_list = []
        for element in some_list:
            match = re.match(pattern, element)
            if match:
                match_list.append(element)
        return " ".join(match_list)

    class Rsync_options:
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
    class Remote_user:
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

"""
class Throw_in:
    @staticmethod
    def parser_results():
        Parser_Results.cli = Parser.Rsync_options.parser(ArgsReceiver.receiver())
        Parser_Results.password = Parser.Password.parser(ArgsReceiver.receiver())
        Parser_Results.loc = Parser.Local_directory.parser(ArgsReceiver.receiver())
        Parser_Results.files = Parser.Files.parser(ArgsReceiver.receiver())
        Parser_Results.user = Parser.Remote_user.parser(ArgsReceiver.receiver())
        Parser_Results.port = Parser.Remote_port.parser(ArgsReceiver.receiver())
        Parser_Results.host = Parser.Remote_host.parser(ArgsReceiver.receiver())
        Parser_Results.dist = Parser.Remote_directory.parser(ArgsReceiver.receiver())
        Parser_Results.full_host = Parser.remote_stuff(ArgsReceiver.receiver())


Throw_in.parser_results()
print(sys.version)
print(Parser_Results.cli)
print(Parser_Results.password)
print(Parser_Results.loc)
print(Parser_Results.files)
print(Parser_Results.user)
print(Parser_Results.port)
print(Parser_Results.host)
print(Parser_Results.dist)
print(Parser_Results.full_host)
"""
