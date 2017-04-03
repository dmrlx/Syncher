import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname='192.168.0.102', username='virtual', password='Me')
print(client.get_host_keys().save())
stdin, stdout, stderr = client.exec_command('ls')
print(stdout.read().split())