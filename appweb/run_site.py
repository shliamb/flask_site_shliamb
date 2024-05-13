#### Logging ####
import logging
logging.basicConfig(level=logging.INFO, filename='./appweb/log/appweb.log', filemode='a', format='%(levelname)s - %(asctime)s - %(name)s - %(message)s',) 
#### Flask ####
import flask
#### Modules ####
from api import api_blueprint
from views import views_blueprint
from models import db#, Page_1  # Импортируйте ваши модели данных
from admin import setup_admin  # Импортируйте функцию настройки админки
from keys import user_db, paswor_db, flask_key


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = flask_key

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user_db}:{paswor_db}@localhost:5433/flask_database"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app) # Инициализация базы



# Регистрация Blueprint'ов
app.register_blueprint(api_blueprint, url_prefix='/api') # API
app.register_blueprint(views_blueprint, url_prefix='/') # Default site

setup_admin(app, db) # Инициализация админки

























# app.secret_key = 'sdJhvfhYghhjnm2b32jsdhsnxsdfJJJKKK'  # Change this! super secret string
# login_manager = flask_login.LoginManager()
# login_manager.init_app(app)


# # Our mock database.
# users = {'admin': {'password': '123'}}

# class User(flask_login.UserMixin):
#     pass


# @login_manager.user_loader
# def user_loader(email):
#     if email not in users:
#         return

#     user = User()
#     user.id = email
#     return user


# @login_manager.request_loader
# def request_loader(request):
#     email = request.form.get('email')
#     if email not in users:
#         return

#     user = User()
#     user.id = email
#     return user


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if flask.request.method == 'GET':
#         return '''
#                <form action='login' method='POST'>
#                 <input type='text' name='email' id='email' placeholder='email'/>
#                 <input type='password' name='password' id='password' placeholder='password'/>
#                 <input type='submit' name='submit'/>
#                </form>
#                '''

#     email = flask.request.form['email']
#     if email in users and flask.request.form['password'] == users[email]['password']:
#         user = User()
#         user.id = email
#         flask_login.login_user(user)
#         return flask.redirect(flask.url_for('protected'))

#     return 'Bad login'


# @app.route('/protected')
# @flask_login.login_required
# def protected():
#     return 'Logged in as: ' + flask_login.current_user.id



# @app.route('/logout')
# def logout():
#     flask_login.logout_user()
#     return 'Logged out'



# @login_manager.unauthorized_handler
# def unauthorized_handler():
#     return 'Unauthorized', 401







if __name__ == '__main__':
    app.run(debug=True, port=5000)























# @app.route('/')
# def home():
#     return render_template('main.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/songs')
# def songs():
#     songs_list = Song.query.all()
#     return render_template('songs.html', songs=songs_list)


# {% for song in songs %}
#     <div class="col-md-3">
#       <div class="card mb-3">
#           <div class="card-header fw-bold">{{ song.title }}</div>
#           <div class="card-body">
#               <p class="badge bg-primary text-wrap">{{ song.album.artist.name }}</p>
#               <p class="card-text">Альбом: 
#               <strong>{{ song.album.title }}</strong></p>
#               <p class="card-text">Длина: {{ song.length }} минут</p>
#               <p class="card-text">Номер трека: {{ song.track_number }}</p>
#               <p class="card-text">Дата релиза: {{ song.album.year }}</p>
#           </div>
#       </div>
#     </div>
#   {% endfor %}



# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         # проверка логина и пароля
#         return 'Вы вошли в систему!'
#     else:
#         return render_template('login.html')



# @app.route('/<manufacturer>/<category>')
# def show_items(manufacturer, category):
#     items = Item.query.join(Item.manufacturers).join(Item.category).\
#                 filter(Manufacturer.name == manufacturer).\
#                 filter(Category.name == category).all()
#     return render_template('items.html', manufacturer=manufacturer, category=category, items=items)


