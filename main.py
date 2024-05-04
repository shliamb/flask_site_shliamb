from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Добро пожаловать на мой сайт на Flask!'


@app.route('/about')
def about():
    return 'Здесь будет информация об авторе сайта.'

@app.route('/blog')
def blog():
    return 'Это блог с заметками о работе и увлечениях.'


@app.route('/user/<username>')
def user_profile(username):
    return f"Это профиль пользователя {username}"


if __name__ == '__main__':
    app.run(debug=False)