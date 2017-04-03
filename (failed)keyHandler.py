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
