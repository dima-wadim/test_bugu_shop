# Test Bugu Shop

## Описание

Test Bugu Shop - это веб-сервис, разработанный с использованием Django и Django REST Framework, который предоставляет API для работы со статьями. Пользователи могут регистрироваться, авторизоваться, просматривать и создавать статьи. Доступ к закрытым статьям доступен только для авторизованных пользователей с ролью "подписчик". 

## Функционал

- **Публичные статьи**: Доступны всем пользователям, включая неавторизованных.
- **Авторизация пользователей**: С помощью Basic Auth. В качестве логина используется email.
- **Регистрация пользователей**: Создание аккаунта с ролью "подписчик".
- **Чтение закрытых статей**: Доступно только для авторизованных пользователей с ролью "подписчик".
- **Создание статей**: Доступно только для пользователей с ролью "автор".
- **Редактирование и удаление статей**: Автор может редактировать или удалять только свои статьи.

## Требования

- Python 3.8+
- PostgreSQL
- Django 4.x
- Django REST Framework

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone <https://github.com/dima-wadim/test_bugu_shop>
    cd test_bugu_shop
    ```

2. Создайте и активируйте виртуальное окружение:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Для Linux/MacOS
    venv\Scripts\activate     # Для Windows
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Настройте подключение к базе данных в `test_bugu_shop/settings.py`:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5. Примените миграции:

    ```bash
    python manage.py migrate
    ```

6. Создайте суперпользователя:

    ```bash
    python manage.py createsuperuser
    ```

7. Запустите сервер разработки:

    ```bash
    python manage.py runserver
    ```

8. Откройте в браузере `http://127.0.0.1:8000/` для доступа к приложению.

## Развертывание на Heroku

1. Установите Heroku CLI, если он ещё не установлен.

2. Выполните вход в Heroku:

    ```bash
    heroku login
    ```

3. Создайте Heroku приложение:

    ```bash
    heroku create
    ```

4. Добавьте PostgreSQL на Heroku:

    ```bash
    heroku addons:create heroku-postgresql:hobby-dev
    ```

5. Задеплойте приложение на Heroku:

    ```bash
    git push heroku main
    ```

6. Выполните миграции на Heroku:

    ```bash
    heroku run python manage.py migrate
    ```

7. Получите ссылку на развернутое приложение и используйте её для доступа к вашему приложению.

## Лицензия

Этот проект лицензирован под лицензией MIT. Подробности см. в файле LICENSE.
