# vars for tests
class ParserResults(object):
    cli = "-r"
    password = "000"
    dirs_and_files = "ijeiejfie"
    user = "root"
    port = "22"
    host = "host"
    dist = "hgh"
    pass_file = ""


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

        if ParserResults.dirs_and_files:
            dirs_and_files_param = ParserResults.dirs_and_files + " "
            cli_param += "-r "
        else:
            dirs_and_files_param = ""

        if ParserResults.dist:
            dist_param = ParserResults.dist
        else:
            dist_param = ""

        if ParserResults.pass_file:
            pass_file_param = "--password-file={} ".format(ParserResults.pass_file)
        else:
            pass_file_param = ""

        return cmd + cli_param + ssh_param + dirs_and_files_param + pass_file_param + ParserResults.user + "@" +\
               ParserResults.host + ":" + dist_param


print(Composer.composer())
