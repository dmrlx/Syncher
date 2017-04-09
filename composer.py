# vars for tests
# class ParserResults(object):
#     cli = "-r"
#     password = "000"
#     dirs = "/usr"
#     files = "jkhdkjh"
#     user = "root"
#     port = "22"
#     host = "host"
#     dist = "hgh"

from variables import ParserResults

class Composer(object):
    @staticmethod
    def composer(parser_results=ParserResults):
        cmd = "rsync "
        if parser_results.port:
            ssh_param = "-e \"ssh -p {}\" ".format(parser_results.port)
        else:
            ssh_param = ""

        if parser_results.cli:
            cli_param = parser_results.cli + " "
        else:
            cli_param = ""

        if parser_results.dirs:
            loc_param = parser_results.dirs + " "
        else:
            loc_param = ""

        if parser_results.files:
            files_param = parser_results.files + " "
        else:
            files_param = ""

        if parser_results.dist:
            dist_param =  parser_results.dist
        else:
            dist_param = ""

        return cmd + cli_param + ssh_param + loc_param + files_param + parser_results.user + \
               "@" + parser_results.host + ":" + dist_param


# print(Composer.composer())
