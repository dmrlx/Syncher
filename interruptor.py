r""" Interruptor - модуль, "перехватывающий" комманду
     прерывания выполнения (^C) переданной функции, и
     задающий условие для дальнейшего выполнения функции.

     Функция handle осуществляет "перехват" первого прерывания
     и останавливает выполнение функции при втором прерывании.

     Функция redirect задает после первого прерывания условие
     для дальнейшего выполнения функции ("продолжить" или "остановиться").
"""

from signal import signal, SIGINT
from sys import version_info, exit as sys_exit


def handle(function):
    try:
# Тут с помощью модуля signal делается перехватчик интеррапт-сигнала (^C),
# дальнейшие действия определяются методом redirect
        signal(SIGINT, redirect)
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
    if version_info.major == 2:
        take_input = raw_input
    elif version_info.major == 3:
        take_input = input
    while True:
# RuntimeError exception takes place here, due to some stranger things (tried to figure it out for too much time)...
        choice = take_input(frase)
# Если введен y - останавливаем выполнение операции
        if choice.lower() == 'y':
            sys_exit()
# Если введен n (по умолчанию, т.е. можно нажать ввод) - операция выполняется дальше
# (с того места, где было словлено прерывание ^C)
        elif choice.lower() == 'n' or choice == '':
            break
# Если введен любой другой символ - просит ввести заново (идет на while)
        else:
            continue


if __name__ == "__main__":
    from time import sleep


    def function():
        check = 0
        while True:
            print('{} Goin\'...'.format(check))
            check += 1
            sleep(1)
# Пример использования
    handle(function)
