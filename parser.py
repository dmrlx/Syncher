import re


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

class Parser(object):

    @staticmethod
    def execute():
        ParserResults.cli = Parser.options_parse(ArgsReceiver.receiver())
        ParserResults.password = Parser.password_parse(ArgsReceiver.receiver())
        ParserResults.dirs_and_files = Parser.loc_dirs_and_files_parse(ArgsReceiver.receiver())
        ParserResults.user = Parser.rem_user_parse(ArgsReceiver.receiver())
        ParserResults.port = Parser.rem_port_parse(ArgsReceiver.receiver())
        ParserResults.host = Parser.rem_host_parse(ArgsReceiver.receiver())
        ParserResults.dist = Parser.rem_dirs_and_files_parse(ArgsReceiver.receiver())

    @staticmethod
    def check_for_match(pattern, some_list):
        match_list = []
        for element in some_list:
            match = re.match(pattern, element)
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
        return Parser.check_for_match(pattern, some_list)

    @staticmethod
    def loc_dirs_and_files_parse(some_list):
        pattern = r'^[^-\'"].+'
        found = Parser.check_for_match(pattern, some_list)
        remote_info = Parser.pull_remote_info(some_list)
        return found.replace(remote_info, '')

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

    @staticmethod
    def rem_user_parse(some_list):
        pattern = r'^\w+[^\:\.\,\@]*'
        remote_info = Parser.pull_remote_info(some_list)
        if '@' in remote_info:
            user = re.match(pattern, remote_info)
            if user:
                return user.group(0)
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
    def rem_dirs_and_files_parse(some_list):
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

Parser.execute()
print('options:{}'.format(ParserResults.cli))
print('password:{}'.format(ParserResults.password))
print('dir\'s & files :{}'.format(ParserResults.dirs_and_files))
print('user:{}'.format(ParserResults.user))
print('port:{}'.format(ParserResults.port))
print('host:{}'.format(ParserResults.host))
print('dist_dir:{}'.format(ParserResults.dist))
