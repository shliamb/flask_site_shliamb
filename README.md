
**Сайт на Flask**

Проект разделен на модули для гибкости и масштабируемости:

*   **APPWEB:**  Основное веб-приложение на Flask. Отображает данные из базы данных (главная, категории, комментарии).  Цель – быстрый запуск сайта с возможностью SEO-оптимизации.
*   **APPLOG:**  Сервис аутентификации/авторизации.  Планируется интеграция через Telegram (удобство, распространенность).
*   **APPADMIN:**  Админ-панель с широким функционалом. Доступ через Telegram (APPLOG). Возможности: управление видимостью страниц, SEO-настройки, загрузка данных (цены), интеграция с GPT-chat 4 (генерация title, описаний, изображений, текста), проверка ошибок, управление базой данных.

*APPWEB - только чтение данных, APPADMIN - чтение/запись.*
