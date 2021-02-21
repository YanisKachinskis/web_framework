import quopri


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

        method = environ['REQUEST_METHOD']
        data = self.get_input_data(environ)
        data = self.parse_input_data(data)


        query_string = environ['QUERY_STRING']
        request_params = self.data_in_dict(query_string)

        if path in self.routes:
            view = self.routes[path]

            request = {'method': method, 'data': data,
                       'request_params': request_params}

            for controller in self.front_controllers:
                controller(request)
            code, page = view(request)
            start_response(code, [('Content-Type', 'text/html')])
            return [page.encode('utf-8')]
        else:
            start_response('400 NOT FOUND', [('Content-Type', 'text/html')])
            return [b'<h3>404 Page not found!</h3>']

    def get_input_data(self, environ):
        content_length = int(environ.get('CONTENT_LENGTH')) if environ.get(
            'CONTENT_LENGTH') else 0
        data = environ['wsgi.input'].read(
            content_length) if content_length > 0 else b''
        return data

    def parse_input_data(self, data: bytes):
        result = {}
        if data:
            data_string = data.decode(encoding='utf-8')
            # data_string = self.decode_value(data_string)
            result = self.data_in_dict(data_string)
        return result

    def data_in_dict(self, data: str):
        """
        Принимает строку вида id=1&name=Petr,
        Возвращает словарь вида {id: 1, name: 'Petr'}
        :param data: str
        :return: dict
        """
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                key, value = item.split('=')
                value = self.decode_value(value)
                result[key] = value
        return result

    @staticmethod
    def decode_value(val):
        val_in_bytes = bytes(val.replace('%', '=').replace("+", " "), 'utf-8')
        val_decode_str = quopri.decodestring(val_in_bytes)
        return val_decode_str.decode('utf-8')

