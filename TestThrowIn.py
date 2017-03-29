import re
import unittest
import TestParser as module

class Results(module.ParserResults):
    pass

class TestThrowIn(unittest.TestCase):
    def test_parser_results(self):
        args = module.ArgsReceiver.receiver()
        self.assertIsInstance(args, list)
        self.assertNotEqual(len(args), 0)
        Results.cli = module.TestParser.TestOptions.test_parser(args)
        self.assertIsInstance(Results.cli, str)
        Results.password = module.TestParser.TestPassword.test_parser(args)
        self.assertIsInstance(Results.password, str)
        Results.dirs_and_files = module.TestParser.TestDirsAndFiles.test_parser(args)
        self.assertIsInstance(Results.dirs_and_files, str)
        Results.user = module.TestParser.TestRemoteUser.test_parser(args)
        self.assertIsInstance(Results.user, str)
        Results.port = module.TestParser.TestRemotePort.test_parser(args)
        self.assertIsInstance(Results.port, str)
        Results.host = module.TestParser.TestRemoteHost.test_parser(args)
        self.assertIsInstance(Results.host, str)
        Results.dist = module.TestParser.TestRemoteDirectory.test_parser(args)
        self.assertIsInstance(Results.dist, str)

if __name__ == '__main__':
    unittest.main()