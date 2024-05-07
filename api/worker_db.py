import sys
from pathlib import Path

# Добавляем путь к корневой папке проекта в sys.path
root_path = str(Path(__file__).resolve().parent.parent)
sys.path.append(root_path)

import logging
# logging.getLogger('aiogram').propagate = False # Блокировка логирование 
logging.basicConfig(level=logging.INFO, filename='./appweb/log/appweb.log', filemode='a', format='%(levelname)s - %(asctime)s - %(name)s - %(message)s',) 
from flask import Flask
from api.models import db, Page_main
import sqlalchemy
from sqlalchemy import select, insert, update, extract, join, func
from keys import user_db, paswor_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user_db}:{paswor_db}@localhost:5433/flask_database"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# связываем приложение и экземпляр SQLAlchemy
db.init_app(app)



#### PAGE_MAIN ####
#
# Read data Page_main
def read_data_main(id):
    with app.app_context():
        data = None
        query = select(Page_main).where(Page_main.id == id)
        result = db.session.execute(query)
        data = result.scalar_one_or_none() 
        return data or None
     
# Write data Page_main
def write_data_main(data):
    with app.app_context():
        try:
            db.create_all()
            query = insert(Page_main).values(**data)
            db.session.execute(query)
            db.session.commit()
            return True
        except Exception as e:
            logging.error(f"Error: write data to table page_main: {e}")
            return False

# Update data Page_main
def update_data_main(id, data):
    with app.app_context():
        try:
            query = update(Page_main).where(Page_main.id == id).values(**data)
            db.session.execute(query)
            db.session.commit()
            return True
        except Exception as e:
            logging.error(f"Error: update data to table page_main: {e}")
            return False



