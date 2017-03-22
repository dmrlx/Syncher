class Parser(object):


# Я так понял, в этих опциях будут и пароли тоже - в виде --password-file=...
    class Rsync_options():
        @staticmethod
        def do(some_list):
            pattern = r'-\w+|--.+'
            options = []
            for element in some_list:
                option = re.match(pattern, element)
                if option:
                    options.append(option)
                    return ' '.join(options)

    class Directory():
        @staticmethod
        def do(some_list):
            pattern = r'/.+'
            directories = []
            for element in some_list:
                directory = re.match(pattern, element)
                if file:
                    directories.append(directory.group(0))
            return ' '.join(directories)

    class Files_without_star():
        @staticmethod
        def do(some_list):
            pattern = r'.+\..+'
            files = []
            for element in some_list:
                file = re.match(pattern, element)
                if file:
                    files.append(file.group(0))
            return ' '.join(files)


import re

print(Parser.Files_without_star.do(['45.123', 'qwer.ty', 'rte.']))
