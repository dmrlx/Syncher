import re
import unittest
from Parser import ParserResults, ArgsReceiver

class TestParser(unittest.TestCase):
    @staticmethod
    def test_check_for_match(pattern, some_list):
        match_list = []
        for element in some_list:
            TestParser.assertIsInstance(TestParser, element, str)
            match = re.match(pattern, element)
            if match:
                match_list.append(element)
        return " ".join(match_list)

    @staticmethod
    def test_remote_stuff(some_list):
        pattern_full = r'^.+@.+'
        pattern_host = r'^.+:.*'
        for element in some_list:
            TestParser.assertIsInstance(TestParser, element, str)
            remote_full = re.match(pattern_full, element)
            remote_host = re.match(pattern_host, element)
            if remote_full:
                return element
            elif remote_host:
                return element
        return ''

    class TestOptions(unittest.TestCase):
        @staticmethod
        def test_parser(some_list):
            options_pattern = r'(^-\w+|^--[\w\-\=]+[\w\d\/\.\_]+|^[\'"].+[\'"]$)'
            password_pattern = r'-pass=.+'
            options = TestParser.test_check_for_match(options_pattern, some_list)
            password = TestParser.test_check_for_match(password_pattern, some_list)
            return options.replace(password, '')
            
    class TestPassword(unittest.TestCase):
        @staticmethod
        def test_parser(some_list):
            pattern = r'-pass=.+'
            return TestParser.test_check_for_match(pattern, some_list)

    class TestDirsAndFiles(unittest.TestCase):
        @staticmethod
        def test_parser(some_list):
            pattern = r'^[^-\'"].+'
            found = TestParser.test_check_for_match(pattern, some_list)
            remote_stuff = TestParser.test_remote_stuff(some_list)
            return found.replace(remote_stuff, '')

    class TestRemoteUser(unittest.TestCase):
        @staticmethod
        def test_parser(some_list):
            pattern = r'^\w+[^\:\.\,\@]*'
            remote_stuff = TestParser.test_remote_stuff(some_list)
            TestParser.assertIsInstance(TestParser, remote_stuff, str)
            if '@' in remote_stuff:
                user = re.match(pattern, remote_stuff)
                if user:
                    return user.group(0)
            return ''

    class TestRemotePort(unittest.TestCase):
        @staticmethod
        def test_parser(some_list):
            user = TestParser.TestRemoteUser.test_parser(some_list)
            remote_stuff = TestParser.test_remote_stuff(some_list)
            TestParser.assertIsInstance(TestParser, remote_stuff, str)
            if '@' in remote_stuff:
                remote_stuff = remote_stuff.split('@')
                port = remote_stuff[0].lstrip(user)
                if port:
                    port = port.lstrip(':,.')
                    return port
            return ''


    class TestRemoteHost(unittest.TestCase):
        @staticmethod
        def test_parser(some_list):
            remote_stuff = TestParser.test_remote_stuff(some_list)
            TestParser.assertIsInstance(TestParser, remote_stuff, str)
            if '@' in remote_stuff:
                host_plus_dir = remote_stuff.split('@')[1].split(':')
                return host_plus_dir[0]
            else:
                host_plus_dir = remote_stuff.split(':')
                return host_plus_dir[0]

    class TestRemoteDirectory(unittest.TestCase):
        @staticmethod
        def test_parser(some_list):
            remote_stuff = TestParser.test_remote_stuff(some_list)
            TestParser.assertIsInstance(TestParser, remote_stuff, str)
            if '@' in remote_stuff:
                host_plus_dir = remote_stuff.split('@')[1].split(':')
                if len(host_plus_dir) > 1:
                    return host_plus_dir[1]
            else:
                host_plus_dir = remote_stuff.split(':')
                if len(host_plus_dir) > 1:
                    return host_plus_dir[1]
                return ''

if __name__ == '__main__':
    unittest.main()