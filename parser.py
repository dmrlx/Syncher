from re import match as re_match
from os.path import isdir as path_isdir, isfile as path_isfile
from receiver import ArgsReceiver
from variables import ParserResults


class Parser(object):

    @staticmethod
    def execute(args):
        ParserResults.cli = Parser.options_parse(args)
        ParserResults.password = Parser.password_parse(args)
        ParserResults.dirs = Parser.dirs_parse(args)
        ParserResults.files = Parser.files_parse(args)
        ParserResults.user = Parser.rem_user_parse(args)
        ParserResults.port = Parser.rem_port_parse(args)
        ParserResults.host = Parser.rem_host_parse(args)
        ParserResults.dist = Parser.rem_dirs_parse(args)

    @staticmethod
    def check_for_match(pattern, some_list):
        match_list = []
        for element in some_list:
            match = re_match(pattern, element)
            if match:
                match_list.append(element)
        return " ".join(match_list)

    @staticmethod
    def options_parse(some_list):
        options_pattern = r'(^-\w+|^--[\w\-\=]+[\w\d\/\.\_]+|^[\'"].+[\'"]$)'
        password_pattern = r'-pass=.+'
        options = Parser.check_for_match(options_pattern, some_list)
        password = Parser.check_for_match(password_pattern, some_list)
        return options.replace(password, '')

    @staticmethod
    def password_parse(some_list):
        pattern = r'-pass=.+'
        return Parser.check_for_match(pattern, some_list).lstrip('-pass=')

    @staticmethod
    def pull_local_info(some_list):
        pattern = r'^[^-\'"].+'
        found = Parser.check_for_match(pattern, some_list)
        remote_info = Parser.pull_remote_info(some_list)
        return found.replace(remote_info, '')

    @staticmethod
    def dirs_parse(some_list):
        dirs = []
        for element in Parser.pull_local_info(some_list).split():
            if path_isdir(element):
                dirs.append(element)
        return " ".join(dirs)

    @staticmethod
    def files_parse(some_list):
        files = []
        for element in Parser.pull_local_info(some_list).split():
            if path_isfile(element):
                files.append(element)
        return " ".join(files)

    @staticmethod
    def pull_remote_info(some_list):
        pattern_full = r'^.+@.+'
        pattern_host = r'^.+:.*'
        for element in some_list:
            remote_full = re_match(pattern_full, element)
            remote_host = re_match(pattern_host, element)
            if remote_full:
                return element
            elif remote_host:
                return element
        return ''

    @staticmethod
    def rem_user_parse(some_list):
        pattern = r'^\w+[^\:\.\,\@]*'
        remote_info = Parser.pull_remote_info(some_list)
        if '@' in remote_info:
            user = re_match(pattern, remote_info)
            if user:
                return user.group()
        return ''

    @staticmethod
    def rem_port_parse(some_list):
        user = Parser.rem_user_parse(some_list)
        remote_info = Parser.pull_remote_info(some_list)
        if '@' in remote_info:
            remote_info = remote_info.split('@')
            port = remote_info[0].lstrip(user)
            if port:
                port = port.lstrip(':,.')
                return port
        return ''

    @staticmethod
    def rem_host_parse(some_list):
        remote_info = Parser.pull_remote_info(some_list)
        if '@' in remote_info:
            host_plus_dir = remote_info.split('@')[1].split(':')
            return host_plus_dir[0]
        else:
            host_plus_dir = remote_info.split(':')
            return host_plus_dir[0]

    @staticmethod
    def rem_dirs_parse(some_list):
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


if __name__ == "__main__":
# Пример вызова функции
    Parser.execute(ArgsReceiver.receiver())
    for attr in ['cli', 'password', 'dirs', 'files', 'user', 'port', 'host', 'dist']:
        print('{}: '.format(attr), end='')
        eval('print(ParserResults.{})'.format(attr))
