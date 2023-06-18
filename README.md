# API для Yatube

[![Python](https://img.shields.io/badge/Python-%203.9-blue?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-%203.2.16-blue?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![Pytest](https://img.shields.io/badge/Pytest-%20-blue?style=flat-square&logo=pytest)](https://docs.pytest.org/en/6.2.x/)
[![Postman](https://img.shields.io/badge/Postman-%20-blue?style=flat-square&logo=postman)](https://www.postman.com/)

## Описание

Яндекс Практикум. Спринт №9. Итоговый проект. API для Yatube.

## Функционал

- Подписка и отписка от автора авторизованным пользователем;
- Авторизованный пользователь может просматривать посты, создавать новые, удалять и изменять их;
- Пользователь может просматривать список сообществ;
- Пользователь может создавать, просматривать, удалять и обновлять комментарии;
- Доступна фильтрация по подпискам.

## Установка
###
1. Клонировать репозиторий:

    ```python
    git clone https://github.com/PrimeStr/api_final_yatube.git
    ```

2. Перейти в папку с проектом:

    ```python
    cd yatube_api/
    ```

3. Установить виртуальное окружение для проекта:

    ```python
    # для OS Linux и MacOS
    python3 -m venv venv

    # для OS Windows
    python -m venv venv
    ```

4. Активировать виртуальное окружение для проекта:

    ```python
    # *source* можно заменить на .
   
    # для OS Linux и MacOS
    source venv/bin/activate

    # для OS Windows
    source venv/Scripts/activate
    ```


5. Установить зависимости:

    ```python
    pip install -r requirements.txt
    ```

6. Перейти в папку yatube_api и выполнить миграции на уровне проекта:

   ```python
   cd yatube_api
   
   # для OS Linux и MacOS
    python3 manage.py migrate

    # для OS Windows
    python manage.py migrate
   ```


7. Запустить проект локально:

   ```python
   # для OS Linux и MacOS
    python3 manage.py runserver
   
   # для OS Windows
    python manage.py runserver

## Примеры запросов

Для начала нужно зарегистрировать пользователя
: Отправить POST-запрос на эндпоинт `'api/v1/users/'` и передать в нём 2 поля:

```json
  {
      "username": "Ваше_имя_пользователя",
      "password": "Ваш_пароль"
  }
```

Получение токена

: Отправить POST-запрос на эндпоинт `'api/v1/users/'` и передать в нём 2 поля:

```json
  {
      "username": "Ваше_имя_пользователя",
      "password": "Ваш_пароль"
  }
```

В ответе от API в поле`"token"`вы получите токен. Сохраните его.

Создание поста

: Отправить POST-запрос на эндпоинт `api/v1/posts/` и передать в него обязательное поле `text`, в заголовке указать тот самый скопированный ранее токен:`Authorization`:`Bearer <токен>`.

1. Пример запроса:

   ```json
   {
     "text": "Это мой первый пост."
   }
   ```

2. Пример ответа:

   ```json
   {
     "id": 2,
     "author": "Ваше_имя_пользователя",
     "text": "Это мой первый пост.",
     "pub_date": "2023-06-4T12:00:22.021094Z",
     "image": null,
     "group": null
   }
   ```

Комментирование поста пользователя

: Отправить POST-запрос на эндпоинт `api/v1/posts/{post_id}/comments/` и передать в него обязательные поля `post`(id поста) и `text`, в заголовке так же обязательно указать токен как в предыдущем примере.

1. Пример запроса:

   ```json
   {
     "post": 1,
     "text": "Это мой первый комментарий."
   }
   ```

2. Пример ответа:

   ```json
   {
     "id": 1,
     "author": "Ваше_имя_пользователя",
     "text": "Это мой первый комментарий.",
     "created": "2023-06-4T12:12:22.021094Z",
     "post": 1
   }
   ```

## Ресурсы

```python
# Документацию проекта вы можете найти по адресу:
    http://127.0.0.1:8000/redoc/
# Для доступа к документации проект должен быть запущен.
```

```python
# Для создания и тестирования API использовался Postman:
    https://www.postman.com/
# Крайне рекомендую воспользоваться им.
```