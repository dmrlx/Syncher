import re
import sys


class Args:
    @staticmethod
    def receiver():
        first_list = ['-a', '-av', '--pass-file=/take.here', "-pass='111'",
                    '/usr', '/usr/', '45.123', 'qwer.ty', 'e.t', 'word*',
                    'user.13@host:/usr']
        some_list = ['-t', '*.c', 'foo:/ps']
        return some_list


class ParserResults:
    cli = ""
    password = ""
    loc = ""
    files = ""
    user = ""
    port = ""
    host = ""
    dist = ""


class Parser(object):

    @staticmethod
    def check_for_match(pattern, some_list):
        match_list = []
        for element in some_list:
            match = re.match(pattern, element)
            if match or match is not None:
                match_list.append(element)
        return " ".join(match_list)

    class Options:
        @staticmethod
        def parser(some_list):
            options_pattern = r'^(-\w+|--[\w\-\=]+[\w\d\/\.\_]+)'
            password_pattern = r'-pass=.+'
            options = Parser.check_for_match(options_pattern, some_list)
            password = Parser.check_for_match(password_pattern, some_list)
            return options.replace(password, '')

    class Password:
        @staticmethod
        def parser(some_list):
            pattern = r'-pass=.+'
            return Parser.check_for_match(pattern, some_list)

    class LocalDirectory:
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

# Can be no user nor host at all (checked)
    @staticmethod
    def remote_stuff(some_list):
        pattern_full = r'^.+@.+'
        pattern_host = r'^.+:.*'
        for element in some_list:
            remote_full = re.match(pattern_full, element)
            remote_host = re.match(pattern_host, element)
            if remote_full or remote_full is not None:
                return element
            elif remote_host or remote_host is not None:
                return element
        return ''

    class RemoteUser:
        @staticmethod
        def parser(some_list):
            pattern = r'^\w+[^\:\.\,]*'
            remote_stuff = Parser.remote_stuff(some_list)
            if '@' in remote_stuff:
                user = re.match(pattern, remote_stuff)
                if user or user is not None:
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
                if port or port is not None:
                    port = port.lstrip(':,.')
                return port
            return ''

# Host may be ip-like (i think)
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


class ThrowIn:
    @staticmethod
    def parser_results():
        Parser_Results.cli = Parser.Options.parser(Args.receiver())
        Parser_Results.password = Parser.Password.parser(Args.receiver())
        Parser_Results.loc = Parser.LocalDirectory.parser(Args.receiver())
        Parser_Results.files = Parser.Files.parser(Args.receiver())
        Parser_Results.user = Parser.RemoteUser.parser(Args.receiver())
        Parser_Results.port = Parser.RemotePort.parser(Args.receiver())
        Parser_Results.host = Parser.RemoteHost.parser(Args.receiver())
        Parser_Results.dist = Parser.RemoteDirectory.parser(Args.receiver())


ThrowIn.parser_results()
print(sys.version)
print('options: ', ParserResults.cli)
print('password', ParserResults.password)
print('loc_dir: ', ParserResults.loc)
print('files: ', ParserResults.files)
print('user: ', ParserResults.user)
print('port: ', ParserResults.port)
print('host: ', ParserResults.host)
print('dist_dir: ', ParserResults.dist)
