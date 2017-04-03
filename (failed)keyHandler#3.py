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
