import subprocess

class ArgsReceiver(object): # Получает аргументы от CLI
    pass


class ParserResults(object): # Класс глобальных переменных
    cli = ""
    password = ""
    files = ""
    name = ""
    port = ""
    host = ""
    dist = ""
    full_host = ""


class Parser(object): # Класс парсера с подклассами

    class ParserPassword(object):
        @staticmethod
        def parser(self, some_list):
            pass


    class ParserFiles(object):
        @staticmethod
        def parser(self, some_list):
            pass


class ValidateParams(object): # Класс валидатора
    @staticmethod
    def validator(ParsResult):
        pass


class Interface(object): # Класс и метод для доступа к скрипту снаружи

    @staticmethod
    @property
    def interface(params):
        pass


if "__name__" == "__main__":
    # Добавить проверку ОС

    cmd = "rsync {} {} {} {}".format(ParserResults.cli, ParserResults.files, ParserResults.full_host, ParserResults.dist)
    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT, close_fds=True)
    print(p.stdout.read())
