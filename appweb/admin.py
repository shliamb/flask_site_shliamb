from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from models import Page_main, Page_1, Page_2, Menu, Comments
from flask_admin.contrib.fileadmin import FileAdmin


class PageMainModel(ModelView):
    column_labels = {'url_site': 'Сайт', 'responsive': 'Адаптивный', 'lang': 'Язык'}


class MyAdminIndexView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html', admin=True)
    


def setup_admin(app, db):
    admin = Admin(app, name='Админка:', template_mode='bootstrap2', url='/admin')
    #admin = Admin(app, name='Админка:', template_mode='bootstrap2', index_view=MyAdminIndexView(url='/admin'))
    admin.add_view(PageMainModel(Page_main, db.session, name='Сайт'))
    admin.add_view(ModelView(Page_1, db.session, name='Разделы'))
    admin.add_view(ModelView(Page_2, db.session, name='Страницы'))
    admin.add_view(ModelView(Menu, db.session, name='Меню'))
    admin.add_view(ModelView(Comments, db.session, name='Комментарии'))
    path = './files'
    admin.add_view(FileAdmin(path, name='File Manager'))




# class UserView(ModelView):
#     column_filters = ['username', 'email']
#     column_sortable_list = ['username', 'email']

# class UserAdminView(ModelView):
#     column_searchable_list = ('username',)
#     column_sortable_list = ('username', 'admin')
#     column_exclude_list = ('pwdhash',)
#     form_excluded_columns = ('pwdhash',)
#     form_edit_rules = ('username', 'admin')

# def is_accessible(self):
#     return current_user.is_authenticated and current_user.is_adminfrom flask_admin.contrib.sqla import ModelView

