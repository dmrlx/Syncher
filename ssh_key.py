import subprocess
from paramiko import SSHClient, AutoAddPolicy
import installer

def transfer(username, hostname, password, key_path):
# Записываем в переменную содержимое паблик ключа на нашей машине
# (сгенерирован в инсталлере)
    local_key = subprocess.check_output('cat {}.pub'.format(key_path)).decode()
# Три команды - подключаемся к удаленной машине
    remote_machine = SSHClient()
    remote_machine.set_missing_host_key_policy(AutoAddPolicy())
    remote_machine.connect(username=username, hostname=hostname, password=password)
# Вызываем функцию поиска пути файла с паблик ключами на удаленной машине -
# возвращает путь
    rem_key_path = key_search(remote_machine)
# Вызываем функцию добавления в файл (с паблик ключами на удаленной машине)
# нашего сгенерированного ключа
    key_append(remote_machine, local_key, rem_key_path)

def key_search(machine, auth_keys='authorized_keys'):
# Смотрим на удаленной машине, есть ли файл с паблик ключами подкючавшихся к ней машин
    stdin, stdout, stderr = machine.exec_command('find / -name {}'.format(auth_keys))
# Если найден, то записываем путь к нему в переменную
    found = stdout.read().decode()
# Если такого файла не было найдено, создаем его в папке по умолчанию
    if not found:
        machine.exec_command('mkdir -p ~/.ssh/ && touch ~/.ssh/{}'.format(auth_keys))
        stdin, stdout, stderr = machine.exec_command('find / -name {}'.format(auth_keys))
        found = stdout.read().decode()
    return found

def key_append(machine, key, rem_path):
# Добавляем паблик ключ нашей локальной машины к списку паблик ключей на удаленном хосте
    machine.exec_command("echo {} >> {}".format(key, rem_path))

if __name__ == '__main__':
    transfer('root', '192.168.222.131', 'me', installer.pub_keys_path)
