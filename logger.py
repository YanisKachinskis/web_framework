from patterns.singletones import SingletonByName
from time import time


class Logger(metaclass=SingletonByName):

    def __init__(self, name):
        self.name = name

    def log(self, text):
        print(f'[DEBUG] {self.name} {text}')


def debug(view):
    def inner(*args, **kwargs):
        start = time()
        res = view(*args, **kwargs)
        finish = time()
        print(f'Запущена функция - {view.__name__}. '
              f'Время выполнения {finish - start}')
        return res
    return inner
