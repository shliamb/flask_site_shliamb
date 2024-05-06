from flask import Flask, request, render_template
from models import db
from keys import user_db, paswor_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user_db}:{paswor_db}@localhost:5432/my_database"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# связываем приложение и экземпляр SQLAlchemy
db.init_app(app)



@app.route('/')
def home():
    return render_template('main.html')



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

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)


