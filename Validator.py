class ValidateParams(object):
    
    import platform, sys, os, subprocess

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
    def Check_local_os_version():   # Check local OS
        if platform.system() == "Linux":
            ValidateParams.Check_exists()   #Check does exist rsync on local machine
        else:
            print('Unfortunately, your OS is {}! Rsync works only with Unix-like systems'.format(platform.system()))
            sys.exit(1)

    @staticmethod
    def Check_exists(): #Check does exist rsync on local machine
        if subprocess.call('which rsync > /dev/null', shell=True) == 0:
            pass
        else:
            print("Unfortunately, rsync doesn't exist on your machine! Let's install it!")
            ValidateParams.Install_rsync()  #Install rsync on local machine

    @staticmethod
    def Install_rsync():    #Install rsync on local machine
        try:
            subprocess.call('apt-get install -y rsync > /dev/null || yum install -y rsync > /dev/null', shell=True)
            print("Rsync was successfully installed!")
        except:
            print("OOps..! Rsync wasn't installed on your machine! Please, check machine's configuration and try again!")    
   
    @staticmethod
    def Check_availability():
        if subprocess.call('ping -c1 {} > /dev/null'.format(ParserResults.host), shell=True) == 0:
            pass
        else:
            print('Remote host {} is not reachable!\nPlease, try again later'.format(ParserResults.host))
            sys.exit(1)

    @staticmethod
    def do_validator():
        ValidateParams.Source_files.validator()
        ValidateParams.Username.validator()
        ValidateParams.Remote_host.validator()
        ValidateParams.Check_local_os_version()
        ValidateParams.Check_availability()

ValidateParams.do_validator()
