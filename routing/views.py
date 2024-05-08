#### Relative imports ####
import sys
from pathlib import Path
root_path = str(Path(__file__).resolve().parent.parent)
sys.path.append(root_path)
#### Logging ####
import logging
logging.basicConfig(level=logging.INFO, filename='./routing/log/views.log', filemode='a', format='%(levelname)s - %(asctime)s - %(name)s - %(message)s',) 
#### Flask ####
from flask import Blueprint, jsonify, request
from routing.worker_db import read_data_main, read_data_1, read_data_2




views_blueprint = Blueprint('views', __name__)


@views_blueprint.route('/', methods=['GET'])
def get_page_main():
    id = "1"
    page_data = read_data_main(id)
    if page_data:
        return jsonify(page_data)
    else:
        return jsonify({'error': 'Страница не найдена'}), 404



@views_blueprint.route('/sitemap.xml', methods=['GET'])
def get_sitemap():
    return "Тут будет выводиться карта сайта, позже."



@views_blueprint.route('/<page_1>/', methods=['GET'])
def get_page_1(page_1):
    page_data = read_data_1(page_1)
    if page_data:
        return jsonify(page_data)
    else:
        return jsonify({'error': 'Страница не найдена'}), 404


@views_blueprint.route('/<page_1>/<page_2>/', methods=['GET'])
def get_page_2(page_1, page_2):
    page_data = read_data_2(page_1, page_2)
    if page_data:
        return jsonify(page_data)
    else:
        return jsonify({'error': 'Страница не найдена'}), 404
        
