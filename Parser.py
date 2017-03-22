import re
import sys


class ArgsReceiver:

    @staticmethod
    def receiver():
        options_list = ['-a', '-av', '--password-file=/root/pswds/take.here']
        dirs_list = ['/usr', '/usr/', 'host:/usr']
        files_list = ['45.123', 'qwer.ty', 'rte.']
        users_list = ['user:22@host:/usr']
        some_list = options_list + dirs_list + files_list + users_list
        return some_list


class Parser_Results:
    cli = ""
    password = ""
    files = ""
    user = ""
    port = ""
    host = ""
    dist = ""
    full_host = ""


class Parser:

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
            pattern = r'^(-\w+|--[\w\-\=]+[\w\d\/\.\_]+)'
            return Parser.check_for_match(pattern, some_list)

    class Local_directory:
        @staticmethod
        def parser(some_list):
            pattern = r'^/.+'
            return Parser.check_for_match(pattern, some_list)

    class Files:
        @staticmethod
        def parser(some_list):
            pattern = r'^[^-].+\.[^@].+'
            return Parser.check_for_match(pattern, some_list)

    @staticmethod
    def remote_stuff(some_list):
        pattern = r'^.+@.+'
        for element in some_list:
            remote = re.match(pattern, element)
            if remote:
                return element.split('@')

    class Remote_user:
        @staticmethod
        def parser(some_list):
            pattern = r'^\w+[\:\.\,]'
            remote_stuff = Parser.remote_stuff(some_list)
            if : in remote_stuff[0]:
                print('yes')
            user = re.match(pattern, remote_stuff[0])
            print(user)
            if user:
                return user.group(0)

    class Remote_port:
        @staticmethod
        def parser(some_list):
            pattern = r'\d+'
            remote_stuff = Parser.remote_stuff(some_list)
            port = re.match(pattern, remote_stuff[0])
            print(port)
            if port:
                return port.group(0)

    class Remote_host:
        @staticmethod
        def parser(some_list):
            remote_stuff = Parser.remote_stuff(some_list)
            host_plus_dir = remote_stuff[1].split(':')
            return host_plus_dir[0]

    class Remote_directory:
        @staticmethod
        def parser(some_list):
            remote_stuff = Parser.remote_stuff(some_list)
            host_plus_dir = remote_stuff[1].split(':')
            if len(host_plus_dir) > 1:
                return host_plus_dir[1]
            else:
                return ''

class Give:
    @staticmethod
    def parsing():
        Parser_Results.cli = Parser.Rsync_options.parser(ArgsReceiver.receiver())
        Parser_Results.password = 'something'
        Parser_Results.files = Parser.Files.parser(ArgsReceiver.receiver())
        Parser_Results.user = Parser.Remote_user.parser(ArgsReceiver.receiver())
        Parser_Results.port = Parser.Remote_port.parser(ArgsReceiver.receiver())
        Parser_Results.host = Parser.Remote_host.parser(ArgsReceiver.receiver())
        Parser_Results.dist = Parser.Remote_directory.parser(ArgsReceiver.receiver())
        Parser_Results.full_host = Parser.remote_stuff(ArgsReceiver.receiver())


Give.parsing()
print(sys.version)
print(Parser_Results.cli)
print(Parser_Results.files)
print(Parser_Results.user)
print(Parser_Results.port)
print(Parser_Results.host)
print(Parser_Results.dist)
print(Parser_Results.full_host)
