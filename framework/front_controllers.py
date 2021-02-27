import random


def get_token(request):
    request['token'] = random.randint(1000000, 9999999)


def get_menu(request):
    links_menu = [
        {'href': '/', 'name': 'Главная'},
        {'href': '/course-list/', 'name': 'Список курсов'},
        {'href': '/create-course/', 'name': 'Создать курс'},
        {'href': '/create-category/', 'name': 'Создать категорию'},
        {'href': '/category-list/', 'name': 'Список категорий'},
        {'href': '/create-student/', 'name': 'Создать студента'},
        {'href': '/students-list/', 'name': 'Список студентов'},
        {'href': '/add-student/', 'name': 'Добавить студента на курс'},
        {'href': '/contact/', 'name': 'Написать нам'},
        {'href': '/about/', 'name': 'О нас'},
    ]
    request['links_menu'] = links_menu


front_controllers = [get_token, get_menu]
