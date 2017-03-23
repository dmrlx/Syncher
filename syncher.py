import subprocess
import ArgsReceiver

# Class-receiver
#class ArgsReceiver(object): 
#    pass


# Class of global vars
class ParserResults(object): 
    cli = ""
    password = ""
    loc = ""
    files = ""
    name = ""
    port = ""
    host = ""
    dist = ""
    full_host = ""


#Parser Class
class Parser(object):

    class ParserPassword(object):
        @staticmethod
        def parser(self, some_list):
            pass


    class ParserFiles(object):
        @staticmethod
        def parser(self, some_list):
            pass


#Class which update global vars
class Throw_in(object):
    @staticmethod
    def parser_results():
        Parser_Results.cli = Parser.Rsync_options.parser(ArgsReceiver.receiver())
        Parser_Results.password = Parser.Password.parser(ArgsReceiver.receiver())
        Parser_Results.loc = Parser.Local_directory.parser(ArgsReceiver.receiver())
        Parser_Results.files = Parser.Files.parser(ArgsReceiver.receiver())
        Parser_Results.user = Parser.Remote_user.parser(ArgsReceiver.receiver())
        Parser_Results.port = Parser.Remote_port.parser(ArgsReceiver.receiver())
        Parser_Results.host = Parser.Remote_host.parser(ArgsReceiver.receiver())
        Parser_Results.dist = Parser.Remote_directory.parser(ArgsReceiver.receiver())
        Parser_Results.full_host = Parser.remote_stuff(ArgsReceiver.receiver())


# Validator class
class ValidateParams(object):
    @staticmethod
    def validator(ParsResult):
        pass


#Interface class
class Interface(object):

    @staticmethod
    @property
    def interface(params):
        pass


if "__name__" == "__main__":
    # Add OS check

    cmd = "rsync {} {} {} {}".format(ParserResults.cli, ParserResults.files, ParserResults.full_host, ParserResults.dist)
    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT, close_fds=True)
    print(p.stderr.read())
