from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.dialects.postgresql import UUID
import uuid

db = SQLAlchemy()



# APPWEB
#
# Главная страница с настройками всего сайта и параметрами самой страницы
class Page_main(db.Model):
    id = db.Column(db.String(100), nullable=False, primary_key=True, index=True, unique=True) # url site
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
    views = db.Column(db.Integer, nullable=True)
    publish = db.Column(db.Boolean, default=True, nullable=False, index=True)
    date_create = db.Column(db.DateTime, nullable=True)
    date_update = db.Column(db.DateTime, nullable=True)

# Страницы первого порядка id ключ - это url страницы, праметры и текст
class Page_1(db.Model):
    id = db.Column(db.String(100), nullable=False, primary_key=True, index=True, unique=True) # url page_1
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
####
    sessions = db.relationship('Page_2', backref='page_1', lazy=True)

# Страницы второго порядка
class Page_2(db.Model):
    id = db.Column(db.String(100), nullable=False, primary_key=True, index=True, unique=True) # url page_2
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
####
    page_1_id = db.Column(db.String(100), db.ForeignKey('page_1.id'), nullable=False)
    sessions = db.relationship('Comments', backref='page_2', lazy=True)

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

# Данные для сбора карты сайта
class Sitemap(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    page_main_id = db.Column(db.String(100), nullable=True)
    date_main = db.Column(db.DateTime, nullable=True)

    page_1_id = db.Column(db.String(100), nullable=True)
    date_page_1 = db.Column(db.DateTime, nullable=True)

    page_2_id = db.Column(db.String(100), nullable=True, index=True, unique=True)
    date_page_2 = db.Column(db.DateTime, nullable=True)







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