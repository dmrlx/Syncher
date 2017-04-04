def interrupt(function):
    import signal
    try:
        signal.signal(signal.SIGINT, redirect)
        function()
    except RuntimeError:
        print('But you\'re still trying to stop it... Okay.')

def redirect(signum, frame):
    import sys
    print("\nOperation is still running. It's highly recommended to wait for it to end. ")
    frase = "\bAre you shure you want to stop it? [y/N] ) -> "
    if sys.version_info.major == 2:
        take_input = raw_input
    elif sys.version_info.major == 3:
        take_input = input
    while True:
# RuntimeError exception takes place here, due to some stranger things (tried to figure it out for too much time)...
        choice = take_input(frase)
        if choice.lower() == 'y':
            sys.exit()
        elif choice.lower() == 'n' or choice == '':
            break
        else:
            continue

if __name__ == "__main__":
    from time import sleep
    import subprocess
    def function():
    #    subprocess.call('ping tut.by', shell=True)
        check = 0
        while True:
            print('{} Goin\'...'.format(check))
            check += 1
            sleep(1)
    interrupt(function)
