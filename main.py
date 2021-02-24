from framework.core import App
from logger import Logger
from urls.urls import routes
from framework.front_controllers import front_controllers
from wsgiref.simple_server import make_server

logger = Logger('main.py')

logger.log('Запускаем приложение')
app = App(routes, front_controllers)

with make_server('', 8000, app) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()