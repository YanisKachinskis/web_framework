from framework.core import App
from framework.templates import render
from logger import Logger
from models import TrainingSite
from logger import debug

site = TrainingSite()
logger = Logger('views.py')


@debug
def get_index_view(request):
    logger.log('Получаем главную страницу')
    links_menu = request.get('links_menu')
    return '200 OK', render('index.html', links_menu=links_menu)


@debug
def get_courses_view(request):
    logger.log('Получаем список курсов')
    links_menu = request.get('links_menu')
    return '200 OK', render('course_list.html', objects_list=site.courses,
                            links_menu=links_menu)


def create_course(request):
    links_menu = request.get('links_menu')
    if request['method'] == 'POST':
        data = request['data']
        name = data['name']
        category_id = data.get('category_id')
        category = None
        if category_id:
            category = site.find_category_by_id(int(category_id))
            course = site.create_course('record', name, category)
            site.courses.append(course)
        logger.log('Создаем новый курс')
        return '200 OK', render('create_course.html', links_menu=links_menu)
    else:
        categories = site.categories
        return '200 OK', render('create_course.html', categories=categories,
                                links_menu=links_menu)


def get_category_view(request):
    logger.log('Получаем список категорий')
    links_menu = request.get('links_menu')
    return '200 OK', render('categories_list.html',
                            objects_list=site.categories,
                            links_menu=links_menu)


def create_category(request):
    links_menu = request.get('links_menu')
    if request['method'] == 'POST':
        data = request['data']
        name = data['name']
        name = App.decode_value(name)
        new_category = site.create_category(name)
        site.categories.append(new_category)
        logger.log('Создаем новую категорию')
        return '200 OK', render('create_category.html', links_menu=links_menu)
    else:
        categories = site.categories
        return '200 OK', render('create_category.html', categories=categories,
                                links_menu=links_menu)


def copy_course(request):
    logger.log('Копируем курс')
    links_menu = request.get('links_menu')
    request_params = request['request_params']
    name = request_params['name']
    old_course = site.get_course(name)
    if old_course:
        new_name = f'копия_курса_{name}'
        new_course = old_course.clone()
        new_course.name = new_name
        site.courses.append(new_course)
    return '200 OK', render('course_list.html', objects_list=site.courses,
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
