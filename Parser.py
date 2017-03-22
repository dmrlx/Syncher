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


class ParserResults(object):
    cli = ""
    password = ""
    files = ""
    user = ""
    port = ""
    host = ""
    dist = ""
    full_host = ""


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
            pattern = r'^(-\w+|--[\w\-\=]+/[\w\d\/\.]+)'
            return Parser.check_for_match(pattern, some_list)

    class Local_directory:
        @staticmethod
        def parser(some_list):
            pattern = r'^/.+'
            return Parser.check_for_match(pattern, some_list)

    class Files:
        @staticmethod
        def parser(some_list):
            pattern = r'^[^-].+\..+'
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
            remote_stuff = Parser.remote_stuff(some_list)
            user_plus_port = remote_stuff[0].split(':')
            return user_plus_port[0]

    class Remote_port:
        @staticmethod
        def parser(some_list):
            remote_stuff = Parser.remote_stuff(some_list)
            user_plus_port = remote_stuff[0].split(':')
            if len(user_plus_port) > 1:
                return user_plus_port[1]
            else:
                return ''

    class Remote_host:
        @staticmethod
        def parser(some_list):
            remote_stuff = Parser.remote_stuff(some_list)
            host_plus_dir = remote_stuff[1].split(':,.')
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

    ParserResults.cli = Rsync_options.parser(ArgsReceiver.receiver)
    ParserResults.password = 'something'
    ParserResults.files = Files.parser(ArgsReceiver.receiver)
    ParserResults.name = Remote_user.parser(ArgsReceiver.receiver)
    ParserResults.port = Remote_port.parcer(ArgsReceiver.receiver)
    ParserResults.host = Remote_host.parser(ArgsReceiver.receiver)
    ParserResults.dist = Remote_directory.parser(ArgsReceiver.receiver)
    ParserResults.full_host = remote_stuff(ArgsReceiver.receiver)


print(sys.version)
print(ParserResults.cli)
print(ParserResults.files)
print(ParserResults.user)
print(ParserResults.port)
print(ParserResults.host)
print(ParserResults.dist)
print(ParserResults.full_host)
