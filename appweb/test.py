import sys
from pathlib import Path
root_path = str(Path(__file__).resolve().parent.parent)
sys.path.append(root_path)

# Теперь мы можем импортировать worker_db из api
from routing.worker_db import read_data_main, write_data_main, update_data_main,\
      write_data_1, read_data_1, write_data_2, read_data_2, get_sitemap_db






from datetime import datetime, timezone, timedelta

# GET DAY AND TIME
def day_utcnow(time_correction=None) -> datetime:
    if time_correction is None:
        time_correction = +3 # Moscow
    utc_zone = timezone.utc
    a = datetime.now(timezone.utc).replace(tzinfo=utc_zone)
    a = a + timedelta(hours=time_correction)
    day_str = a.strftime("%Y-%m-%d %H:%M:%S")
    day = datetime.strptime(day_str, '%Y-%m-%d %H:%M:%S')
    # print("info: Getting the day and time from the server")
    return day or None

#### Page_main ####

# Write Page_main:
#
# date = day_utcnow()
# data = {
#     "id": 1,
#     "url_site": "shliambur.ru",
#     "title": "Title - Главная страница | Shliambur",
#     "seo_title": "seo_title - Компания по разработке",
#     "seo_description": "seo_description - Компания по разработке",
#     "seo_keyword": "seo_keyword - разработка",
#     "date_update": date,
# }

# ass = write_data_main(data)
# print(ass)



# Read Page_main:

# data = read_data_main("1")

# print(data)
# print(data.id)
# print(data.responsive)
# print(data.title)
# print(data.date_create)
# print(data.return_code)


# Update Page_main:
# page_1 = "telegram-bot"
# page_2 = "vreate-bot-2"

# # # id = "site"


# data = read_data_2(page_1, page_2)

# if data:
#     print(data)
# else:
#     print("Такой страницы нэту")





#### Page_1 ####

# Write Page_main:

# date = day_utcnow()

# data = {
#     "id": "site",
#     "title": "Title - сайты",
#     "seo_title": "seo_title - сайты",
#     "seo_description": "seo_description - сайты",
#     "seo_keyword": "seo_keyword - сайты",
#     "text_body": "text_body - текст страницы",
#     "date_update": date,
# }

# ass = write_data_1(data)
# print(ass)




# # Read Page_1:
#page = "telegram-bot"
# page = "site"
# data = read_data_1(page)

# print(data)




#### Page_2 ####

# Write Page_main:

# date = day_utcnow()

# data = {
#     'id': "bot-create2",
#     'title': "title - bot-create2",
#     "seo_title": "seo_title - bot-create2",
#     "seo_description": "seo_description - bot-create2",
#     "seo_keyword": "seo_keyword - bot-create2",
#     "text_body": "text_body - bot-create2",
#     "date_update": date,
#     #'page_1_id': "site",
#     'page_1_id': "bot",
# }

# ass = write_data_2(data)
# print(ass)




# Read Page_2:
# id = "site-page"
# id = "vreate-bot-2"

# page_1 = "telegram-bot"
# page_2 = "vreate-bot-2"

# # # id = "site"


# data = read_data_2(page_1, page_2)

# if data:
#     print(data)
# else:
#     print("Такой страницы нэту")











# Read Page_main:
#data = get_sitemap_db()

# Page_main
# page_main = data["main"][0]
# print(f"https://{page_main['id']}")

# # All Page_1
# data_1 = data["page_1"]
# for n in data_1:
#     print(f"https://shliamb/{n['id']}")

# # All Page_2
# data_2 = data["page_2"]
# for n in data_2:
#     print(f"https://shliamb/{n['page_1_id']}/{n['id']}")



class MyClass():
    pass

myclass = MyClass()


print(type(myclass))

