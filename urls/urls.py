from views import get_index_view, get_about_view, get_contact_view

routes = {
    '/': get_index_view,
    '/about/': get_about_view,
    '/contact/': get_contact_view
    }