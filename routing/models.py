from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid

db = SQLAlchemy()



# APPWEB
#
# The main page with the settings of the entire site and the parameters of the page itself
class Page_main(db.Model):
    id = db.Column(db.Integer, primary_key=True, default=1, nullable=False, index=True) # just 1
    url_site = db.Column(db.String(100), nullable=False, index=True) # site.ru or com
    responsive = db.Column(db.Boolean, default=True, nullable=False, index=True)
    lang = db.Column(db.String(100), default="ru", nullable=False, index=True)
    return_code = db.Column(db.Integer, default=200, nullable=False, index=True)
    comments = db.Column(db.Boolean, default=True, nullable=False, index=True)
    title = db.Column(db.String(1000), nullable=True, index=True)
    seo_title = db.Column(db.String(1000), nullable=True, index=True)
    seo_description = db.Column(db.String(1000), nullable=True, index=True)
    seo_keyword = db.Column(db.String(500), nullable=True, index=True)
    text_body = db.Column(db.String(5000), nullable=True, index=True)
    id_who_changed = db.Column(db.BigInteger, nullable=True)
    time_zone = db.Column(db.Integer, default=+3, nullable=False, index=True)
    views = db.Column(db.Integer, nullable=True)
    publish = db.Column(db.Boolean, default=True, nullable=False, index=True)
    date_create = db.Column(db.DateTime, nullable=True)
    date_update = db.Column(db.DateTime, nullable=True)
    changefreq = db.Column(db.String(500), default="monthly", nullable=False, index=True)
    priority = db.Column(db.Float, default=1, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'url_site': self.url_site,
            'responsive': self.responsive,
            'lang': self.lang,
            'return_code': self.return_code,
            'comments': self.comments,
            'title': self.title,
            'seo_title': self.seo_title,
            'seo_description': self.seo_description,
            'seo_keyword': self.seo_keyword,
            'text_body': self.text_body,
            'id_who_changed': self.id_who_changed,
            'time_zone': self.time_zone,
            'views': self.views,
            'publish': self.publish,
            'date_create': self.date_create,
            'date_update': self.date_update,
            'changefreq': self.changefreq,
            'priority': self.priority
        }

# The first-order page id key is the page url, parameters, and text
class Page_1(db.Model):
    id = db.Column(db.String(100), nullable=False, primary_key=True, index=True, unique=True) # url page_1
    url_site = db.Column(db.String(100), nullable=False, index=True) # site.ru or com
    title = db.Column(db.String(1000), nullable=True, index=True)
    seo_title = db.Column(db.String(1000), nullable=True, index=True)
    seo_description = db.Column(db.String(1000), nullable=True, index=True)
    seo_keyword = db.Column(db.String(500), nullable=True, index=True)
    text_body = db.Column(db.String(5000), nullable=True, index=True)
    id_who_changed = db.Column(db.BigInteger, nullable=True)
    views = db.Column(db.Integer, nullable=True)
    publish = db.Column(db.Boolean, default=True, nullable=False, index=True)
    date_create = db.Column(db.DateTime, nullable=True)
    date_update = db.Column(db.DateTime, nullable=True)
    changefreq = db.Column(db.String(500), default="monthly", nullable=False, index=True)
    priority = db.Column(db.Float, default=1, nullable=False)
####
    sessions = db.relationship('Page_2', backref='page_1', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'url_site': self.url_site,
            'title': self.title,
            'seo_title': self.seo_title,
            'seo_description': self.seo_description,
            'seo_keyword': self.seo_keyword,
            'text_body': self.text_body,
            'id_who_changed': self.id_who_changed,
            'views': self.views,
            'publish': self.publish,
            'date_create': self.date_create,
            'date_update': self.date_update,
            'changefreq': self.changefreq,
            'priority': self.priority
        }

# Pages of the second order
class Page_2(db.Model):
    id = db.Column(db.String(100), nullable=False, primary_key=True, index=True, unique=True) # url page_2
    url_site = db.Column(db.String(100), nullable=False, index=True) # site.ru or com
    title = db.Column(db.String(1000), nullable=True, index=True)
    seo_title = db.Column(db.String(1000), nullable=True, index=True)
    seo_description = db.Column(db.String(1000), nullable=True, index=True)
    seo_keyword = db.Column(db.String(500), nullable=True, index=True)
    text_body = db.Column(db.String(5000), nullable=True, index=True)
    id_who_changed = db.Column(db.BigInteger, nullable=True)
    views = db.Column(db.Integer, nullable=True)
    publish = db.Column(db.Boolean, default=True, nullable=False, index=True)
    date_create = db.Column(db.DateTime, nullable=True)
    date_update = db.Column(db.DateTime, nullable=True)
    changefreq = db.Column(db.String(500), default="monthly", nullable=False, index=True)
    priority = db.Column(db.Float, default=1, nullable=False)
