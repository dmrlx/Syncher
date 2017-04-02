import subprocess
import paramiko

def pusher(cmd):
    cmd = cmd.split()
    push = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = push.stdout.read().decode()
    error = push.stderr.read().decode()
    print(error)
    push.wait()
    return push.poll()

# pusher("sudo apt-get install sshpass")
# print(pusher("sshpass -p 123456 ssh root@192.168.56.102"))


username = "root"
pw = "123456"
host = "192.168.56.102"
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=pw)

client.exec_command("mkdir /1111111")

