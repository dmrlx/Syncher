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
