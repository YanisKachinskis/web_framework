from views import get_index_view, get_about_view, get_contact_view, \
    get_courses_view, get_category_view, create_category, create_course, \
    copy_course

routes = {
    '/': get_index_view,
    '/course-list/': get_courses_view,
    '/create-course/': create_course,
    '/category-list/': get_category_view,
    '/create-category/': create_category,
    '/copy-course/': copy_course,
    '/about/': get_about_view,
    '/contact/': get_contact_view
    }

