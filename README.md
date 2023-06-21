# Проект YaMDb

[![Python](https://img.shields.io/badge/Python-%203.9-blue?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-%203.2-blue?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![Pytest](https://img.shields.io/badge/Pytest-%20-blue?style=flat-square&logo=pytest)](https://docs.pytest.org/en/6.2.x/)
[![Postman](https://img.shields.io/badge/Postman-%20-blue?style=flat-square&logo=postman)](https://www.postman.com/)

## Описание

Яндекс Практикум. Спринт №10. Итоговый проект. API YaMDb.

## Функционал

- Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку;
- Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка» и т.д.;
- Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»);
- Добавлять произведения, категории и жанры может только администратор;
- Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку. Из пользовательских оценок формируется усреднённая оценка произведения — рейтинг. На одно произведение пользователь может оставить только один отзыв;
- Пользователи могут оставлять комментарии к отзывам;
- Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.

## Установка
###
1. Клонировать репозиторий:

```shell
git clone https://github.com/PrimeStr/api_yamdb.git
```

2. Перейти в папку с проектом:

```shell
cd api_yamdb/
```

3. Установить виртуальное окружение для проекта:

>###### Если у вас OS Linux и MacOS
>```shell
>python3 -m venv venv
>```
>###### Если у вас OS Windows
>```shell
>python -m venv venv
>```

4. Активировать виртуальное окружение для проекта:


>#### `source` можно заменить на .
>   
>###### Если у вас OS Linux и MacOS
>```shell
>source venv/bin/activate
>```
>###### Если у вас OS Windows
>```shell
>source venv/Scripts/activate
>```
5. Установить зависимости:

```shell
pip install -r requirements.txt
```

6. Перейти в папку api_yamdb и выполнить миграции на уровне проекта:

```shell
cd api_yamdb/
```
>###### Если у вас OS Linux и MacOS
>```shell
>python3 manage.py migrate
>```
>###### Если у вас OS Windows
>```shell
>python manage.py migrate
>```


7. Запустить проект локально:

>###### Если у вас OS Linux и MacOS
>```shell
>python3 manage.py runserver
>```
>###### Если у вас OS Windows
>```shell
>python manage.py runserver
>```

## Примеры запросов

Все запросы отправляются на эндпоинт `'/api/v1/'`

Для начала нужно зарегистрировать пользователя
: Отправить POST-запрос на эндпоинт `'/auth/signup/'` и передать в нём 2 поля:

```json
{
   "email": "Ваша эл.почта",
   "username": "Ваше имя пользователя"
}
```

Получение токена

: Отправить POST-запрос на эндпоинт `'/auth/token/'` и передать в нём 2 поля:

```json
{
   "username": "Ваше имя пользователя",
   "confirmation_code": "Ваш код подтверждения с эл.почты"
}
```

В ответе от API в поле`"token"`вы получите токен. Сохраните его.
###
Получение списка всех категорий

: Отправить GET-запрос на эндпоинт `/categories/`. Возможен поиск по названию категории. В заголовке указывать тот самый скопированный ранее токен не обязательно. Эндпоинт доступен для всех. Но если нужно - просто указываем в Headers:`Authorization`:`Bearer <токен>`.


Пример ответа:

```json
{
   "count": 3,
   "next": null,
   "previous": null,
   "results": [
      {
         "name": "Фильм",
         "slug": "movie"
      },
      {
         "name": "Книга",
         "slug": "book"
      },
      {
         "name": "Музыка",
         "slug": "music"
      }
   ]
}
```



## Ресурсы


#### Документацию проекта вы можете найти по адресу:
    http://127.0.0.1:8000/redoc/
Для доступа к документации проект должен быть запущен.

###
#### Для создания и тестирования API использовался [Postman](https://www.postman.com/).

## Выражаю свою благодарность коллегам, с которыми мы разделили создание этого проекта. 
### Авторы: [Никита Станишевский](https://github.com/NikitaStanish) , [Александр Кашигин](https://github.com/Alexander-Kashigin), [Максим Головин](https://github.com/PrimeStr)