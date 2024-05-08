import sys
from pathlib import Path
root_path = str(Path(__file__).resolve().parent.parent)
sys.path.append(root_path)

# Теперь мы можем импортировать worker_db из api
from routing.worker_db import read_data_main, write_data_main, update_data_main,\
      write_data_1, read_data_1, write_data_2, read_data_2








#### Page_main ####

# Write Page_main:
#
# data = {
#     "id": "https://shliamb.ru",
#     "title": "Первая страница, а че.."
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

# id = "https://shliamb.ru"

# data = {
#     "id": "1",
#     "title": "Первая страница, а че.. не не, все "
# }

# ass = update_data_main(id, data)
# print(ass)






#### Page_1 ####

# Write Page_main:

# data = {
#     "id": "site",
#     'title': "Сайт"
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

# data = {
#     'id': "site-page",
#     'title': "Второстепенная страница - Старница  ",
#     'page_1_id': "site"
# }

# ass = write_data_2(data)
# print(ass)




# Read Page_2:
# id = "site-page"
# id = "vreate-bot-2"

page_1 = "telegram-bot"
page_2 = "vreate-bot-2"

# # id = "site"


data = read_data_2(page_1, page_2)

if data:
    print(data)
else:
    print("Такой страницы нэту")