####
    page_1_id = db.Column(db.String(100), db.ForeignKey('page_1.id'), nullable=False) # Родительская страница
    sessions = db.relationship('Comments', backref='page_2', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'url_site': self.url_site,
            'title': self.title,
            'seo_title': self.seo_title,
            'seo_description': self.seo_description,
            'seo_keyword': self.seo_keyword,
            'text_body': self.text_body,
            'id_who_changed': self.id_who_changed,
            'views': self.views,
            'publish': self.publish,
            'date_create': self.date_create,
            'date_update': self.date_update,
            'page_1_id': self.page_1_id,
            'changefreq': self.changefreq,
            'priority': self.priority
        }

# MENU
class Menu(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, unique=True, nullable=False) # id menu
    url_site = db.Column(db.String(100), nullable=False, index=True) # site.ru or com
    main_page = db.Column(db.String(100), nullable=True, index=True)
    secondary_page = db.Column(db.String(100), nullable=True, index=True)
    title = db.Column(db.String(1000), nullable=True, index=True)
    count_2_page = db.Column(db.BigInteger, nullable=True)
    count_comments = db.Column(db.Integer, nullable=True)
    publish = db.Column(db.Boolean, default=True, nullable=False, index=True)
    date_create = db.Column(db.DateTime, nullable=True)
    date_update = db.Column(db.DateTime, nullable=True)
####

    def serialize(self):
        return {
            'id': self.id,
            'url_site': self.url_site,
            'main_page': self.main_page,
            'secondary_page': self.secondary_page,
            'title': self.title,
            'count_2_page': self.count_2_page,
            'count_comments': self.count_comments,
            'publish': self.publish,
            'date_create': self.date_create,
            'date_update': self.date_update,
        }



# Комментарии на страницах второго порядка page_2_id - url родителя комментария
class Comments(db.Model):
    id = db.Column(db.BigInteger, primary_key=True) # Просто номер комментария
    answer_to_id = db.Column(db.BigInteger, default=None, nullable=True) # Если комментарий - это ответ, то номер комментария на который отвечаем.
    id_autor = db.Column(db.BigInteger, nullable=True) # Стоит аккуратно использовать, скорее всего только на беке, что бы не палить на фронте id пользователя телеграмм
    hidden_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False) # Для определения пользователя на фронте без палева
    text_comment = db.Column(db.String(5000), nullable=True, index=True)
    img_comment = db.Column(db.String(1000), nullable=True, index=True) # Имя сохраненной картинки, возможно лучщше ее потом обрабатывать - уменьшать
    likes = db.Column(db.BigInteger, nullable=True)
    who_liked = db.Column(db.String(5000), nullable=True, index=True) # id кому понравилось, может последние трое, чисто для картинки, посмотрим, но без определения личности
    publish = db.Column(db.Boolean, default=True, nullable=False, index=True)
    is_block = db.Column(db.Boolean, default=False, nullable=False, index=True)
    is_spam = db.Column(db.Boolean, default=False, nullable=False, index=True)
    is_bot = db.Column(db.Boolean, default=False, nullable=False, index=True)
    date_create = db.Column(db.DateTime, nullable=True)
    date_update = db.Column(db.DateTime, nullable=True)
####
    page_2_id = db.Column(db.String(100), db.ForeignKey('page_2.id'), nullable=False) # Страница 2 порядка после главной где расспологается коммент










# Ниже буду делать позже...

# APPLOGIN

# APPADMIN

# class Push(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     length = db.Column(db.String(4), nullable=False)
#     track_number = db.Column(db.Integer, nullable=False)

# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     length = db.Column(db.String(4), nullable=False)
#     track_number = db.Column(db.Integer, nullable=False)
    
# class Sitemap(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     length = db.Column(db.String(4), nullable=False)
#     track_number = db.Column(db.Integer, nullable=False)




# class Users(db.Model):
#     id = db.Column(db.BigInteger, primary_key=True, unique=True, nullable=False, index=True)
#     name = db.Column(db.String(1000), nullable=False)
#     full_name = db.Column(db.String(1000), nullable=False)
#     first_name = db.Column(db.String(1000), nullable=False)
#     last_name = db.Column(db.String(1000), nullable=False)
#     date = db.Column(db.DateTime, nullable=True)



# class Admins(db.Model):
#     id = db.Column(db.BigInteger, primary_key=True, unique=True, nullable=False, index=True)
#     name = db.Column(db.String(1000), nullable=False)
#     email = db.Column(db.String(1000), nullable=False)
#     pasword = db.Column(db.String(1000), nullable=False)
#     date = db.Column(db.DateTime, nullable=True)

# class Push_admin(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     length = db.Column(db.String(4), nullable=False)
#     track_number = db.Column(db.Integer, nullable=False)

# class Task_admin(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     length = db.Column(db.String(4), nullable=False)
#     track_number = db.Column(db.Integer, nullable=False)