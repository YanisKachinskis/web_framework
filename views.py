from framework.templates import render


def get_index_view(request):
    token = request.get('token')
    return '200 OK', render('index.html', token=token)


def get_about_view(request):
    adresses = ['Москва, ул. Ударная, 13',
                'Санкт-Петербург, ул. Моховая, 23',
                'Казань, пр. Мира, 10']
    return '200 OK', render('about.html', object_list=adresses)


def get_contact_view(request):
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
        return '200 OK', render('contact.html')
    return '200 OK', render('contact.html')
