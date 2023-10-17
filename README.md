# ЯП - Спринт 22-23 - Cервис QRKot.

## Описание
Сервис QRKot позволяет создавать целевые проекты для сбора средств на нужды котиков и отправлять пожертвования в эти проекты.

## Технологии
- Python 3.9
- FastAPI 0.78.0

## Документация
# Копирование репозитория
Клонируем репозиторий
```
~ git clone git@github.com:Certelen/cat_charity_fund.git
```

# Установка
Переходим в клонированный репозиторий
```
~ cd {путь до папки с клонированным репозиторем}
~ cd cat_charity_fund
```
Устанавливаем и активируем виртуальное окружение
```
~ py -3.9 -m venv venv
~ . venv/Scripts/activate
```
Устанавливаем требуемые зависимости:
```
~ pip install -r requirements.txt
```
При необходимости можно создать файл .env и изменить стандартный настройки.

# Миграция базы данных
Применяем миграцию для базы данных:
```
~ alembic upgrade head
```
# Запуск
Запуск сервиса производится командой:
```
~ uvicorn app.main:app --reload
```
Доступ к сервису становится доступен по адресу http://127.0.0.1:8000/

## Адресные пути
- ```http://127.0.0.1:8000/docs``` и ```http://127.0.0.1:8000/redoc``` - документация к проекту.
- ```http://127.0.0.1:8000/charity_project``` - Доступ через API к целевым проектам.
- ```http://127.0.0.1:8000/donation``` - Доступ через API к пожертвованиям.
- ```http://127.0.0.1:8000/google``` - Создание отчета по времени закрытия проектов.

## Примеры запросов
- ```http://127.0.0.1:8000/auth/register``` - POST-запрос регистрирующий пользователя:
```
{
  "email": "user@example.com",
  "password": "string"
}
```
- ```http://127.0.0.1:8000/charity_project``` - GET-запрос возвращает список проектов, POST-запрос администратора создает проект:
- ```http://127.0.0.1:8000/donation``` - GET-запрос администратора возвращает список всех пожертвований, POST-запрос создает пожертвование:
- ```http://127.0.0.1:8000/donation/my``` - GET-запрос возвращает список своих пожертвований:
```
{
  "name": "string",
  "description": "string",
  "full_amount": 0
}
```
- ```http://127.0.0.1:8000/google``` - GET-запрос возвращает ссылку на отчет времени закрытых проектов.


## Автор

- :white_check_mark: [Коломейцев Дмитрий(Certelen)](https://github.com/Certelen)

Проект сделан в рамках учебного процесса по специализации Python-разработчик (back-end) Яндекс.Практикум.