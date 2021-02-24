from framework.core import App, FakeApp
from framework.templates import render
from logger import Logger
from urls.urls import routes
from framework.front_controllers import front_controllers
from wsgiref.simple_server import make_server

logger = Logger('main.py')

logger.log('Запускаем приложение')
app = App(routes, front_controllers)
# app = FakeApp(routes, front_controllers)


@app.add_route('/about/')
def get_about_view(request):
    addresses = ['Москва, ул. Ударная, 13',
                 'Санкт-Петербург, ул. Моховая, 23',
                 'Казань, пр. Мира, 10']
    links_menu = request.get('links_menu')
    return '200 OK', render('about.html', objects_list=addresses,
                            links_menu=links_menu)


with make_server('', 9090, app) as httpd:
    print("Serving on port 9090...")
    httpd.serve_forever()