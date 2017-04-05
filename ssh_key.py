def transfer(username, hostname, password):
    from paramiko import SSHClient, AutoAddPolicy
    import installer
# Три команды - подключаемся к удаленной машине
    remote_machine = SSHClient()
    remote_machine.set_missing_host_key_policy(AutoAddPolicy())
    remote_machine.connect(username=username, hostname=hostname, password=password)
# Смотрим на удаленной машине, есть ли файл с паблик ключами подкючавшихся к ней машин
    auth_keys = 'authorized_keys'
    stdin, stdout, stderr = remote_machine.exec_command('find / -name {}'.format(auth_keys))
# Если найден, то записываем путь к нему в переменную
    rem_keys_path = stdout.read().decode()
# Если такого файла не было найдено, создаем его в папке по умолчанию
    if not rem_keys_path:
        remote_machine.exec_command('mkdir -p ~/.ssh/ && touch ~/.ssh/{}'.format(auth_keys))
        stdin, stdout, stderr = remote_machine.exec_command('find / -name {}'.format(auth_keys))
        rem_keys_path = stdout.read().decode()
# Добавляем паблик ключ нашей локальной машины к списку паблик ключей на удаленном хосте
    remote_machine.exec_command("cat {}.pub >> {}".format(installer.pub_keys_path, rem_keys_path))

if __name__ == '__main__':
    transfer('root', 'host', '111')
