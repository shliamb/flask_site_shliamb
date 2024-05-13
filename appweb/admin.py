from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import Page_main, Page_1, Page_2, Menu, Comments



def setup_admin(app, db):
    admin = Admin(app, name='Admin panel:', template_mode='bootstrap3', url='/admin')
    admin.add_view(ModelView(Page_main, db.session))
    admin.add_view(ModelView(Page_1, db.session))
    admin.add_view(ModelView(Page_2, db.session))
    admin.add_view(ModelView(Menu, db.session))
    admin.add_view(ModelView(Comments, db.session))



