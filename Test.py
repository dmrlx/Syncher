import re
import unittest

class Args():
    @staticmethod
    def receive():
        first_list = ['-a', "'ssh -P -i'", "'-e ssh -P -i'", '--pass-file=/take.here',
                      "-pass='111'", './123', './1*', '/usr', '/usr/word*', '45.123', 'qwer.ty', 'e.t',
                      'user@host:/usr']
        some_list = ['-t', '*.c', 'foo:/ps', "'-e ssh -P -i'"]
        return first_list

class Results():
    cli = ""
    password = ""
    dirs_and_files = ""
    user = ""
    port = ""
    host = ""
    dist = ""

class Parser(unittest.TestCase):

    def setUp(self):
        self.test_execute()

    def test_execute(self):
        args = Args.receive()
        self.assertIsInstance(args, list)
        self.assertNotEqual(len(args), 0)
        Results.cli = self.options_parse(self, args)
        self.assertIsInstance(Results.cli, str)
        Results.password = self.password_parse(self, args)
        self.assertIsInstance(Results.password, str)
        Results.dirs_and_files = self.loc_dirs_and_files_parse(self, args)
        self.assertIsInstance(Results.dirs_and_files, str)
        Results.user = self.rem_user_parse(self, args)
        self.assertIsInstance(Results.user, str)
        Results.port = self.rem_port_parse(self, args)
        self.assertIsInstance(Results.port, str)
        Results.host = self.rem_host_parse(self, args)
        self.assertIsInstance(Results.host, str)
        Results.dist = self.rem_dirs_and_files_parse(self, args)
        self.assertIsInstance(Results.dist, str)

    @staticmethod
    def check_for_match(self, pattern, some_list):
        match_list = []
        for element in some_list:
            self.assertIsInstance(element, str)
            match = re.match(pattern, element)
            if match:
                match_list.append(element)
        return " ".join(match_list)

    @staticmethod
    def pull_remote_info(self, some_list):
        pattern_full = r'^.+@.+'
        pattern_host = r'^.+:.*'
        for element in some_list:
            self.assertIsInstance(element, str)
            remote_full = re.match(pattern_full, element)
            remote_host = re.match(pattern_host, element)
            if remote_full:
                return element
            elif remote_host:
                return element
        return ''

    @staticmethod
    def options_parse(self, some_list):
        options_pattern = r'(^-\w+|^--[\w\-\=]+[\w\d\/\.\_]+|^[\'"].+[\'"]$)'
        password_pattern = r'-pass=.+'
        options = self.check_for_match(self, options_pattern, some_list)
        password = self.check_for_match(self, password_pattern, some_list)
        return options.replace(password, '')

    @staticmethod
    def password_parse(self, some_list):
        pattern = r'-pass=.+'
        return self.check_for_match(self, pattern, some_list)

    @staticmethod
    def loc_dirs_and_files_parse(self, some_list):
        pattern = r'^[^-\'"].+'
        found = self.check_for_match(self, pattern, some_list)
        remote_info = self.pull_remote_info(self, some_list)
        return found.replace(remote_info, '')

    @staticmethod
    def rem_user_parse(self, some_list):
        pattern = r'^\w+[^\:\.\,\@]*'
        remote_info = self.pull_remote_info(self, some_list)
        self.assertIsInstance(remote_info, str)
        if '@' in remote_info:
            user = re.match(pattern, remote_info)
            if user:
                return user.group(0)
        return ''

    @staticmethod
    def rem_port_parse(self, some_list):
        user = self.rem_user_parse(self, some_list)
        self.assertIsInstance(user, str)
        remote_info = self.pull_remote_info(self, some_list)
        self.assertIsInstance(remote_info, str)
        if '@' in remote_info:
            remote_info = remote_info.split('@')
            port = remote_info[0].lstrip(user)
            if port:
                port = port.lstrip(':,.')
                return port
        return ''

    @staticmethod
    def rem_host_parse(self, some_list):
        remote_info = self.pull_remote_info(self, some_list)
        self.assertIsInstance(remote_info, str)
        if '@' in remote_info:
            host_plus_dir = remote_info.split('@')[1].split(':')
            return host_plus_dir[0]
        else:
            host_plus_dir = remote_info.split(':')
            return host_plus_dir[0]

    @staticmethod
    def rem_dirs_and_files_parse(self, some_list):
        remote_info = self.pull_remote_info(self, some_list)
        self.assertIsInstance(remote_info, str)
        if '@' in remote_info:
            host_plus_dir = remote_info.split('@')[1].split(':')
            if len(host_plus_dir) > 1:
                return host_plus_dir[1]
        else:
            host_plus_dir = remote_info.split(':')
            if len(host_plus_dir) > 1:
                return host_plus_dir[1]
            return ''

if __name__ == '__main__':
    unittest.main()