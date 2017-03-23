class ValidateParams(object):

    @staticmethod
    def Check_length(parametr, param_name):
        magic_number = 777
        try:
            magic_number / len(parametr)
            return parametr
        except:
            print('Unfortunately, you forgot define {}!\nFormat rsync function : rsync [OPTION] ... SRC ... [USER@] HOST:DEST \nPlease, try again'.format(param_name))
            sys.exit(1)

    class Source_files:
        @staticmethod
        def validator():
            return ValidateParams.Check_length(ParserResults.loc + ParserResults.files, "files")

    class Username:
        @staticmethod
        def validator():
            return ValidateParams.Check_length(ParserResults.user, "user")

    class Remote_host:
        @staticmethod
        def validator():
            return ValidateParams.Check_length(ParserResults.host, "host")

    @staticmethod
    def do_validator():
        ValidateParams.Source_files.validator()
        ValidateParams.Username.validator()
        ValidateParams.Remote_host.validator()


ValidateParams.do_validator()
