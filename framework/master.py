class App:

    def __init__(self, routes: dict, front_controllers: list):
        """
        Объект класса принимает словарь из связок url: view, а так же
        список функций front_controllers
        :param routes:
        :param front_controllers:
        """
        self.routes = routes
        self.front_controllers = front_controllers

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        print(f'Loading page: {path}')
        if not path.endswith('/'):
            path = f'{path}/'
        if path in self.routes:
            view = self.routes[path]
            request = {}
            for controller in self.front_controllers:
                controller(request)
            code, page = view(request)
            start_response(code, [('Content-Type', 'text/html')])
            return [page.encode('utf-8')]
        else:
            start_response('400 NOT FOUND', [('Content-Type', 'text/html')])
            return [b'<h3>404 Page not found!</h3>']
