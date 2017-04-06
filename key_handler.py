import signal
import sys
from time import sleep

def interrupt(function):
    try:
# Тут с помощью модуля signal делается перехватчик интеррапт-сигнала (^C),
# дальнейшие действия определяются методом redirect
        signal.signal(signal.SIGINT, redirect)
        function()
    except RuntimeError:
# Ловим RuntimeError от ВТОРОГО ПОДРЯД нажатия ctrl+c - команда input()
# не может добавить ^C в переменную choice (какие-то внутренние шаманства).
# Место выделено комментарием внизу
        print('But you\'re still trying to stop it... Okay.')

def redirect(signum, frame):
    print("\nOperation is still running. It's highly recommended to wait for it to end. ")
    frase = "\bAre you shure you want to stop it? [y/N] ) -> "
# Поправка input-команды на версию питона
    if sys.version_info.major == 2:
        take_input = raw_input
    elif sys.version_info.major == 3:
        take_input = input
    while True:
# RuntimeError exception takes place here, due to some stranger things (tried to figure it out for too much time)...
        choice = take_input(frase)
# Если введен y - останавливаем выполнение операции
        if choice.lower() == 'y':
            sys.exit()
# Если введен n (по умолчанию) - операция выполняется дальше
# (с того места, где было словлено прерывание ^C)
        elif choice.lower() == 'n' or choice == '':
            break
# Если введен любой другой символ - просит ввести заново (идет на while)
        else:
            continue

if __name__ == "__main__":

    def function():
        check = 0
        while True:
            print('{} Goin\'...'.format(check))
            check += 1
            sleep(1)

    interrupt(function)
