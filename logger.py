from patterns.singletones import SingletonByName
from time import time
from datetime import datetime


class ConsoleWriter:

    def write(self, text):
        print(text)


class FileWriter:

    def __init__(self, file_name):
        self.file_name = file_name

    def write(self, text):
        with open(self.file_name, 'a', encoding='utf-8') as f:
            f.write(f'{str(datetime.now())} - {text}\n')


class Logger(metaclass=SingletonByName):

    def __init__(self, name, handler=FileWriter('log.txt')):
        self.name = name
        self.handler = handler

    def log(self, text):
        text = f'[DEBUG] {self.name} {text}'
        self.handler.write(text)


def debug(view):
    def inner(*args, **kwargs):
        start = time()
        res = view(*args, **kwargs)
        finish = time()
        print(f'Запущена функция - {view.__name__}. '
              f'Время выполнения {finish - start}')
        return res
    return inner
