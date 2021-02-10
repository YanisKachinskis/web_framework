from views import get_index_view, get_about_view, spam

routes = {
    '/': get_index_view,
    '/about/': get_about_view,
    '/spam/': spam
    }