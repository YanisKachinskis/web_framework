import random


def get_token(request):
    request['token'] = random.randint(1000000, 9999999)


front_controllers = [get_token]