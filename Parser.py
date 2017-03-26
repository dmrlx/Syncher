import re
import sys


class ArgsReceiver:
    @staticmethod
    def receiver():
        first_list = ['-a', "'ssh -P -i'", "'-e ssh -P -i'", '--pass-file=/take.here',
                      "-pass='111'", './123', './1*', '/usr', '/usr/word*', '45.123', 'qwer.ty', 'e.t',
                      'user@host:/usr']
        some_list = ['-t', '*.c', 'foo:/ps', "'-e ssh -P -i'"]
        return first_list


class ParserResults(object):
    cli = ""
    password = ""
    dirs_and_files = ""
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
                print(user)
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


class ThrowIn(object):

    @staticmethod
    def parser_results():
        ParserResults.cli = Parser.Options.parser(ArgsReceiver.receiver())
        ParserResults.password = Parser.Password.parser(ArgsReceiver.receiver())
        ParserResults.dirs_and_files = Parser.DirsAndFiles.parser(ArgsReceiver.receiver())
        ParserResults.user = Parser.RemoteUser.parser(ArgsReceiver.receiver())
        ParserResults.port = Parser.RemotePort.parser(ArgsReceiver.receiver())
        ParserResults.host = Parser.RemoteHost.parser(ArgsReceiver.receiver())
        ParserResults.dist = Parser.RemoteDirectory.parser(ArgsReceiver.receiver())


ThrowIn.parser_results()
print(sys.version)
print('options:{}'.format(ParserResults.cli))
print('password:{}'.format(ParserResults.password))
print('dir\'s & files :{}'.format(ParserResults.dirs_and_files))
print('user:{}'.format(ParserResults.user))
print('port:{}'.format(ParserResults.port))
print('host:{}'.format(ParserResults.host))
print('dist_dir:{}'.format(ParserResults.dist))
