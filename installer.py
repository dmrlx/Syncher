import paramiko, subprocess, os, sys
from os.path import expanduser

def install_local_rsync():    #Install rsync on local machine
    try:
        subprocess.call('apt-get install -y rsync > /dev/null || yum install -y rsync > /dev/null', shell=True)
        print("Rsync was successfully installed!")
    except:
        print("OOps..! Rsync wasn't installed on your machine! Please, check machine's configuration and try again!") 

def install_remote_rsync(): #Install rsync on remote machine
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(syncherVariables.host, password=syncherVariables.password, username=syncherVariables.user)
        stdin, stdout, stderr = ssh.exec_command('apt-get install -y rsync > /dev/null || yum install -y rsync > /dev/null')
        print("Rsync was successfully installed on remote host!")
    except:
        print("OOps..! Rsync wasn't installed on remote machine! Please, check machine's configuration and try again!")
        sys.exit(1)
        
def remote_mkdir(need_dir):    #Make remote directory
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(syncherVariables.host, password=syncherVariables.password, username=syncherVariables.user)
        stdin, stdout, stderr = ssh.exec_command("mkdir -p {}".format(need_dir))
        print("{} was successfully created!".format(need_dir))
    except:
        print("Unfortunately, remote directory wasn't created! Please,try again later")
        sys.exit(1)
 
def generate_keys():    #Generate SSH keys
    try:
        pub_keys_path="expanduser('~')+'/.ssh/id_rsa'"
        subprocess.call('ssh-keygen -t rsa -N "" -f {} > /dev/null'.format(pub_keys_path), shell=True)
        print("SSH keys were successfully generated!")
    except:
        print("Unfortunately, SSH keys weren't generated, please, try again later")
            sys.exit(1)
        
if __name__ == "__main__":
    import syncherVariables
