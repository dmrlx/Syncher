class connectSSH():
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

class customSSH():
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

class keyHandler():
    class Interrupt():

        @staticmethod
        def redirect(main_runer_function):
            import signal
            signal.signal(signal.SIGINT, Interrupt.handler)
            main_runer_function()

        @staticmethod
        def handler(signum, frame):
            import sys
            from time import sleep
            print("\nOperation is still running. It's highly recommended to wait for it to end.", end='')
            frase = "Are you shure you want to stop it? [y/N] -> "
            while True:
                print(frase, end='')
                choice = sys.stdin.readline()
                print('This is your choice: {}'.format(choice))
                if choice == '':
                    choice='n'
                    break
                elif choice.lower() == 'y':
                    sys.exit()
                elif choice.lower() == 'n':
                    break
                else:
                    continue


    if __name__ == "__main__":
        from time import sleep
        import subprocess

        def func():
    #        subprocess.call('ping tut.by', shell=True)
            while True:
                print('Goin\'...')
                sleep(1)

        Interrupt.redirect(func)

class keyHandler3():
    class Interrupt():

        @staticmethod
        def redirect(main_runer_function):
            import signal
            signal.signal(signal.SIGINT, Interrupt.handle)
            main_runer_function()

        @staticmethod
        def handle(signum, frame):
            import sys
            print("\nOperation is still running. It's highly recommended to wait for it to end.")
            frase = "Are you shure you want to stop it? [y/N] - (Please, just don\'t press Ctrl+C) ->"
            times = 0
            if sys.version_info.major == 2:
                take_input = 'raw_input'
            else:
                take_input = 'input'
            while True:
                sys.stdin.flush()
                sys.stdout.flush()
                choice = Interrupt.take(take_input, frase, times)
                times += 1
                if choice == '':
                    choice='n'
                    break
                elif choice.lower() == 'y':
                    sys.exit()
                elif choice.lower() == 'n':
                    break
                else:
                    continue
        
        @staticmethod
        def take(take_input, frase, times):
            import sys
            from time import sleep
            try:
                print('Trying')
                choice = eval('{}(\"{}\")'.format(take_input, frase))
                print(choice)
            except:
                print('Got Exception {}'.format(sys.exc_info()[0])) # Figure out something with that RuntimeError
                choice = 'I won? {} times'.format(times)
                print(choice)
                sleep(1)
                return choice
            finally:
                return choice


    if __name__ == "__main__":
        from time import sleep
        import subprocess

        def func():
    #        subprocess.call('ping tut.by', shell=True)
            while True:
                print('Goin\'...')
                sleep(1)

        Interrupt.redirect(func)

class keyHandler4():
    class Interrupt():

        @staticmethod
        def redirect(main_runer_function):
            import sys
            try:
                main_runer_function()
            except KeyboardInterrupt:
                print("\nOperation is still running. It's highly recommended to wait for it to end.")
                frase = "\nAre you shure you want to stop it? [y/N] - (Please, just don\'t press Ctrl+C) ->"
                if sys.version_info.major == 2:
                    take_input = raw_input
                elif sys.version_info.major == 3:
                    take_input = input
                while True:
                    try:
                        choice = take_input(frase)
                    except KeyboardInterrupt:
                        continue
                    else:
                        if choice == 'y':
                            sys.exit()
                        elif choice.lower() == 'n' or choice == '':
                            break
                        else:
                            continue

        # @staticmethod
        # def handle():
        #     import sys
        #     Interrupt.first_redirect = False
        #     print("\nOperation is still running. It's highly recommended to wait for it to end.")
        #     frase = "Are you shure you want to stop it? [y/N] - (Please, just don\'t press Ctrl+C) ->"
        #     if sys.version_info.major == 2:
        #         take_input = 'raw_input'
        #     else:
        #         take_input = 'input'
        #     choice = eval('{}(\"{}\")'.format(take_input, frase))
        #     print(choice)
        #     Interrupt.first_redirect = True
        #     return choice
        
    #     @staticmethod
    #     def take(take_input, frase, times):
    #         import sys
    #         from time import sleep
    #         try:
    #             print('Trying')
    #             choice = eval('{}(\"{}\")'.format(take_input, frase))
    #             print(choice)
    #         except:
    #             print('Got Exception {}'.format(sys.exc_info()[0])) # Figure out something with that RuntimeError
    #             choice = 'I won? {} times'.format(times)
    #             print(choice)
    #             sleep(1)
    #             return choice
    #         finally:
    #             return choice


    if __name__ == "__main__":
        from time import sleep
        import subprocess

        def func():
    #        subprocess.call('ping tut.by', shell=True)
            while True:
                print('Goin\'...')
                sleep(1)

        Interrupt.redirect(func)
