from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         # проверка логина и пароля
#         return 'Вы вошли в систему!'
#     else:
#         return render_template('login.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)