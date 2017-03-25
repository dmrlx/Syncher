#vars for tests
"""class ParserResults(object):
    cli = "-u"
    password = "000"
    loc = "/usr"
    files = ""
    user = "root"
    port = "22"
    host = "host"
    dist = "hgh"""""


class Composer(object):
    @staticmethod
    def composer():
        cmd = "rsync "
        if ParserResults.port:
            ssh_param = "-e \"ssh -p {}\" ".format(ParserResults.port)
        else:
            ssh_param = "ssh "

        if ParserResults.loc:
            loc_param = ParserResults.loc
        else:
            loc_param = ""

        if ParserResults.files:
            files_param = ParserResults.files
        else:
            files_param = ""

        if ParserResults.dist:
            dist_param = ":" + ParserResults.dist
        else:
            dist_param = ""

        return cmd + ssh_param + loc_param + files_param + " " + ParserResults.user + "@" + ParserResults.host + dist_param


print(Composer.composer())
