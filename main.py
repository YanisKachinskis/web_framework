from framework.core import App
from logger import Logger
from urls.urls import routes
from framework.front_controllers import front_controllers

logger = Logger('main.py')

logger.log('Запускаем приложение')
app = App(routes, front_controllers)