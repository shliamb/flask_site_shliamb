import sys
from pathlib import Path
root_path = str(Path(__file__).resolve().parent.parent)
sys.path.append(root_path)

# Теперь мы можем импортировать worker_db из api
from api.worker_db import read_data_main, write_data_main, update_data_main








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

data = read_data_main("https://shliamb.ru")

print(data.id)
print(data.responsive)
print(data.title)
print(data.date_create)
print(data.return_code)


# Update Page_main:
#
# id = "https://shliamb.ru"

# data = {
#     "id": "https://shliamb.ru",
#     "title": "Первая страница, а че.. не не, все "
# }

# ass = update_data_main(id, data)
# print(ass)