import subprocess
import paramiko
"""
# cmd = 'ssh -f user@host'
# password = '111'
# subprocess.call("expect -c 'spawn {}; expect -re \".*assword.*\";send \"{}\n\";\
#                 interact;'".format(command, password), shell=True)

cmd = "echo Enter password: "
std_codes = subprocess.PIPE
p = subprocess.Popen(cmd, shell=True, stdin=std_codes, stdout=std_codes, stderr=subprocess.STDOUT)
out = p.stdout.read().decode()
print(out)
if 'assword' in out:
    print('Got it!')
    p.stdin.write('111'.encode())
"""

def remote_commander(cmd, user, host, password):
    import paramiko
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=password)
    stdin, stdout, stderr = client.exec_command(cmd)
    

host = '192.168.222.131'
user = 'root'
secret = 'me'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret)
stdin, stdout, stderr = client.exec_command('ls')
result = [eval("{}.read().decode()".format(_)) for _ in ['stdout', 'stderr']]
client.close()
print(result)