from framework.templates import render


def get_index_view(request):
    token = request.get('token')
    return '200 OK', render('index.html', token=token)


def get_about_view(request):
    adresses = ['Москва, ул. Ударная, 13',
                'Санкт-Петербург, ул. Моховая, 23',
                'Казань, пр. Мира, 10']
    return '200 OK', render('about.html', object_list=adresses)


def spam(request):
    return '200 OK', 'Это на самом деле спам!'
