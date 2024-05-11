#### Relative imports ####
import sys
from pathlib import Path
root_path = str(Path(__file__).resolve().parent.parent)
sys.path.append(root_path)
#### Logging ####
import logging
logging.basicConfig(level=logging.INFO, filename='./appweb/log/appweb.log', filemode='a', format='%(levelname)s - %(asctime)s - %(name)s - %(message)s',) 
#### Flask ####
from flask import Flask
#### Modules ####
from routing.api import api_blueprint
from routing.views import views_blueprint



app = Flask(__name__)


# Регистрация Blueprint'ов
app.register_blueprint(api_blueprint, url_prefix='/api') # API
app.register_blueprint(views_blueprint, url_prefix='/') # Default site


if __name__ == '__main__':
    app.run(debug=True)





























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


