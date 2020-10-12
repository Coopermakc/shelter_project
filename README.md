Это учебный проект сайта приюта для животных

Библиотеки, используемые в проекте описаны в файле requirements.
Выполнить установку библиотек из файла, выполнив команду в папке проекта
    
    pip install -r requirements.txt

Для запуска миграций выполните

    python manage.py migrate

Фикстуры находятся в файле initial_data.json

Загрузка фикстур
    python manage.py loaddata initial_data

Запуск сервера

    python manage.py runserver

Создание объектов выполняется через админку

Учетные данные для админки user_a/12qw!@QW


Ссылка на heroku

    https://obscure-wildwood-64971.herokuapp.com