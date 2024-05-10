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
#### Sqlalchemy ####
import sqlalchemy
from sqlalchemy import select, insert, update, extract, join, func
#### Modules ####
from routing.models import db, Page_main, Page_1, Page_2
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
        return data.serialize() if data else None
     
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





#### PAGE_1 ####
#
# Read data Page_1
def read_data_1(id):
    with app.app_context():
        data = None
        query = select(Page_1).where(Page_1.id == id)
        result = db.session.execute(query)
        data = result.scalar_one_or_none() 
        return data.serialize() if data else None
     
# Write data Page_1
def write_data_1(data):
    with app.app_context():
        try:
            db.create_all()
            query = insert(Page_1).values(**data)
            db.session.execute(query)
            db.session.commit()
            return True
        except Exception as e:
            logging.error(f"Error: write data to table page_1: {e}")
            return False

# Update data Page_1
def update_data_1(id, data):
    with app.app_context():
        try:
            query = update(Page_1).where(Page_1.id == id).values(**data)
            db.session.execute(query)
            db.session.commit()
            return True
        except Exception as e:
            logging.error(f"Error: update data to table page_1: {e}")
            return False
        






#### PAGE_2 ####
#
# Read data Page_2
def read_data_2(page_1, page_2):
    with app.app_context():
        data = None
        query = select(Page_2).where(Page_2.id == page_2).where(Page_2.page_1_id == page_1)
        result = db.session.execute(query)
        data = result.scalar_one_or_none()
        return data.serialize() if data else None
     
# Write data Page_2
def write_data_2(data):
    with app.app_context():
        try:
            db.create_all()
            query = insert(Page_2).values(**data)
            db.session.execute(query)
            db.session.commit()
            return True
        except Exception as e:
            logging.error(f"Error: write data to table page_2: {e}")
            return False

# Update data Page_2
def update_data_2(id, data):
    with app.app_context():
        try:
            query = update(Page_2).where(Page_2.id == id).values(**data)
            db.session.execute(query)
            db.session.commit()
            return True
        except Exception as e:
            logging.error(f"Error: update data to table page_2: {e}")
            return False


# Get data to genereted sitemap.xml
def get_sitemap_db():
    with app.app_context():
        data_main = db.session.query(Page_main).all()
        data_page_1 = db.session.query(Page_1).filter_by(publish=True).all()
        data_page_2 = db.session.query(Page_2).filter_by(publish=True).all()

        # Объединение данных в один список, если это возможно
        # или обработка каждого набора данных отдельно
        return {
            'main': [item.serialize() for item in data_main],
            'page_1': [item.serialize() for item in data_page_1],
            'page_2': [item.serialize() for item in data_page_2],
        }