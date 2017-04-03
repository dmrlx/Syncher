from syncherVariables import ParserResults, CustomShell


def keygen(file_path='$HOME/.ssh/id_rsa', passphrase=''):
    import subprocess
    pipe = subprocess.PIPE
    proc = subprocess.Popen('ssh-keygen -q -f {} -N \"{}\"'.format(
        file_path, passphrase), shell=True, stdout=pipe, stderr=subprocess.STDOUT)
    CustomShell.key_path = file_path


def id_copy(key_path, user, host, password='Me'):
    import os, pty, subprocess
    pipe = subprocess.PIPE
    pswd = subprocess.Popen('echo {}'.format(
        password), shell=True, stdout=pipe)
    print(pswd.stdout.read())
    pid, child_fd = pty.fork()
    proc = subprocess.Popen('ssh-copy-id -i {}.pub -o StrictHostKeyChecking=no {}@{}'.format(
        key_path, user, host), shell=True, stdin=pswd.stdout, stdout=pipe, stderr=subprocess.STDOUT)

    # try:
    #     output = os.read(child_fd, 1024).strip()
    # except:
    #     pass
    # lower = output.lower()
    # if b'password:' in lower:
    #     write(child_fd, self.password + b'\n')
    #...

    # with proc.stdout.readlines():
    #     print(proc.stdin.writable())
    #     if proc.stdin.writable():
    #         proc.stdin.write(password)


if __name__ == "__main__":
    keygen('$HOME/key')
    id_copy('$HOME/key', 'virtual', '192.168.0.102')
