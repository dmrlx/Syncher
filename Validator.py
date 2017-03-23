class ValidateParams(object):       

    @staticmethod
    def Check_lenth(parametr):
        magic_number=777
        try:
            magic_number/len(parametr)
            return parametr
        except:
            print('Unfortunately, you forgot define {}!\nFormat rsync function : rsync [OPTION] ... SRC ... [USER@] HOST:DEST \nPlease, try again'.format(parametr))
            sys.exit(1)
            
    class Source_files:
        @staticmethod
        def validator():
            return ValidateParams.Check_lenth(Parser_Results.loc+Parser_Results.files)

    class Username:
        @staticmethod
        def validator():
            return ValidateParams.Check_lenth(Parser_Results.user)

    class Remote_host:
        @staticmethod
        def validator():
            return ValidateParams.Check_lenth(Parser_Results.host)

    @staticmethod
    def do_validator():
        ValidateParams.Source_files.validator()
        ValidateParams.Username.validator()
        ValidateParams.Remote_host.validator()


ValidateParams.do_validator()
