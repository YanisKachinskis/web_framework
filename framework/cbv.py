from framework.templates import render


class TemplateView:
    template_name = 'template.html'

    def get_context_data(self):
        return {}

    def get_template(self):
        return self.template_name

    def render_template_with_context(self, links_menu):
        template_name = self.get_template()
        context = self.get_context_data()

        return '200 OK', render(template_name, **context, links_menu=links_menu)

    def __call__(self, request):
        links_menu = request['links_menu']
        return self.render_template_with_context(links_menu)


class ListView(TemplateView):
    queryset = []
    template_name = 'list.html'
    context_object_name = 'objects_list'

    def get_queryset(self):
        print(self.queryset)
        return self.queryset

    def get_context_object_name(self):
        return self.context_object_name

    def get_context_data(self):
        queryset = self.get_queryset()
        context_object_name = self.get_context_object_name()
        context = {context_object_name: queryset}
        return context


class CreateView(TemplateView):
    template_name = 'create.html'

    def get_request_data(self, request: dict) -> dict:
        return request['data']

    def create_obj(self, data: dict):
        pass

    def __call__(self, request: dict):
        links_menu = request['links_menu']
        if request['method'] == 'POST':
            # метод пост
            data = self.get_request_data(request)
            self.create_obj(data)
            return self.render_template_with_context(links_menu)
        else:
            return super().__call__(request)