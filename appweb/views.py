#### Relative imports ####
# import sys
# from pathlib import Path
# root_path = str(Path(__file__).resolve().parent.parent)
# sys.path.append(root_path)
#### Logging ####
import logging
logging.basicConfig(level=logging.INFO, filename='./routing/log/views.log', filemode='a', format='%(levelname)s - %(asctime)s - %(name)s - %(message)s',) 
#### Flask ####
from flask import Blueprint, Response, jsonify, render_template, request
from worker_db import read_data_main, read_data_1, read_data_2, get_sitemap_db, read_menu


views_blueprint = Blueprint('views', __name__)



#### MENU ####
#
# Sorting menu items
def get_menu():
    data = read_menu()
    if data is None:
        return None
    out_data = []
    for one in data:
        # Main Page
        if one.get("main_page") is None:
            out_data.append(one)
        # Secondary Page
        elif one.get("secondary_page") is None and one.get("publish") is True:
            parent = one.get("main_page")
            out_data.append(one)
            for one_sec in data:
                if one_sec.get("secondary_page") is not None and one_sec.get("main_page") == parent and one_sec.get("publish") is True:
                    out_data.append(one_sec)
    return out_data

# ROUTED MAIN PAGE
@views_blueprint.route('/', methods=['GET'])
def get_page_main():
    page_data = read_data_main(id=1)
    menu = get_menu()
    if page_data:
        return render_template("main.html", data=page_data, menu=menu)
    else:
        return render_template("error.html", message="Страница не найдена"), 404

# ROUTED 1st PAGE
@views_blueprint.route('/<page_1>/', methods=['GET'])
def get_page_1(page_1):
    page_data = read_data_1(page_1)
    menu = get_menu()
    if page_data:
        return render_template('page_1.html', data=page_data, menu=menu)
    else:
        return render_template('error.html', message='Страница не найдена'), 404 

# ROUTED 2 PAGE
@views_blueprint.route('/<page_1>/<page_2>/', methods=['GET'])
def get_page_2(page_1, page_2):
    page_data = read_data_2(page_1, page_2)
    menu = get_menu()
    if page_data:
        return render_template('page_2.html', data=page_data, menu=menu)
    else:
        return render_template('error.html', message='Страница не найдена'), 404 
        
# ROUTED and GENERATION SITEMAP
@views_blueprint.route('/sitemap.xml', methods=['GET'])
def get_sitemap():
    data = get_sitemap_db()
    if data:
            # main
        main = data["main"][0]
        main_url = f"https://{main['url_site']}"
        main_date = main.get('date_update')
        changefreq = main['changefreq']
        priority = main['priority']
            # page_1
        page_1 = set()
        data_1 = data["page_1"]
        for n in data_1:
            corp = (f"{main_url}/{n['id']}/", f"{n['date_update']}", f"{n['changefreq']}", f"{n['priority']}")
            page_1.add(corp)
            # page_2
        page_2 = set()
        data_2 = data["page_2"]
        for n in data_2:
            corp = (f"{main_url}/{n['page_1_id']}/{n['id']}/", f"{n['date_update']}", f"{n['changefreq']}", f"{n['priority']}")
            page_2.add(corp)
        urls = {
            'main_url': main_url,
            'main_date': main_date,
            'changefreq': changefreq,
            'priority': priority,
            'page_1': page_1,
            'page_2': page_2,
            }
        sitemap_xml = render_template("sitemap.xml", data=urls)
        response = Response(sitemap_xml, mimetype="application/xml")
        return response
    else:
        return render_template("error.html", message="There is no data to generate a site map, sorry."), 404 


