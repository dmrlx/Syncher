import platform, sys, os, subprocess, paramiko

class ValidateParams(object):

    @staticmethod
    def check_length(parametr, param_name):
        magic_number = 777
        try:
            magic_number / len(parametr)
            return parametr
            #return True
        except:
            print('Unfortunately, you forgot define {}!\nFormat rsync function : rsync [OPTION] ... SRC ... [USER@] HOST:DEST \nPlease, try again'.format(param_name))
            sys.exit(1)
            #return False

    class SourceFiles(object):
        @staticmethod
        def validator():
            return ValidateParams.check_length(syncherVariables.dirs + syncherVariables.files, "files")

    class Username(object):
        @staticmethod
        def validator():
            return ValidateParams.check_length(syncherVariables.user, "user")

    class RemoteHost(object):
        @staticmethod
        def validator():
            return ValidateParams.check_length(syncherVariables.host, "host")
    
    @staticmethod
    def check_local_os_version():   # Check local OS
        if platform.system() == "Linux":
            ValidateParams.check_exists()   #Check does exist rsync on local machine
            #return True
        else:
            print('Unfortunately, your OS is {}! Rsync works only with Unix-like systems'.format(platform.system()))
            sys.exit(1)
            #return False

    @staticmethod
    def check_exists(): #Check does exist rsync on local machine
        if subprocess.call('which rsync > /dev/null', shell=True) == 0:
            pass
            #return True
        else:
            print("Unfortunately, rsync doesn't exist on your machine! Let's install it!")
            installer.install_local_rsync()  #Install rsync on local machine
            #return False
       
    @staticmethod
    def check_pub_keys():    #Check if public ssh keys exist
        if os.path.exists(expanduser('~')+'/.ssh/id_rsa.pub' ) == True:
            pass
            #return True
        else:
            installer.generate_keys()   #Generate SSH keys
            #return False

#    @staticmethod
#    def do_validator():
#        ValidateParams.Source_files.validator()
#        ValidateParams.Username.validator()
#        ValidateParams.Remote_host.validator()
#        ValidateParams.check_local_os_version()
#        ValidateParams.check_pub_keys()

#ValidateParams.do_validator()

class RemoteCheck(object):

    @staticmethod
    def check_passwordless_access():#Check passwordless access with remote host
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(syncherVariables.host, username=syncherVariables.user)
            #return True
        except:
            print("Passwordless access hasn't been setup with {}! Let's do it!".format(syncherVariables.host))
            #return False

    @staticmethod
    def check_rsync_exists(): #Check does exist rsync on remote machine
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(syncherVariables.host, password=syncherVariables.password, username=syncherVariables.user)
        stdin, stdout, stderr = ssh.exec_command('which rsync')
        data=stdout.readlines()
        if len(data) != 0:
            pass
            #return True
        else:
            print("Unfortunately, rsync doesn't exist on local machine! Let's install it!")
            installer.install_remote_rsync()    #Install rsync on remote machine
            #return False
 
    @staticmethod
    def check_remote_dir_exists():  #Check if remote directory exists
        b=(syncherVariables.dirs).split("/")
        if '*' in dir:
            c = "/".join(b[2:-1])
        else:
            c = "/".join(b[2:])
        need_dir=expanduser('~')+'/'+c
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(syncherVariables.host, password=syncherVariables.password, username=syncherVariables.user)
        stdin, stdout, stderr = ssh.exec_command("find {} ".format(need_dir))
        output=stdout.readlines()
        if len(output) != 0:
            print("Directory {} exists on remote machine".format(syncherVariables.dirs))
            #return True
        else:
            print("Directory {} doesn't exist on remote host!".format(syncherVariables.dirs))
            installer.remote_mkdir(need_dir)  #Make remote directory
            #return False

#Remote_check.check_passwordless_access()
#Remote_check.check_rsync_exists()
#Remote_check.check_remote_dir_exists()


if __name__ == "__main__":
    import syncherVariables
    
