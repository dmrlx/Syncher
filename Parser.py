class Parser(object):

    @staticmethod
    def check_for_match(pattern, some_list):
        match_list = []
        for element in some_list:
            match = re.match(pattern, element)
            if match:
                match_list.append(element)
        return match_list

# Я так понял, в этих опциях будут и пароли тоже - в виде --password-file=...
    class Rsync_options():
        @staticmethod
        def do(some_list):
            pattern = r'^(-\w+|--[\w\-\=]+/[\w\d\/\.]+)'
            return Parser.check_for_match(pattern, some_list)

    class Local_directory():
        @staticmethod
        def do(some_list):
            pattern = r'^/.+'
            return Parser.check_for_match(pattern, some_list)

    class Files_without_star():
        @staticmethod
        def do(some_list):
            pattern = r'^[^-].+\..+'
            return Parser.check_for_match(pattern, some_list)

    @staticmethod
    def remote_stuff(some_list):
        pattern = r'^.+@.+'
        for element in some_list:
            remote = re.match(pattern, element)
            if remote:
                return element.split('@')


    class Remote_user():
        @staticmethod
        def do(some_list):
            remote_stuff = Parser.remote_stuff(some_list)
            user_plus_port = remote_stuff[0].split(':')
            return user_plus_port[0]

    class Remote_port():
        @staticmethod
        def do(some_list):
            remote_stuff = Parser.remote_stuff(some_list)
            user_plus_port = remote_stuff[0].split(':')
            if len(user_plus_port) > 1:
                return user_plus_port[1]
            else: return ''

    class Remote_host():
        @staticmethod
        def do(some_list):
            remote_stuff = Parser.remote_stuff(some_list)
            host_plus_dir = remote_stuff[1].split(':')
            return host_plus_dir[0]

    class Remote_directory():
        @staticmethod
        def do(some_list):
            remote_stuff = Parser.remote_stuff(some_list)
            host_plus_dir = remote_stuff[1].split(':')
            if len(host_plus_dir) > 1:
                return host_plus_dir[1]
            else: return ''

"""
import re
import sys

print(sys.version)
options_list = ['-a', '-av', '--password-file=/root/pswds/take.here']
dirs_list = ['/usr', '/usr/', 'host:/usr']
files_list = ['45.123', 'qwer.ty', 'rte.']
users_list = ['user:22@host:/usr']
some_list = options_list + dirs_list + files_list + users_list
print(Parser.Rsync_options.do(some_list))
print(Parser.Local_directory.do(some_list))
print(Parser.Files_without_star.do(some_list))
print(Parser.Remote_user.do(some_list))
print(Parser.Remote_port.do(some_list))
print(Parser.Remote_host.do(some_list))
print(Parser.Remote_directory.do(some_list))
"""
