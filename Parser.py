"""
import re
import sys


class ArgsReceiver():
    @staticmethod
    def receiver():
        first_list = ['-a', "'ssh -P -i'", "'-e ssh -P -i'", '--pass-file=/take.here',
                      "-pass='111'", './123', './1*', '/usr', '/usr/word*', '45.123', 'qwer.ty', 'e.t',
                      'user@host:/usr']
        some_list = ['-t', '*.c', 'foo:/ps', "'-e ssh -P -i'"]
        return first_list


class ParserResults():
    cli = ""
    password = ""
    dirs_and_files = ""
    user = ""
    port = ""
    host = ""
    dist = ""
"""
class Parser(object):

    def execute(self):
        ParserResults.cli = self.Options.parse(ArgsReceiver.receiver())
        ParserResults.password = self.Password.parse(ArgsReceiver.receiver())
        ParserResults.dirs_and_files = self.DirsAndFiles.parse(ArgsReceiver.receiver())
        ParserResults.user = self.RemoteUser.parse(ArgsReceiver.receiver())
        ParserResults.port = self.RemotePort.parse(ArgsReceiver.receiver())
        ParserResults.host = self.RemoteHost.parse(ArgsReceiver.receiver())
        ParserResults.dist = self.RemoteDirectory.parse(ArgsReceiver.receiver())

    @staticmethod
    def check_for_match(pattern, some_list):
        match_list = []
        for element in some_list:
            match = re.match(pattern, element)
            if match:
                match_list.append(element)
        return " ".join(match_list)

    class Options():
        @staticmethod
        def parse(some_list):
            options_pattern = r'(^-\w+|^--[\w\-\=]+[\w\d\/\.\_]+|^[\'"].+[\'"]$)'
            password_pattern = r'-pass=.+'
            options = Parser.check_for_match(options_pattern, some_list)
            password = Parser.check_for_match(password_pattern, some_list)
            return options.replace(password, '')

    class Password():
        @staticmethod
        def parse(some_list):
            pattern = r'-pass=.+'
            return Parser.check_for_match(pattern, some_list)

    class DirsAndFiles():
        @staticmethod
        def parse(some_list):
            pattern = r'^[^-\'"].+'
            found = Parser.check_for_match(pattern, some_list)
            pull_remote_info = Parser.pull_remote_info(some_list)
            return found.replace(pull_remote_info, '')

    @staticmethod
    def pull_remote_info(some_list):
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

    class RemoteUser():
        @staticmethod
        def parse(some_list):
            pattern = r'^\w+[^\:\.\,\@]*'
            remote_info = Parser.pull_remote_info(some_list)
            if '@' in remote_info:
                user = re.match(pattern, remote_info)
                if user:
                    return user.group(0)
            return ''

    class RemotePort():
        @staticmethod
        def parse(some_list):
            user = Parser.RemoteUser.parse(some_list)
            remote_info = Parser.pull_remote_info(some_list)
            if '@' in remote_info:
                remote_info = remote_info.split('@')
                port = remote_info[0].lstrip(user)
                if port:
                    port = port.lstrip(':,.')
                    return port
            return ''

    class RemoteHost():
        @staticmethod
        def parse(some_list):
            remote_info = Parser.pull_remote_info(some_list)
            if '@' in remote_info:
                host_plus_dir = remote_info.split('@')[1].split(':')
                return host_plus_dir[0]
            else:
                host_plus_dir = remote_info.split(':')
                return host_plus_dir[0]

    class RemoteDirectory():
        @staticmethod
        def parse(some_list):
            remote_info = Parser.pull_remote_info(some_list)
            if '@' in remote_info:
                host_plus_dir = remote_info.split('@')[1].split(':')
                if len(host_plus_dir) > 1:
                    return host_plus_dir[1]
            else:
                host_plus_dir = remote_info.split(':')
                if len(host_plus_dir) > 1:
                    return host_plus_dir[1]
                return ''
"""
Parser().execute()
print('options:{}'.format(ParserResults.cli))
print('password:{}'.format(ParserResults.password))
print('dir\'s & files :{}'.format(ParserResults.dirs_and_files))
print('user:{}'.format(ParserResults.user))
print('port:{}'.format(ParserResults.port))
print('host:{}'.format(ParserResults.host))
print('dist_dir:{}'.format(ParserResults.dist))
"""
