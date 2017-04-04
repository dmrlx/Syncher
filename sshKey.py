def transfer(username, hostname, password):
    from paramiko import SSHClient, AutoAddPolicy
    from socket import gethostbyname, gethostname
    import installer

    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(username=username, hostname=hostname, password=password)
# Смотрим есть ли файл авторизированных ключей, если нет - создаем
    auth_keys = 'authorized_keys'
    stdin, stdout, stderr = client.exec_command('find / -name {}'.format(auth_keys))
    rem_path_to_keys = stdout.read().decode()
    if not rem_path_to_keys:
        client.exec_command('mkdir -p ~/.ssh/ && touch ~/.ssh/{}'.format(auth_keys))
        stdin, stdout, stderr = client.exec_command('find / -name {}'.format(auth_keys))
        rem_path_to_keys = stdout.read().decode()
# Добавляем наш ключ к списку ключей на удаленном хосте
    client.exec_command("cat {}.pub >> {}".format(installer.pub_keys_path, rem_path_to_keys))

if __name__ == '__main__':
    transfer('root', '192.168.222.131', 'me')
