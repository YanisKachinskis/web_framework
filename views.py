from framework.cbv import CreateView, ListView
from framework.core import App
from framework.templates import render
from logger import Logger
from mappers import MapperRegistry
from models import TrainingSite, EmailNotifier, SmsNotifier, Serializer
from logger import debug
from orm.unitofwork import UnitOfWork

site = TrainingSite()
logger = Logger('views')
email_notifier = EmailNotifier()
sms_notifier = SmsNotifier()
UnitOfWork.new_current()
UnitOfWork.get_current().set_mapper_registry(MapperRegistry)


@debug
def get_index_view(request):
    logger.log('Получаем главную страницу')
    links_menu = request.get('links_menu')
    return '200 OK', render('index.html', links_menu=links_menu)


class CoursesListView(ListView):
    template_name = 'course_list.html'
    queryset = site.courses

# def get_courses_view(request):
#     logger.log('Получаем список курсов')
#     links_menu = request.get('links_menu')
#     return '200 OK', render('course_list.html', objects_list=site.courses,
#                             links_menu=links_menu)


def create_course(request):
    links_menu = request.get('links_menu')
    if request['method'] == 'POST':
        data = request['data']
        name = data['name']
        name = App.decode_value(name)
        category_id = data.get('category_id')
        if category_id:
            category = site.find_category_by_id(int(category_id))
            course = site.create_course('record', name, category)
            course.observers.append(email_notifier)
            course.observers.append(sms_notifier)
            site.courses.append(course)
        categories = site.categories
        logger.log(f'Создаем новый курс {name}')
        return '200 OK', render('create_course.html', links_menu=links_menu)
    else:
        categories = site.categories
        return '200 OK', render('create_course.html', categories=categories,
                                links_menu=links_menu)


class CategoryListView(ListView):
    template_name = 'categories_list.html'
    queryset = site.categories


# def get_category_view(request):
#     logger.log('Получаем список категорий')
#     links_menu = request.get('links_menu')
#     return '200 OK', render('categories_list.html',
#                             objects_list=site.categories,
#                             links_menu=links_menu)


class CategoryCreateView(CreateView):
    template_name = 'create_category.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['categories'] = site.categories
        return context

    def create_obj(self, data: dict):
        name = data['name']
        name = App.decode_value(name)
        category_id = data.get('category_id')

        category = None
        if category_id:
            category = site.find_category_by_id(int(category_id))

        new_category = site.create_category(name, category)
        site.categories.append(new_category)
        logger.log(f'Создаем новую категорию {new_category.name}')


# def create_category(request):
#     links_menu = request.get('links_menu')
#     if request['method'] == 'POST':
#         data = request['data']
#         name = data['name']
#         name = App.decode_value(name)
#         new_category = site.create_category(name)
#         site.categories.append(new_category)
#         logger.log('Создаем новую категорию')
#         return '200 OK', render('create_category.html', links_menu=links_menu)
#     else:
#         categories = site.categories
#         return '200 OK', render('create_category.html', categories=categories,
#                                 links_menu=links_menu)


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


class StudentCreateView(CreateView):
    template_name = 'create_student.html'

    def create_obj(self, data: dict):
        name = data['name']
        name = App.decode_value(name)
        new_obj = site.create_user('student', name)
        site.students.append(new_obj)
        new_obj.mark_new()
        UnitOfWork.get_current().commit()
        logger.log(f'Создаем нового студента {name}')


class StudentListView(ListView):
    # queryset_1 = site.students
    template_name = 'student_list.html'

    def get_queryset(self):
        mapper = MapperRegistry.get_current_mapper('student')
        return mapper.find_all()


class AddStudentInCourseCreateView(CreateView):
    template_name = 'add_student.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['courses'] = site.courses
        # context['students'] = site.students
        mapper = MapperRegistry.get_current_mapper('student')
        context['students'] = mapper.find_all()
        return context

    def create_obj(self, data: dict):
        course_name = data['course_name']
        course_name = App.decode_value(course_name)
        course = site.get_course(course_name)
        student_name = data['student_name']
        student_name = App.decode_value(student_name)
        mapper = MapperRegistry.get_current_mapper('student')
        for item in mapper.find_all():
            if item.name == student_name:
                student = item
        # student = site.get_student(student_name)
        logger.log(f'Студен {student.name} добавился на курс {course.name}')
        course.add_student(student)


def course_api(request):
    return '200 OK', Serializer(site.courses).save()
