class ArgsReceiver(object): # Получает аргументы от CLI
    return result


class ParserResults(object): # Класс глобальных переменных
    cli = ""
    password = ""
    files = []
    host = ""


class Parser(object): # Класс парсера с подклассами
    class ParserPassword(object):
        def parser(self, some_list):
            return result

    class ParserFiles(object):
        def parser(self, some_list):
            return result


class ValidateParams(object): # Класс валидатора
    def validator(self, ParsResult):
        return result


class Interface(object): # Класс и метод для доступа к скрипту снаружи

    @property
    def interface(params):

