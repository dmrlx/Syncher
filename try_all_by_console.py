# -*- coding: utf-8 -*-

import subprocess

# Генератор ping'a
def ping_cmd_generator(host, timer=1):
    ping_cmd = "ping " + str(host) + " -c 1 " + "-W " + str(timer)
    return ping_cmd

# Спёр у Полины
def check_passwordless_access(user='dmrlx', host='192.168.56.102'):
    try:
        subprocess.call("ssh -o NumberOfPasswwordPromts=0 {}@{} 'echo hello'".format(user, host))
        print('Access granted.')
    except:
        print('Access denied')
        do_passwordless_access()

# Моя очередь
def do_passwordless_access(key_path='$HOME/.ssh/id_rsa', passphrase='', user='dmrlx', host='192.168.56.102', password='111'):
    pipe = subprocess.PIPE
    ssh_keygen = subprocess.Popen("ssh-keygen -q -f {} -N {}".format(key_path, passphrase),
                                   shell=True, stdout=pipe, stderr=subprocess.STDOUT)
    pswd = subprocess.Popen("echo {}".format(password), shell=True, stdout=pipe)
    print(pswd.stdout.read())
    ssh_copy_id = subprocess.Popen('ssh-copy-id -i $HOME/.ssh/id_rsa.pub -o StrictHostKeyChecking=no dmrlx@192.168.56.102',
                                    shell=True, stdin=pswd.stdout, stdout=pipe, stderr=subprocess.STDOUT)
    # Если тут запустить какой-нибудь ssh_copy_id.stdout.read(), то ничего не выйдет. Все еще ищу решение...

# Проверяем наличие указанной папки на удалённом компе, при необходимости создаем
def rem_dir_check(user='dmrlx', host='192.168.56.102', rem_dir='/directory'):
    import subprocess
    check = subprocess.Popen("ssh {}@{} 'test -d {}'".format(user, host, rem_dir), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    check.communicate()
    not_there = check.returncode
    if not_there:
        subprocess.call("ssh {}@{} 'mkdir {}'".format(user, host, rem_dir))


# pusher: Отправляет сформированные в модуле composer команды
# Возвращает "0" если всё хорошо и "1" если ошибка.
def pusher(cmd):
    cmd = cmd.split()
    push = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = push.stdout.read().decode()
    error = push.stderr.read().decode()
    push.wait()
    return push.poll()

if __name__ == "__main__":
    pusher(ping_cmd_generator("192.168.56.102"))


