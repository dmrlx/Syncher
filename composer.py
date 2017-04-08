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
    def composer():
        cmd = "rsync "
        if ParserResults.port:
            ssh_param = "-e \"ssh -p {}\" ".format(ParserResults.port)
        else:
            ssh_param = ""

        if ParserResults.cli:
            cli_param = ParserResults.cli + " "
        else:
            cli_param = ""

        if ParserResults.dirs:
            loc_param = ParserResults.dirs + " "
        else:
            loc_param = ""

        if ParserResults.files:
            files_param = ParserResults.files + " "
        else:
            files_param = ""

        if ParserResults.dist:
            dist_param =  ParserResults.dist
        else:
            dist_param = ""

        return cmd + cli_param + ssh_param + loc_param + files_param + ParserResults.user + \
               "@" + ParserResults.host + " /" + dist_param


print(Composer.composer())