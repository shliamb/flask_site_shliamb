#### Relative imports ####
import sys
from pathlib import Path
root_path = str(Path(__file__).resolve().parent.parent)
sys.path.append(root_path)
#### Logging ####
import logging
logging.basicConfig(level=logging.INFO, filename='./routing/log/views.log', filemode='a', format='%(levelname)s - %(asctime)s - %(name)s - %(message)s',) 
#### Flask ####
from flask import Blueprint, Response, jsonify, render_template, request
from routing.worker_db import read_data_main, read_data_1, read_data_2, get_sitemap_db


views_blueprint = Blueprint('views', __name__)



@views_blueprint.route('/', methods=['GET'])
def get_page_main():
    id = "1"
    page_data = read_data_main(id)
    if page_data:
        return render_template('main.html', data=page_data)
    else:
        return render_template('error.html', message='Страница не найдена'), 404 



@views_blueprint.route('/sitemap.xml', methods=['GET'])
def get_sitemap():
    data = get_sitemap_db()
    if data:
        # main
        main = data["main"][0]
        main_url = main['id']
        main_date = main['date_update']
        # page_1
        page_1 = set()
        data_1 = data["page_1"]
        for n in data_1:
            page_1.add(n['id'])
        # page_2
        page_2 = set()
        data_2 = data["page_2"]
        for n in data_2:
            page_2.add(f"{n['page_1_id']}/{n['id']}")

        urls = {
            "main_url": main_url,
            "main_date": main_date,
            "page_1": page_1,
            "page_1_date": page_1_date,
            "page_2": page_2,
            }

        sitemap_xml = render_template('sitemap.xml', data=urls)
        response = Response(sitemap_xml, mimetype='application/xml')
        return response
    else:
        return render_template('error.html', message='Нет данных'), 404 



@views_blueprint.route('/<page_1>/', methods=['GET'])
def get_page_1(page_1):
    page_data = read_data_1(page_1)
    if page_data:
        return render_template('main.html', data=page_data)
    else:
        return render_template('error.html', message='Страница не найдена'), 404 


@views_blueprint.route('/<page_1>/<page_2>/', methods=['GET'])
def get_page_2(page_1, page_2):
    page_data = read_data_2(page_1, page_2)
    if page_data:
        return render_template('main.html', data=page_data)
    else:
        return render_template('error.html', message='Страница не найдена'), 404 
        


