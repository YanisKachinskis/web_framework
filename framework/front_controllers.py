import random


def get_token(request):
    request['token'] = random.randint(1000000, 9999999)


def get_menu(request):
    links_menu = [
        {'href':  '/', 'name':  'Главная'},
        {'href':  '/contact/', 'name':  'Написать нам'},
        {'href':  '/about/', 'name': 'О нас'},
    ]
    request['links_menu'] = links_menu



front_controllers = [get_token, get_menu]