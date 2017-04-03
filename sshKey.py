def transfer(username, hostname, password):
    from paramiko import SSHClient, AutoAddPolicy
    from socket import gethostbyname, gethostname
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    # Я это просто так тут оставлю...
    # rsa = paramiko.RSAKey.generate(2048)
    # print(rsa.get_base64())
    client.connect(username=username, hostname=hostname, password=password)

    # Смотрим есть ли файл авторизированных ключей, если нет - создаем
    stdin, stdout, stderr = client.exec_command('find / -name {}'.format('authorized_keys'))
    path_to_keys = stdout.read().decode()
    if not path_to_keys:
        # print('Got here')
        client.exec_command('mkdir -p ~/.ssh/ && touch ~/.ssh/{}'.format('authorized_keys'))
        stdin, stdout, stderr = client.exec_command('find / -name {}'.format('authorized_keys'))
        path_to_keys = stdout.read().decode()
    # print(path_to_keys)

    # Генерим паблик ключ для мёрджа на удаленном хосте
    for k, v in client.get_host_keys().values()[0].items():
        pub_key = '{} {} {}@{}'.format(k, v.get_base64(), gethostname(), gethostbyname(gethostname()))
        # print(pub_key)
        break

    # Добавляем наш ключ к списку ключей на удаленном хосте
    client.exec_command("echo \'{}\' >> {}".format(pub_key, path_to_keys))

if __name__ == '__main__':
    transfer('root', '192.168.222.131', 'me')