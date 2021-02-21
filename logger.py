from patterns.singletones import SingletonByName


class Logger(metaclass=SingletonByName):

    def __init__(self, name):
        self.name = name

    def log(self, text):
        print(f'[DEBUG] {self.name} {text}')