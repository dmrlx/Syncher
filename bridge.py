r""" Bridge - модуль для "проброса ключей":

     - В функции key_transfer создается соединение
       с удаленной машиной и запускаются две остальные
       функции - key_search и key_append.

     - В функции key_search происходит поиск/создание
       файла с паблик ключами на удаленной машине

     - В функции key_append происходит добавление
       созданного на локаьной машине паблик ключа
       к найденному/созданному в функции key_search
       файлу
"""

from subprocess import check_output
from installer import Installer


def key_transfer(key_path):
# Записываем в переменную содержимое паблик ключа на нашей машине
# (сгенерирован в инсталлере)
    local_key = check_output('cat {}.pub'.format(key_path), shell=True).decode().strip()
# Вызываем функцию поиска пути файла с паблик ключами на удаленной машине -
# возвращает путь
    rem_key_path = key_search()
# Вызываем функцию добавления в файл (с паблик ключами на удаленной машине)
# нашего сгенерированного ключа
    key_append(local_key, rem_key_path)

@Installer.to_connect
def key_search(auth_keys='authorized_keys', ssh='will be replaced in wrapper'):
# Смотрим на удаленной машине, есть ли файл с паблик ключами подкючавшихся к ней машин
    stdin, stdout, stderr = ssh.exec_command('find / -name {}'.format(auth_keys))
# Если найден, то записываем путь к нему в переменную
    found = stdout.read().decode()
# Если такого файла не было найдено, создаем его в папке по умолчанию
    if not found:
        ssh.exec_command('mkdir -p ~/.ssh/ && touch ~/.ssh/{}'.format(auth_keys))
        stdin, stdout, stderr = ssh.exec_command('find / -name {}'.format(auth_keys))
        found = stdout.read().decode()
    return found

@Installer.to_connect
def key_append(key, rem_path, ssh='will be replaced in wrapper'):
# Добавляем паблик ключ нашей локальной машины к списку паблик ключей на удаленном хосте
    ssh.exec_command("echo {} >> {}".format(key, rem_path))


if __name__ == '__main__':
# Пример вызова функции
    key_transfer(Installer.pub_keys_path)
