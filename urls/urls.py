from views import get_index_view, get_contact_view, \
    create_course, copy_course, CategoryCreateView, CategoryListView, \
    CoursesListView, StudentCreateView, StudentListView, \
    AddStudentInCourseCreateView, course_api

routes = {
    '/': get_index_view,
    '/course-list/': CoursesListView(),
    '/create-course/': create_course,
    '/category-list/': CategoryListView(),
    '/create-category/': CategoryCreateView(),
    '/create-student/': StudentCreateView(),
    '/students-list/': StudentListView(),
    '/add-student/': AddStudentInCourseCreateView(),
    '/copy-course/': copy_course,
    '/contact/': get_contact_view,
    '/api/': course_api,
    }

