from framework.templates import render


def get_index_view(request):
    courses = [
        {'name': 'Английский'},
        {'name': 'Испанский'},
        {'name': 'Китайский'},
        {'name': 'Французский'}
    ]
    links_menu = request.get('links_menu')
    return '200 OK', render('course_list.html', objects_list=courses,
                            links_menu=links_menu)


def get_about_view(request):
    adresses = ['Москва, ул. Ударная, 13',
                'Санкт-Петербург, ул. Моховая, 23',
                'Казань, пр. Мира, 10']
    links_menu = request.get('links_menu')
    return '200 OK', render('about.html', objects_list=adresses,
                            links_menu=links_menu)


def get_contact_view(request):
    links_menu = request.get('links_menu')
    if request['method'] == 'POST':
        data = request['data']
        title = data['title']
        text = data['text']
        email = data['email']
        print(
            f'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n'
            f'Поступило сообщение от {email}:\n'
            f'Тема: {title}\n'
            f'Текст: {text}\n'
            f'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        return '200 OK', render('contact.html', links_menu=links_menu)
    return '200 OK', render('contact.html', links_menu=links_menu)
